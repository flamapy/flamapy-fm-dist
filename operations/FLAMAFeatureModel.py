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
        FMAverageBranchingFactor
        """

        # Try to use the Find operation, which returns the atomic sets if they are found
        try:
            result = self.dm.use_operation(self.fm_model,'FMAverageBranchingFactor').get_result()
            return result
        except:
            return False
        
    def core_features(self):
        """ 
        FMCoreFeatures
        """

        # Try to use the Find operation, which returns the atomic sets if they are found
        try:
            features = self.dm.use_operation(self.fm_model,'FMCoreFeatures').get_result()
            core_features = []
            for feature in features:
                core_features.append(feature.name)
            return core_features
        except:
            return False
        
    def count_leafs(self):
        """ 
        FMCountLeafs
        """

        # Try to use the Find operation, which returns the atomic sets if they are found
        try:
            result = self.dm.use_operation(self.fm_model,'FMCountLeafs').get_result()
            return result
        except:
            return False
        
    def estimated_number_of_products(self):
        """ 
        FMEstimatedProductsNumber
        """

        # Try to use the Find operation, which returns the atomic sets if they are found
        try:
            result = self.dm.use_operation(self.fm_model,'FMEstimatedProductsNumber').get_result()
            return result
        except:
            return False

    def feature_ancestors(self,feature_name:str):
        ''' 
        FMFeatureAncestors. This operation might have an error in the implementation
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

