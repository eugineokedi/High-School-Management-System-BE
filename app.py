from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_mail import Mail, Message
from api.models import db
from dotenv import load_dotenv
from config import get_config
from flask_migrate import Migrate

# Initialize Flask app
app = Flask(__name__)

# Load environment variables from.env file
load_dotenv()

# Use the get_config() function to load the correct configuration based on FLASK_ENV
app.config.from_object(get_config())

# Initialize extensions
db.init_app(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
api = Api(app)
mail = Mail(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(port=5001,debug=app.config.get("DEBUG", False))
