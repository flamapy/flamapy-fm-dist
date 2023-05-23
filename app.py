from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

# Importing routes
from routes.operations_routes import operations_bp

# Creating the app and configuring the cors
app = Flask(__name__)
CORS(app)
app.config['API_BASE_URL'] = '/api/v2'

#Now we are configuring the self generation of swagger by means of flasgger
config = {
     "specs_route": "/docs/"
}
swag = Swagger(app,config=config,merge=True)

# Adding blueprints
app.register_blueprint(operations_bp)

@app.route("/", methods=['GET'])
def home():
    return app.send_static_file('home.html')

if __name__ == '__main__':
    app.run()
