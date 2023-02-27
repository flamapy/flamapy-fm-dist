import os

from flask import Flask, request
from validator.check import model_checker, product_checker

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './validator/models/'
app.config['ALLOWED_EXTENSIONS'] = {'uvl'}

@app.route('/api/v1')
def hello_world():
    return 'This is my first API call!'

@app.route('/api/v1/check/model', methods=['POST'])
def check_model():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
        result = model_checker(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
        if (result):
            return 'Model is valid'
        else:
            return 'Model is invalid'
    else:
        return 'No file uploaded'

@app.route('/api/v1/check/product', methods=['POST'])
def check_product():
    result = product_checker()
    return result