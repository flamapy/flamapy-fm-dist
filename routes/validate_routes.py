import os
from flask import Blueprint, request, jsonify
from operations.validate import model_validator, product_validator

validate_bp = Blueprint('validate_bp', __name__, url_prefix='/api/v1/validate')

MODEL_FOLDER = './operations/models/'
PRODUCT_FOLDER = './operations/products/'

ALLOWED_EXTENSIONS = {'uvl'}

@validate_bp.route('/model', methods=['POST'])
def check_model():
    # Get files
    uploaded_model = request.files['model']

    # Check if file is provided
    if uploaded_model.filename != '':

        # Save file
        uploaded_model.save(os.path.join(MODEL_FOLDER, uploaded_model.filename))

        # Validate
        result = model_validator(os.path.join(MODEL_FOLDER, uploaded_model.filename))

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


@validate_bp.route('/product', methods=['POST'])
def check_product():
    # Get files
    uploaded_model = request.files['model']
    uploaded_product = request.files['product']

    # Check if files are provided
    if uploaded_model.filename != '' and uploaded_product.filename != '':
        
        # Save files
        uploaded_model.save(os.path.join(MODEL_FOLDER, uploaded_model.filename))
        uploaded_product.save(os.path.join(PRODUCT_FOLDER, uploaded_product.filename))
        
        # Validate
        result = product_validator(os.path.join(MODEL_FOLDER, uploaded_model.filename), os.path.join(PRODUCT_FOLDER, uploaded_product.filename))
        
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