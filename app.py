from flask import Flask
from routes.validator_routes import validator_bp

app = Flask(__name__)

app.config['BASE_ROUTE'] = '/api/v1'

app.register_blueprint(validator_bp)

@app.route(app.config['BASE_ROUTE'], methods=['GET'])
def hello_world():
    return 'FLAMAPY API - V1 - Running and ready to use!'