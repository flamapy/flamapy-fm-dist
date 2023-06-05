#!/usr/bin/python

import fire
from flamapy.interfaces.python.FLAMAFeatureModel import FLAMAFeatureModel

class FLAMACommandLine():
    """
    This class exists only to personalize the command line interface.
    """
    def __init__(self, modelPath:str):
        self.fm=FLAMAFeatureModel(modelPath)

    def atomic_sets(self):
        return self.fm.atomic_sets()

    def average_branching_factor(self):
        return self.fm.average_branching_factor()
    
    def core_features(self):
        return self.fm.core_features()
    
    def count_leafs(self):
        return self.fm.count_leafs()
    
    def estimated_number_of_products(self):
        return self.fm.estimated_number_of_products()
    
    def feature_ancestors(self,feature_name:str):
        return self.fm.feature_ancestors(feature_name)
    
    def leaf_features(self):
        return self.fm.leaf_features()
    
    def max_depth(self):
        return self.fm.max_depth()
    
    def commonality(self,configurationPath:str):
        return self.fm.commonality(configurationPath)
    
    def dead_features(self):
        return self.fm.dead_features()
    
    def error_detection(self):
        return self.fm.error_detection()
    
    def false_optional_features(self):
        return self.fm.false_optional_features()
    
    def filter(self,configurationPath:str):
        return self.fm.filter(configurationPath)
    
    def products_number(self):
        return self.fm.products_number()
    
    def products(self):
        return self.fm.products()
    
    def valid_configuration(self,configurationPath:str):
        return self.fm.valid_configuration(configurationPath)
    
    def valid_product(self,configurationPath:str):
        return self.fm.valid_product(configurationPath)
    
    def valid(self):
        return self.fm.valid()

def flama_fm() -> None:
    fire.Fire(FLAMACommandLine)