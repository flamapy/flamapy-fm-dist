from flamapy.core.discover import DiscoverMetamodels
from flamapy.metamodels.fm_metamodel.models import FeatureModel
from typing import Optional

class FLAMAFeatureModel():

    def __init__(self, modelPath:str, configurationPath:Optional[str]=None):
        """
        This is the path in the filesystem where the model is located. 
        Any model in UVL, FaMaXML or FeatureIDE format are accepted
        """
        self.modelPath=modelPath
        """
        This is the path in the filesystem where the configuration is located. 
        Only CSV format are accepted (see documentation for more information)
        """
        self.modelPath=configurationPath
        """
        Creating the interface witht he flama framework
        """
        self.dm = DiscoverMetamodels()
        """
        We save the model for later ussage
        """
        self.fm_model=self._read(modelPath)
        """
        We create a empty sat model to avoid double transformations
        """
        self.sat_model=None
        
    def _read(self, modelPath)->FeatureModel:
        return self.dm.use_transformation_t2m(modelPath,'fm')
    
    def _transform_to_sat(self):
        if self.sat_model == None:
            self.sat_model=self.dm.use_transformation_m2m(self.fm_model,"pysat")
            
    def atomic_sets(self):
        """ 
        This operation is used to find the atomic sets in a model:
        It returns the atomic sets if they are found in the model. 
        If the model does not follow the UVL specification, an 
        exception is raised and the operation returns False.
        """

        # Try to use the Find operation, which returns the atomic sets if they are found
        try:
            atomic_sets = self.dm.use_operation(self.fm_model,'FMAtomicSets').get_result()
            result = []
            for atomic_set in atomic_sets:
                partial_set = []
                for feature in atomic_set:
                    partial_set.append(feature.name)
                result.append(partial_set)
            return result
        except:
            return False
        
    def average_branching_factor(self):
        """ 
        This refers to the average number of child features that a parent feature has in a 
        feature model. It's calculated by dividing the total number of child features by the 
        total number of parent features. A high average branching factor indicates a complex 
        feature model with many options, while a low average branching factor indicates a 
        simpler model.
        """

        # Try to use the Find operation, which returns the atomic sets if they are found
        try:
            result = self.dm.use_operation(self.fm_model,'FMAverageBranchingFactor').get_result()
            return result
        except:
            return False
        
    def count_leafs(self):
        """ 
        This operation counts the number of leaf features in a feature model. Leaf features 
        are those that do not have any child features. They represent the most specific 
        options in a product line.
        """

        # Try to use the Find operation, which returns the atomic sets if they are found
        try:
            result = self.dm.use_operation(self.fm_model,'FMCountLeafs').get_result()
            return result
        except:
            return False
        
    def estimated_number_of_products(self):
        """ 
         This is an estimate of the total number of different products that can be produced 
         from a feature model. It's calculated by considering all possible combinations of 
         features. This can be a simple multiplication if all features are independent, but 
         in most cases, constraints and dependencies between features need to be taken 
         into account.
        """

        # Try to use the Find operation, which returns the atomic sets if they are found
        try:
            result = self.dm.use_operation(self.fm_model,'FMEstimatedProductsNumber').get_result()
            return result
        except:
            return False

    def feature_ancestors(self,feature_name:str):
        ''' 
        These are the features that are directly or indirectly the parent of a given feature in 
        a feature model. Ancestors of a feature are found by traversing up the feature hierarchy. 
        This information can be useful to understand the context and dependencies of a feature.
        '''
        # Try to use the Find operation, which returns the atomic sets if they are found
        try:
            operation = self.dm.get_operation(self.fm_model,'FMFeatureAncestors')
            operation.set_feature(self.fm_model.get_feature_by_name(feature_name))
            operation.execute(self.fm_model)
            flama_result = operation.get_result()
            result = []
            for res in flama_result:
                result.append(res.name)
            return result
        except:
            return False  


    def leaf_features(self):
        """ 
        This operation is used to find leaf features in a model:
        It returns the leaf features if they are found in the model. 
        If the model does not follow the UVL specification, an 
        exception is raised and the operation returns False.
        
        Traditionally you would use the flama tool by             
        features = dm.use_operation_from_file('OperationString', model)
        however, in this tool we know that this operation is from the fm metamodel, 
        so we avoid to execute the transformation if possible
        """

        # Try to use the operation, which returns the leaf features if they are found
        try:
            features = self.dm.use_operation(self.fm_model,'FMLeafFeatures').get_result()
            leaf_features = []
            for feature in features:
                leaf_features.append(feature.name)
            return leaf_features
        except:
            return False

    def max_depth(self):
        """ 
        This operation is used to find the max depth of the tree in a model:
        It returns the max depth of the tree. 
        If the model does not follow the UVL specification, an 
        exception is raised and the operation returns False.
        """

        # Try to use the Find operation, which returns the max depth of the tree
        try:
            return self.dm.use_operation(self.fm_model,'FMMaxDepthTree').get_result()
        except:
            return False
    """
    The methods above rely on sat to be executed.
    """
    def commonality(self, configurationPath:str):
        """
        This is a measure of how often a feature appears in the products of a 
        product line. It's usually expressed as a percentage. A feature with 
        100% commonality is a core feature, as it appears in all products.
        """
        try:
            self._transform_to_sat()
            configuration = self.dm.use_transformation_t2m(configurationPath,'csvconf')
    
            operation = self.dm.get_operation(self.fm_model,'Glucose3Commonality')
            operation.set_configuration_file(configuration)
            operation.execute(self.sat_model)
            return operation.get_result()

        except:
            return False

    def core_features(self):
        """
        These are the features that are present in all products of a product line. In a feature model, 
        they are the features that are mandatory and not optional. Core features define the commonality 
        among all products in a product line. This call requires sat to be called, however, there is 
        an implementation within flama that does not requires sat. please use the framework in case of needing it. 
        """
        try:
            self._transform_to_sat()
            features = self.dm.use_operation(self.sat_model,'Glucose3CoreFeatures').get_result()
            return features
        except:
            return False
        
    def dead_features(self):
        """
        These are features that, due to the constraints and dependencies in the 
        feature model, cannot be included in any valid product. Dead features are usually 
        a sign of an error in the feature model.
        """
        try:
            self._transform_to_sat()
            features = self.dm.use_operation(self.sat_model,'Glucose3DeadFeatures').get_result()
            dead_features = []
            for feature in features:
                dead_features.append(feature.name)
            return dead_features
        except:
            return False

    def error_detection(self):
        """
        This refers to the process of identifying and locating errors in a feature model. 
        Errors can include things like dead features, false optional features, or 
        contradictions in the constraints.
        """
        try:
            self._transform_to_sat()
            #errors = self.dm.use_operation(self.sat_model,'Glucose3ErrorDetection').get_result()

            operation = self.dm.get_operation(self.sat_model,'Glucose3ErrorDetection')
            operation.feature_model=self.fm_model
            operation.execute(self.sat_model)
            result = operation.get_result()

            return result
        except:
            return False

    def false_optional_features(self):
        """
        These are features that appear to be optional in the feature model, but due to the 
        constraints and dependencies, must be included in every valid product. Like dead features, 
        false optional features are usually a sign of an error in the feature model.
        """
        try:
            self._transform_to_sat()

            operation = self.dm.get_operation(self.sat_model,'Glucose3FalseOptionalFeatures')
            operation.feature_model=self.fm_model
            operation.execute(self.sat_model)
            features = operation.get_result()
            
            false_optional_features = []
            for feature in features:
                false_optional_features.append(feature.name)
            return false_optional_features
        except:
            return False

    def filter(self, configurationPath:str):
        """
        This operation selects a subset of the products of a product line based on certain criteria. 
        For example, you might filter the products to only include those that contain a certain feature.
        """
        try:
            self._transform_to_sat()
            configuration = self.dm.use_transformation_t2m(configurationPath,'configuration')

            operation = self.dm.get_operation(self.sat_model,'Glucose3Filter')
            operation.set_configuration(configuration)
            operation.execute(self.sat_model)
            result = operation.get_result()
            return result
        except:
            return False

    def products_number(self):
        """
        This is the total number of different products that can be produced from a feature model. 
        It's calculated by considering all possible combinations of features, taking into account 
        the constraints and dependencies between features.
        """
        try:
            self._transform_to_sat()
            nop = self.dm.use_operation(self.sat_model,'Glucose3ProductsNumber').get_result()
            return nop
        except:
            return False

    def products(self):
        """
        These are the individual outcomes that can be produced from a feature model. Each product 
        is a combination of features that satisfies all the constraints and dependencies in the 
        feature model.
        """
        try:
            self._transform_to_sat()
            products = self.dm.use_operation(self.sat_model,'Glucose3Products').get_result()
            return products
        except:
            return False

    def valid_configuration(self, configurationPath:str):
        """
        This is a combination of features that satisfies all the constraints and dependencies
        in the feature model. A valid configuration can be turned into a product.
        """
        try:
            self._transform_to_sat()
            configuration = self.dm.use_transformation_t2m(configurationPath,'configuration')

            operation = self.dm.get_operation(self.sat_model,'Glucose3ValidConfiguration')
            operation.set_configuration(configuration)
            operation.execute(self.sat_model)
            result = operation.get_result()
            return result
        except:
            return False

    def valid_product(self, configurationPath:str):
        """
        This is a product that is produced from a valid configuration of features. A valid 
        product satisfies all the constraints and dependencies in the feature model.
        """
        try:
            self._transform_to_sat()
            configuration = self.dm.use_transformation_t2m(configurationPath,'configuration')
            operation = self.dm.get_operation(self.sat_model,'Glucose3ValidProduct')
            operation.set_configuration(configuration)
            operation.execute(self.sat_model)
            result = operation.get_result()
            return result
        except:
            return False

    def valid(self):
        """
        In the context of feature models, this usually refers to whether the feature model itself 
        satisfies all the constraints and dependencies. A a valid feature model is one that 
        does encodes at least a single valid product.
        """
        try:
            self._transform_to_sat()
            result = self.dm.use_operation(self.sat_model,'Glucose3Valid').get_result()
            return result
        except:
            return False


