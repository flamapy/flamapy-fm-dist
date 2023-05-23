import os
from flask import Blueprint, request, jsonify
from operations.FLAMAFeatureModel import FLAMAFeatureModel

operations_bp = Blueprint('operations_bp', __name__, url_prefix='/api/v1/operations')

MODEL_FOLDER = './resources/models/'

def _api_call(operation_name:str):
    # Get files
    uploaded_model = request.files['model']
    
    # Check if file is provided
    if uploaded_model.filename != '':

        # Save file
        uploaded_model.save(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))

        fm=FLAMAFeatureModel(os.path.join(
            MODEL_FOLDER, uploaded_model.filename))
        
        operation =getattr(fm,operation_name)

        if(operation_name=='feature_ancestors'):
            result= operation(request.form["feature"])
        else:
            result= operation()
        
        # Remove file
        os.remove(os.path.join(MODEL_FOLDER, uploaded_model.filename))
        
        # Return result
        if (result):
            return jsonify(result)
        else:
            return jsonify(error='Not valid result'), 404

'''
This is the set of operations within the fm metamodel. 
TODO This could be self generated by means of implementing classes (Operation)
'''
@operations_bp.route('/atomic_sets', methods=['POST'])
def atomic_sets():
    """This endpoint returns the atomics sets of a feature model.
    Note that this is not using sat based solving, thus, there might 
    happens to be more atomic sets to explicitly defined in the model
    ---
    tags:
      - Atomic sets
    parameters:
      - name: model
        in: formData
        type: file
        required: true
    responses:
      200:
        description: A list of lists features representing the atomic sets
        examples:
          result: 5
    """
    return _api_call("atomic_sets")

@operations_bp.route('/average_branching_factor', methods=['POST'])
def average_branching_factor():
    """This endpoint returns the average branching factor of the feature tree.
    ---
    tags:
      - Average Branching factor
    parameters:
      - name: model
        in: formData
        type: file
        required: true
    responses:
      200:
        description: A float representing the average branching factor
        examples:
          result: 5.1
    """
    return _api_call("average_branching_factor")
        
@operations_bp.route('/core_features', methods=['POST'])
def core_features():
    """This endpoint returns the core features within a feature model.
    ---
    tags:
      - Core Features
    parameters:
      - name: model
        in: formData
        type: file
        required: true
    responses:
      200:
        description: A list of core features
        examples:
          result: ['lettuce', 'tomato', 'onion']
    """
    return _api_call("core_features")

@operations_bp.route('/count_leafs', methods=['POST'])
def count_leafs():
    """This endpoint returns the core features within a feature model.
    ---
    tags:
      - Count leafs
    parameters:
      - name: model
        in: formData
        type: file
        required: true
    responses:
      200:
        description: An integer with the number of leafs within a feature model
        examples:
          result: 2
    """
    return _api_call("count_leafs")

@operations_bp.route('/estimated_number_of_products', methods=['POST'])
def estimated_number_of_products():
    """This endpoint returns an approximation of the number of features within a feature model.
    ---
    tags:
      - Estimated number of products
    parameters:
      - name: model
        in: formData
        type: file
        required: true
    responses:
      200:
        description: An integer representing an estimation of the number of products
        examples:
          result: 2324
    """
    return _api_call("estimated_number_of_products")

@operations_bp.route('/feature_ancestors', methods=['POST'])
def feature_ancestors():
    """This endpoint returns the features that are parent from a selected one.
    ---
    tags:
      - Feature Ancestors
    parameters:
      - name: model
        in: formData
        type: file
        required: true
      - name: feature
        in: formData
        type: string
        required: true
    responses:
      200:
        description: A list of feature leafs
        examples:
          result: ['lettuce', 'tomato', 'onion']
    """
    return _api_call("feature_ancestors")

@operations_bp.route('/leaf_features', methods=['POST'])
def leaf_features():
    """This endpoint returns the features that are leafs within a feature model.
    ---
    tags:
      - Leaf Features
    parameters:
      - name: model
        in: formData
        type: file
        required: true
    responses:
      200:
        description: A list of feature leafs
        examples:
          result: ['lettuce', 'tomato', 'onion']
    """
    return _api_call("leaf_features")
    
@operations_bp.route('/max_depth', methods=['POST'])
def max_depth():
    """This endpoint returns the maximum depth of the feature tree.
    ---
    tags:
      - Max depth
    parameters:
      - name: model
        in: formData
        type: file
        required: true
    responses:
      200:
        description: An integer representing the deep of the tree
        examples:
          result: 5
    """
    return _api_call("max_depth")

'''
This is the set of operations within the fm metamodel. 
TODO This could be self generated by means of implementing classes (Operation)
'''