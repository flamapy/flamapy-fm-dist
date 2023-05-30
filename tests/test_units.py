import sys
import warnings
import pytest
from operations.FLAMAFeatureModel import FLAMAFeatureModel
sys.path.append(".")

VALID_MODEL = "./resources/models/valid_model.uvl"
NON_VALID_MODEL = "./resources/models/non_valid_model.uvl"

def test_atomic_sets():
    # Prepare
    flamafm=FLAMAFeatureModel(VALID_MODEL)
    expected_result=[['Cart', 'eCommerce', 'Server', 'Web', 'Security', 'Catalog', 'v74', 'Payment', 'Shopping', 'PHP', 'Storage', 'Search'], ['LOW'], ['ENOUGH'], ['BASIC'], ['ADVANCED'], ['PayPal'], ['CreditCard'], ['Mobile'], ['HIGH'], ['STANDARD'], ['Backup'], ['Marketing'], ['SEO'], ['Socials'], ['Twitter'], ['Facebook'], ['YouTube']]

    # Act
    result = flamafm.atomic_sets()

    # Assert if the size are the same (this is to speed up the test)
    assert len(result) == len(expected_result)

def test_average_branching_factor():
    # Prepare
    flamafm=FLAMAFeatureModel(VALID_MODEL)
    
    # Act
    result = flamafm.average_branching_factor()

    # Assert
    assert result == 2.45

def test_core_features():
    # Prepare
    flamafm=FLAMAFeatureModel(VALID_MODEL)
    expected_result=['eCommerce', 'Server', 'Web', 'Catalog', 'Search', 'Shopping', 'Security', 'Cart', 'Payment', 'PHP', 'Storage', 'v74']
    # Act
    result = flamafm.core_features()

    # Assert
    assert sorted(result) == sorted(expected_result)

def test_count_leafs():
    # Prepare
    flamafm=FLAMAFeatureModel(VALID_MODEL)
    
    # Act
    result = flamafm.count_leafs()

    # Assert
    assert result == 17

def test_estimated_number_of_products():
    # Prepare
    flamafm=FLAMAFeatureModel(VALID_MODEL)
    
    # Act
    result = flamafm.estimated_number_of_products()

    # Assert
    assert result == 1904


def test_estimated_number_of_products():
    # Prepare
    flamafm=FLAMAFeatureModel(VALID_MODEL)
    
    # Act
    result = flamafm.estimated_number_of_products()

    # Assert
    assert result == 1904

def test_feature_ancestors():
    # Prepare
    flamafm=FLAMAFeatureModel(VALID_MODEL)
    
    # Act
    result = flamafm.feature_ancestors("v74")

    # Assert
    assert result == ['PHP', 'Server', 'eCommerce']    

def test_leaf_features():
    # Prepare
    flamafm=FLAMAFeatureModel(VALID_MODEL)
    
    # Act
    result = flamafm.leaf_features()

    # Assert
    assert sorted(result) == sorted(['v74', 'LOW', 'ENOUGH', 'Catalog', 'BASIC', 'ADVANCED', 'Cart', 'PayPal', 'CreditCard', 'Mobile', 'HIGH', 'STANDARD', 'Backup', 'SEO', 'Twitter', 'Facebook', 'YouTube'])

def test_maxdep():
    # Prepare
    flamafm=FLAMAFeatureModel(VALID_MODEL)
    
    # Act
    result = flamafm.max_depth()

    # Assert
    assert result == 4
