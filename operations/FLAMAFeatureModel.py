from flamapy.core.discover import DiscoverMetamodels
from flamapy.metamodels.fm_metamodel.models import FeatureModel

class FLAMAFeatureModel():

    def __init__(self, modelPath:str, configurationPath:str):
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
            features = self.dm.use_operation(self.fm_model,'FMLeafFeatures')
            leaf_features = []
            for feature in features:
                leaf_features.append(feature.name)
            return leaf_features
        except:
            return False


    def valid_products(self):
        """ 
        This operation is used to find products in a model:
        It returns the product if it is found in the model. 
        If the model does not follow the UVL specification, an 
        exception is raised and the operation returns False.
        
        This operation requires the model to be translated to sat, 
        so we check if thats done
        """

        
        # Try to use the operation, which returns the product if it is found
        try:
            self._transform_to_sat()
            return self.dm.use_operation('Products', self.sat_model)
        except:
            return False


    def core_features(self):
        """ 
        This operation is used to find the core features in a model:
        It returns the core if it is found in the model. 
        If the model does not follow the UVL specification, an 
        exception is raised and the operation returns False.
        
        This operation requires the model to be translated to sat, 
        so we check if thats done
        """


        # Try to use the Find operation, which returns the core if it is found
        try:
            self._transform_to_sat()
            features = self.dm.use_operation('CoreFeatures', self.sat_model)
            core_features = []
            for feature in features:
                core_features.append(feature.name)
            return core_features
        except:
            return False


    def dead_features(self,model):
        """ 
        This operation is used to find the dead features in a model:
        It returns the dead if it is found in the model. 
        If the model does not follow the UVL specification, an 
        exception is raised and the operation returns False.
        """

        # Try to use the Find operation, which returns the dead if it is found
        try:
            self._transform_to_sat()
            features = self.dm.use_operation('DeadFeatures', self.sat_model)
            dead_features = []
            for feature in features:
                dead_features.append(feature.name)
            return dead_features
        except Exception as e:
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
            return self.dm.use_operation(self.fm_model,'FMMaxDepthTree')
        except:
            return False


    def atomic_sets(self):
        """ 
        This operation is used to find the atomic sets in a model:
        It returns the atomic sets if they are found in the model. 
        If the model does not follow the UVL specification, an 
        exception is raised and the operation returns False.
        """

        # Try to use the Find operation, which returns the atomic sets if they are found
        try:
            atomic_sets = self.dm.use_operation(self.fm_model,'AtomicSets')
            result = []
            for atomic_set in atomic_sets:
                partial_set = []
                for feature in atomic_set:
                    partial_set.append(feature.name)
                result.append(partial_set)
            return result
        except:
            return False



    def number_of_products(self,model):
        """ 
        This operation is used to count the number of products in a model:
        It returns the number of products in the model. 
        If the model does not follow the UVL specification, an 
        exception is raised and the operation returns False.
        """

        # Try to use the Products operation, which returns a list of products
        # TODO This operation is more officient in BDD, analyze if is worth to include its use
        try:
            self._transform_to_sat()
            return self.dm.use_operation(self.sat_model,'ProductsNumber')
        except:
            return False


    def number_of_feature_leafs(self):
        """ 
        This operation is used to count the number of leafs in a model:
        It returns the number of leafs in the model. 
        If the model does not follow the UVL specification, an 
        exception is raised and the operation returns False.
        """

        # Try to use the Leafs operation, which returns a list of leafs
        try:
            return self.dm.use_operation(self.fm_model,'CountLeafs')
        except:
            return False


    def valid_fm(self):
        """ 
        This operation is used to validate a model:
        It returns True if the model is valid, False otherwise. 
        If the model does not follow the UVL specification, an 
        exception is raised and the operation returns False.
        """
        # Try to use the Valid operation, which returns True if the model is valid

        try:
            self._transform_to_sat()
            return self.dm.use_operation(self.sat_model,'Valid')
        except:
            return False
    '''
    def valid_product(model, product):
        """
        This operation is used to validate a product:
        It returns True if the product is valid, False otherwise.
        If the model does not follow the UVL specification, an
        exception is raised and the operation returns False.
        """

        dm = DiscoverMetamodels()

        # Change the file extension of product.csv to csvconf
        product_csvconf = product.replace('.csv', '.csvconf')

        # Save the configuration file with new extension
        with open(product_csvconf, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            with open(product, newline='') as original_csvfile:
                csv_reader = csv.reader(original_csvfile)
                for row in csv_reader:
                    csv_writer.writerow(row)

        # Try to use the Valid operation, which returns True if the configuration is valid
        try:
            result = dm.use_operation_from_file(
                'ValidProduct', model, configuration_file=product_csvconf)
            # delete the csvconf file
            os.remove(product_csvconf)
            return result
        except:
            # delete the csvconf file
            os.remove(product_csvconf)
            return False


    def valid_configuration(model, configuration):
        """
        This operation is used to validate a configuration:
        It returns True if the configuration is valid, False otherwise.
        If the model does not follow the UVL specification, an
        exception is raised and the operation returns False.
        """
        dm = DiscoverMetamodels()

        # Change the file extension of configuration to csvconf
        configuration_csvconf = configuration.replace('.csv', '.csvconf')

        # Save the configuration file with new extension
        with open(configuration_csvconf, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            with open(configuration, newline='') as original_csvfile:
                csv_reader = csv.reader(original_csvfile)
                for row in csv_reader:
                    csv_writer.writerow(row)

        # Try to use the Valid operation, which returns True if the configuration is valid
        try:
            result = dm.use_operation_from_file(
                'ValidConfiguration', model, configuration_file=configuration_csvconf)
            # delete the csvconf file
            os.remove(configuration_csvconf)
            return result
        except:
            # delete the csvconf file
            os.remove(configuration_csvconf)
            return False
    '''