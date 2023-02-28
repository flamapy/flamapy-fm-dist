import sys
import warnings
from app import app
import pytest
from operations.validate import model_validator, product_validator

sys.path.append("..")
warnings.filterwarnings("ignore", category=DeprecationWarning)

def test_model_validator_valid_model():
    # Arrange
    valid_model = "../operations/models/valid_model.uvl"

    # Act
    result = model_validator(valid_model)

    # Assert
    assert result == True

def test_model_validator_invalid_model():
    # Arrange
    invalid_model = "../operations/products/valid_product.csv"

    # Act
    result = model_validator(invalid_model)

    # Assert
    assert result == False