from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_mail import Mail, Message
from api.models import db
from config import Config
from flask_migrate import Migrate
from api.controllers.disciplineRecord_controller import discipline_record_bp

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

app.register_blueprint(discipline_record_bp)

if __name__ == '__main__':
    app.run(debug=app.config.get("DEBUG", False))  # Run with debug based on config
