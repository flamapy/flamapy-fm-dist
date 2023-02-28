import os
from flask import Blueprint, request, jsonify
from operations.find import find_valid_products, find_core_features

find_bp = Blueprint('find_bp', __name__, url_prefix='/api/v1/find')

MODEL_FOLDER = './operations/models/'

ALLOWED_EXTENSIONS = {'uvl'}

@find_bp.route('/valid-products', methods=['POST'])
def valid_products():
    # Get files
     uploaded_model = request.files['model']
    
     # Check if file is provided
     if uploaded_model.filename != '':
    
          # Save file
          uploaded_model.save(os.path.join(
                MODEL_FOLDER, uploaded_model.filename))
    
          # Count
          result = find_valid_products(os.path.join(
                MODEL_FOLDER, uploaded_model.filename))
    
          # Remove file
          os.remove(os.path.join(MODEL_FOLDER, uploaded_model.filename))
    
          # Return result
          if (result):
                return jsonify(result)
          else:
                return jsonify(error='No valid products found'), 404


@find_bp.route('/core-features', methods=['POST'])
def core_features():
    # Get files
     uploaded_model = request.files['model']
    
     # Check if file is provided
     if uploaded_model.filename != '':
    
          # Save file
          uploaded_model.save(os.path.join(
                MODEL_FOLDER, uploaded_model.filename))
    
          # Count
          result = find_core_features(os.path.join(
                MODEL_FOLDER, uploaded_model.filename))
    
          # Remove file
          os.remove(os.path.join(MODEL_FOLDER, uploaded_model.filename))
    
          # Return result
          if (result):
                return jsonify(result)
          else:
                return jsonify(error='No core features found'), 404
