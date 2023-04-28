from typing import NewType
from flamapy.core.discover import DiscoverMetamodels


def get_plugins():
    """ 
    This operation is used to get the list of plugins:
    It returns the list of installed plugins. 
    """

    # Use the operation from the DiscoverMetamodels class
    dm = DiscoverMetamodels()

    # Try to use the Products operation, which returns a list of products
    try:
        return dm.get_plugins()
    except:
        return False


def get_operations(plugin):
    """ 
    This operation is used to get the list of operations:
    It returns a list of operations. 
    If the operation does not exist, an
    exception is raised and the operation returns False.
    """

    # Use the operation from the DiscoverMetamodels class
    dm = DiscoverMetamodels()

    # Try to use the Products operation, which returns a list of products
    try:
        return dm.get_name_operations_by_plugin(plugin)
    except:
        return False
