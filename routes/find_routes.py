import os
from flask import Blueprint, request, jsonify
from operations.find import find_valid_products, find_core_features, find_dead_features, find_max_depth, find_atomic_sets, find_leaf_features

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

            # Count
            result = find_leaf_features(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))

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


@find_bp.route('/dead-features', methods=['POST'])
def dead_features():
      # Get files
      uploaded_model = request.files['model']

      # Check if file is provided
      if uploaded_model.filename != '':

            # Save file
            uploaded_model.save(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))

            # Count
            result = find_dead_features(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))

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

        # Count
        result = find_max_depth(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))

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
        result = find_atomic_sets(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))

        # Remove file
        os.remove(os.path.join(MODEL_FOLDER, uploaded_model.filename))

        # Return result
        if (result):
            return jsonify(result)
        else:
            return jsonify(error='No atomic sets found'), 404
