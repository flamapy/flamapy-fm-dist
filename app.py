import os

from flask import Flask, request, jsonify
from operations.validate import model_validator, product_validator

app = Flask(__name__)

app.config['BASE_ROUTE'] = '/api/v1'
app.config['MODEL_FOLDER'] = './operations/models/'
app.config['PRODUCT_FOLDER'] = './operations/products/'
app.config['ALLOWED_EXTENSIONS'] = {'uvl'}


@app.route(app.config['BASE_ROUTE'], methods=['GET'])
def hello_world():
    return 'FLAMAPY API - V1 - Running and ready to use!'


@app.route(app.config['BASE_ROUTE'] + '/validate/model', methods=['POST'])
def check_model():
    # Get files
    uploaded_model = request.files['model']

    # Check if file is provided
    if uploaded_model.filename != '':

        # Save file
        uploaded_model.save(os.path.join(app.config['MODEL_FOLDER'], uploaded_model.filename))

        # Validate
        result = model_validator(os.path.join(app.config['MODEL_FOLDER'], uploaded_model.filename))

        # Remove file
        os.remove(os.path.join(app.config['MODEL_FOLDER'], uploaded_model.filename))

        # Return result
        if (result):
            return 'Model is valid'
        else:
            return jsonify(error='Model is not valid'), 404
    
    # If no file is provided
    else:
        return 'No file uploaded'


@app.route(app.config['BASE_ROUTE'] + '/validate/product', methods=['GET'])
def check_product():
    # Get files
    uploaded_model = request.files['model']
    uploaded_product = request.files['product']

    # Check if files are provided
    if uploaded_model.filename != '' and uploaded_product.filename != '':
        
        # Save files
        uploaded_model.save(os.path.join(app.config['MODEL_FOLDER'], uploaded_model.filename))
        uploaded_product.save(os.path.join(app.config['PRODUCT_FOLDER'], uploaded_product.filename))
        
        # Validate
        result = product_validator(os.path.join(app.config['MODEL_FOLDER'], uploaded_model.filename), os.path.join(app.config['PRODUCT_FOLDER'], uploaded_product.filename))
        
        # Remove files
        os.remove(os.path.join(app.config['MODEL_FOLDER'], uploaded_model.filename))
        os.remove(os.path.join(app.config['PRODUCT_FOLDER'], uploaded_product.filename))

        # Return result
        if (result):
            return 'Product is valid'
        else:
            return jsonify(error='Product is not valid'), 404

    # If no file is provided
    else:
        return 'No file or product provided'
