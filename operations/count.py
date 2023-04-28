from flamapy.core.discover import DiscoverMetamodels


def count_valid_products(model):
    """ 
    This operation is used to count the number of products in a model:
    It returns the number of products in the model. 
    If the model does not follow the UVL specification, an 
    exception is raised and the operation returns False.
    """

    # Use the operation from the DiscoverMetamodels class
    dm = DiscoverMetamodels()

    # Try to use the Products operation, which returns a list of products
    try:
        return dm.use_operation_from_file('ProductsNumber', model)
    except:
        return False


def count_leafs(model):
    """ 
    This operation is used to count the number of leafs in a model:
    It returns the number of leafs in the model. 
    If the model does not follow the UVL specification, an 
    exception is raised and the operation returns False.
    """

    # Use the operation from the DiscoverMetamodels class
    dm = DiscoverMetamodels()

    # Try to use the Leafs operation, which returns a list of leafs
    try:
        return dm.use_operation_from_file('CountLeafs', model)
    except:
        return False
