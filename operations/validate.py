import os
import csv
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


def configuration_validator(model, configuration):
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
