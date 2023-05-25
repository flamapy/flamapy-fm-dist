import fire
from operations.FLAMAFeatureModel import FLAMAFeatureModel

from typing import Optional

class FLAMACommandLine():
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
if __name__ == "__main__":
    fire.Fire(FLAMACommandLine)