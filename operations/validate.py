import os
from flamapy.core.discover import DiscoverMetamodels


def model_validator(model):
    """ 
    This operation is used to validate a model:
    It returns True if the model is valid, False otherwise. 
    If the model does not follow the UVL specification, an 
    exception is raised and the operation returns False.
    """

    # Use the operation from the DiscoverMetamodels class
    dm = DiscoverMetamodels()

    # Try to use the Valid operation, which returns True if the model is valid

    try:
        return dm.use_operation_from_file('Valid', model)
    except:
        return False


def product_validator(model, product):
    """
    This operation is used to validate a product:
    It returns True if the product is valid, False otherwise.
    If the model does not follow the UVL specification, an
    exception is raised and the operation returns False.
    """

    dm = DiscoverMetamodels()

    product_path = product
    csvconf_path = product.replace(".csv", ".csvconf")

    os.rename(product_path, csvconf_path)

    # Try to use the Valid operation, which returns True if the product is valid



def configuration_validator(model, configuration):
    """
    This operation is used to validate a configuration:
    It returns True if the configuration is valid, False otherwise.
    If the model does not follow the UVL specification, an
    exception is raised and the operation returns False.
    """


    configuration_path = configuration
    csvconf_path = configuration.replace(".csv", ".csvconf")

    os.rename(configuration_path, csvconf_path)

    #save changes
    

    dm = DiscoverMetamodels()


    # Try to use the Valid operation, which returns True if the configuration is valid



print("PRODUCT: ", product_validator("./operations/models/valid_model.uvl",
      "./operations/products/valid_product.csv"))
print("CONFIG: ", configuration_validator("./operations/models/valid_model.uvl",
      "./operations/configurations/valid_configuration.csv"))
