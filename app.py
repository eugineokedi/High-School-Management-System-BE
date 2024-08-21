from flask import Flask
from flask_jwt_extended import JWTManager
from api.routes.auth_routes import LoginResource
from flask_restful import Api
from api.models import db
from config import Config
from flask_mail import Mail


app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
jwt = JWTManager(app)
api = Api(app)
mail = Mail(app)

# Add routes
api.add_resource(LoginResource, '/auth/login')

if __name__ == '__main__':
    app.run()
