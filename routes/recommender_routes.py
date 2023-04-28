import os
from flask import Blueprint, request, jsonify
from operations.recommender import check_recommendation_objects, get_recommendations, restrictiveness

recommender_bp = Blueprint('recommender_bp', __name__,
                           url_prefix='/api/v1/recommendations')

MODEL_FOLDER = './resources/models/'
PRODUCT_FOLDER = './resources/products/'
CONFIGURATION_FOLDER = './resources/configurations/'
RECOMMENDER_FOLDER = './resources/recommendations/'


@recommender_bp.route('/validate', methods=['POST'])
def validate():

    # Get files
    model = request.files['model']
    products = request.files['products']
    query = request.files['query']

    # Check if files are provided
    if model.filename != '' and products.filename != '' and query.filename != '':

        # Save files
        model.save(os.path.join(MODEL_FOLDER, model.filename))
        products.save(os.path.join(PRODUCT_FOLDER, products.filename))
        query.save(os.path.join(PRODUCT_FOLDER, query.filename))

        # Validate
        result = check_recommendation_objects(os.path.join(MODEL_FOLDER, model.filename), os.path.join(
            PRODUCT_FOLDER, products.filename), os.path.join(PRODUCT_FOLDER, query.filename))

        # Remove files
        os.remove(os.path.join(MODEL_FOLDER, model.filename))
        os.remove(os.path.join(PRODUCT_FOLDER, products.filename))
        os.remove(os.path.join(PRODUCT_FOLDER, query.filename))

        # Return result
        if (result == 1):
            return 'Objects are valid'
        else:
            return result

    # If no file is provided
    else:
        return 'No file uploaded'


@recommender_bp.route('/', methods=['POST'])
def recommend():

    # Get files
    model = request.files['model']
    products = request.files['products']
    query = request.files['query']

    # Check if files are provided
    if model.filename != '' and products.filename != '' and query.filename != '':

        # Save files
        model.save(os.path.join(MODEL_FOLDER, model.filename))
        products.save(os.path.join(PRODUCT_FOLDER, products.filename))
        query.save(os.path.join(PRODUCT_FOLDER, query.filename))

        # Result
        result = get_recommendations(os.path.join(MODEL_FOLDER, model.filename), os.path.join(
            PRODUCT_FOLDER, products.filename), os.path.join(PRODUCT_FOLDER, query.filename))

        # Remove files
        os.remove(os.path.join(MODEL_FOLDER, model.filename))
        os.remove(os.path.join(PRODUCT_FOLDER, products.filename))
        os.remove(os.path.join(PRODUCT_FOLDER, query.filename))

        # Return result
        return result

    # If no file is provided
    else:
        return 'No file uploaded'


@recommender_bp.route('/analysis/restrictiveness', methods=['POST'])
def restrictiveness_route():

    # Get files
    model = request.files['model']
    products = request.files['products']
    features = request.form.getlist('features')
    
    # split by comma
    features = [x.strip() for x in features[0].split(',')]

    # Check if files are provided
    if model.filename != '' and products.filename != '' and len(features) != 0:

        # Save files
        model.save(os.path.join(MODEL_FOLDER, model.filename))
        products.save(os.path.join(PRODUCT_FOLDER, products.filename))

        # Result
        result = restrictiveness(os.path.join(MODEL_FOLDER, model.filename), os.path.join(
            PRODUCT_FOLDER, products.filename), features)

        # Remove files
        os.remove(os.path.join(MODEL_FOLDER, model.filename))
        os.remove(os.path.join(PRODUCT_FOLDER, products.filename))

        # Return result
        return str(result)

    # If no file is provided
    else:
        return 'No file uploaded'
