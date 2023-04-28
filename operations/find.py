from flamapy.core.discover import DiscoverMetamodels


def find_leaf_features(model):
    """ 
    This operation is used to find leaf features in a model:
    It returns the leaf features if they are found in the model. 
    If the model does not follow the UVL specification, an 
    exception is raised and the operation returns False.
    """

    # Use the operation from the DiscoverMetamodels class
    dm = DiscoverMetamodels()

    # Try to use the Find operation, which returns the leaf features if they are found
    try:
        features = dm.use_operation_from_file('FMLeafFeatures', model)
        leaf_features = []
        for feature in features:
            leaf_features.append(feature.name)
        return leaf_features
    except:
        return False


def find_valid_products(model):
    """ 
    This operation is used to find products in a model:
    It returns the product if it is found in the model. 
    If the model does not follow the UVL specification, an 
    exception is raised and the operation returns False.
    """

    # Use the operation from the DiscoverMetamodels class
    dm = DiscoverMetamodels()

    # Try to use the Find operation, which returns the product if it is found
    try:
        return dm.use_operation_from_file('Products', model)
    except:
        return False


def find_core_features(model):
    """ 
    This operation is used to find the core features in a model:
    It returns the core if it is found in the model. 
    If the model does not follow the UVL specification, an 
    exception is raised and the operation returns False.
    """

    # Use the operation from the DiscoverMetamodels class
    dm = DiscoverMetamodels()

    # Try to use the Find operation, which returns the core if it is found
    try:
        features = dm.use_operation_from_file('CoreFeatures', model)
        core_features = []
        for feature in features:
            core_features.append(feature.name)
        return core_features
    except:
        return False


def find_dead_features(model):
    """ 
    This operation is used to find the dead features in a model:
    It returns the dead if it is found in the model. 
    If the model does not follow the UVL specification, an 
    exception is raised and the operation returns False.
    """

    # Use the operation from the DiscoverMetamodels class
    dm = DiscoverMetamodels()

    # Try to use the Find operation, which returns the dead if it is found
    try:
        features = dm.use_operation_from_file('DeadFeatures', model)
        dead_features = []
        for feature in features:
            dead_features.append(feature.name)
        return dead_features
    except Exception as e:
        return False


def find_max_depth(model):
    """ 
    This operation is used to find the max depth of the tree in a model:
    It returns the max depth of the tree. 
    If the model does not follow the UVL specification, an 
    exception is raised and the operation returns False.
    """

    # Use the operation from the DiscoverMetamodels class
    dm = DiscoverMetamodels()

    # Try to use the Find operation, which returns the max depth of the tree
    try:
        return dm.use_operation_from_file('FMMaxDepthTree', model)
    except:
        return False


def find_atomic_sets(model):
    """ 
    This operation is used to find the atomic sets in a model:
    It returns the atomic sets if they are found in the model. 
    If the model does not follow the UVL specification, an 
    exception is raised and the operation returns False.
    """

    # Use the operation from the DiscoverMetamodels class
    dm = DiscoverMetamodels()

    # Try to use the Find operation, which returns the atomic sets if they are found
    try:
        atomic_sets = dm.use_operation_from_file('AtomicSets', model)
        result = []
        for atomic_set in atomic_sets:
            partial_set = []
            for feature in atomic_set:
                partial_set.append(feature.name)
            result.append(partial_set)
        return result
    except:
        return False
