import os
from flask import Blueprint, request, jsonify
from operations.FLAMAFeatureModel import FLAMAFeatureModel

solver_bp = Blueprint('count_bp', __name__, url_prefix='/api/v1/count')

MODEL_FOLDER = './resources/models/'


@validate_bp.route('/model', methods=['POST'])
def check_model():
    # Get files
    uploaded_model = request.files['model']

    # Check if file is provided
    if uploaded_model.filename != '':

        # Save file
        uploaded_model.save(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))

        
        fm=FLAMAFeatureModel(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))

        result = fm.valid_fm()

        # Remove file
        os.remove(os.path.join(MODEL_FOLDER, uploaded_model.filename))

        # Return result
        if (result):
            return 'Model is valid'
        else:
            return jsonify(error='Model is not valid'), 404

    # If no file is provided
    else:
        return 'No file uploaded'

"""
@validate_bp.route('/product', methods=['POST'])
def check_product():
    # Get files
    uploaded_model = request.files['model']
    uploaded_product = request.files['product']

    # Check if files are provided
    if uploaded_model.filename != '' and uploaded_product.filename != '':

        # Save files
        uploaded_model.save(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))
        uploaded_product.save(os.path.join(
            PRODUCT_FOLDER, uploaded_product.filename))

        # Validate
        result = product_validator(os.path.join(MODEL_FOLDER, uploaded_model.filename), os.path.join(
            PRODUCT_FOLDER, uploaded_product.filename))

        # Remove files
        os.remove(os.path.join(MODEL_FOLDER, uploaded_model.filename))
        os.remove(os.path.join(PRODUCT_FOLDER, uploaded_product.filename))

        # Return result
        if (result):
            return 'Product is valid'
        else:
            return jsonify(error='Product is not valid'), 404

    # If no file is provided
    else:
        return 'No file or product provided'


@validate_bp.route('/configuration', methods=['POST'])
def check_configuration():
    # Get files
    uploaded_model = request.files['model']
    uploaded_configuration = request.files['configuration']

    # Check if files are provided
    if uploaded_model.filename != '' and uploaded_configuration.filename != '':

        # Save files
        uploaded_model.save(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))
        uploaded_configuration.save(os.path.join(
            CONFIGURATION_FOLDER, uploaded_configuration.filename))

        # Validate
        result = configuration_validator(os.path.join(MODEL_FOLDER, uploaded_model.filename), os.path.join(
            CONFIGURATION_FOLDER, uploaded_configuration.filename))

        # Remove files
        os.remove(os.path.join(MODEL_FOLDER, uploaded_model.filename))
        os.remove(os.path.join(CONFIGURATION_FOLDER,
                  uploaded_configuration.filename))

        # Return result
        if (result):
            return 'Configuration is valid'
        else:
            return jsonify(error='Configuration is not valid'), 404

    # If no file is provided
    else:
        return 'No file or configuration provided'
"""

@count_bp.route('/valid-products', methods=['POST'])
def valid_products():
   # Get files
    uploaded_model = request.files['model']

    # Check if file is provided
    if uploaded_model.filename != '':

        # Save file
        uploaded_model.save(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))

        fm=FLAMAFeatureModel(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))
        # Count
        result = fm.number_of_products()

        # Remove file
        os.remove(os.path.join(MODEL_FOLDER, uploaded_model.filename))

        # Return result
        if (result):
            return jsonify(result)
        else:
            return jsonify(error='No valid products found'), 404


@count_bp.route('/leafs', methods=['POST'])
def leafs():
    # Get files
    uploaded_model = request.files['model']

    # Check if file is provided
    if uploaded_model.filename != '':

        # Save file
        uploaded_model.save(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))

        # Count
        fm=FLAMAFeatureModel(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))
        # Count
        result = fm.number_of_feature_leafs()

        # Remove file
        os.remove(os.path.join(MODEL_FOLDER, uploaded_model.filename))

        # Return result
        if (result):
            return jsonify(result)
        else:
            return jsonify(error='No leafs found'), 404
