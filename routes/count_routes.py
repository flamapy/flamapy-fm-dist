import os
from flask import Blueprint, request, jsonify
from operations.count import count_valid_products, count_leafs

count_bp = Blueprint('count_bp', __name__, url_prefix='/api/v1/count')

MODEL_FOLDER = './resources/models/'


@count_bp.route('/valid-products', methods=['POST'])
def valid_products():
   # Get files
    uploaded_model = request.files['model']

    # Check if file is provided
    if uploaded_model.filename != '':

        # Save file
        uploaded_model.save(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))

        # Count
        result = count_valid_products(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))

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
        result = count_leafs(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))

        # Remove file
        os.remove(os.path.join(MODEL_FOLDER, uploaded_model.filename))

        # Return result
        if (result):
            return jsonify(result)
        else:
            return jsonify(error='No leafs found'), 404
