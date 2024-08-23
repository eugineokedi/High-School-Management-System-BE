from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_mail import Mail, Message
from api.routes.auth_routes import AuthLogin, AuthSignup
from api.models import db
from config import Config
from flask_migrate import Migrate 

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
api = Api(app)
mail = Mail(app)
migrate = Migrate(app, db) 

# Add routes
api.add_resource(AuthLogin, '/auth/login')
api.add_resource(AuthSignup, '/auth/signup')
api.add_resource()
api.add_resource()
api.add_resource()
api.add_resource()
api.add_resource()
api.add_resource()
api.add_resource()

if __name__ == '__main__':
    app.run(debug=app.config.get("DEBUG", False))  # Run with debug based on config
