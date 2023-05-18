import os
from flask import Blueprint, request, jsonify
from operations.FLAMAFeatureModel import FLAMAFeatureModel

find_bp = Blueprint('find_bp', __name__, url_prefix='/api/v1/find')

MODEL_FOLDER = './resources/models/'


@find_bp.route('/leaf-features', methods=['POST'])
def leaf_features():
    # Get files
      uploaded_model = request.files['model']

      # Check if file is provided
      if uploaded_model.filename != '':

            # Save file
            uploaded_model.save(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))

            fm=FLAMAFeatureModel(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))

            result = fm.leaf_features()

            # Remove file
            os.remove(os.path.join(MODEL_FOLDER, uploaded_model.filename))
            
            

            # Return result
            if (result):
                  return jsonify(result)
            else:
                  return jsonify(error='No valid products found'), 404

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
            fm=FLAMAFeatureModel(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))
            # Count
            result = fm.valid_products()
            
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


            fm=FLAMAFeatureModel(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))

            result = fm.core_features()
            
            # Remove file
            os.remove(os.path.join(MODEL_FOLDER, uploaded_model.filename))

            # Return result
            if (result):
                  return jsonify(result)
            else:
                  return jsonify(error='No core features found'), 404


@find_bp.route('/dead-features', methods=['POST'])
def dead_features():
      # Get files
      uploaded_model = request.files['model']

      # Check if file is provided
      if uploaded_model.filename != '':

            # Save file
            uploaded_model.save(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))

            fm=FLAMAFeatureModel(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))

            result = fm.dead_features()
            
            # Remove file
            os.remove(os.path.join(MODEL_FOLDER, uploaded_model.filename))

            # Return result
            if (result):
                  return jsonify(result)
            else:
                  return jsonify(result), 404


@find_bp.route('/max-depth', methods=['POST'])
def max_depth():
    # Get files
    uploaded_model = request.files['model']

    # Check if file is provided
    if uploaded_model.filename != '':

        # Save file
        uploaded_model.save(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))

        fm=FLAMAFeatureModel(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))

        result = fm.max_depth()
        
        # Remove file
        os.remove(os.path.join(MODEL_FOLDER, uploaded_model.filename))

        # Return result
        if (result):
            return jsonify(result)
        else:
            return jsonify(error='No max depth found'), 404


@find_bp.route('/atomic-sets', methods=['POST'])
def atomic_sets():
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

        result = fm.atomic_sets()

        # Remove file
        os.remove(os.path.join(MODEL_FOLDER, uploaded_model.filename))

        # Return result
        if (result):
            return jsonify(result)
        else:
            return jsonify(error='No atomic sets found'), 404
