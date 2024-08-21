from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_mail import Mail
from api.routes.auth_routes import LoginResource
from api.models import db
from config import Config
from flask_migrate import Migrate  # Optional, for handling migrations

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
jwt = JWTManager(app)
api = Api(app)
mail = Mail(app)
migrate = Migrate(app, db)  # Optional, for migrations

# Add routes
api.add_resource(LoginResource, '/auth/login')

# Error handling
@app.errorhandler(404)
def not_found_error(error):
    return {"message": "Not Found"}, 404

@app.errorhandler(500)
def internal_error(error):
    return {"message": "Internal Server Error"}, 500

if __name__ == '__main__':
    app.run(debug=app.config.get("DEBUG", False))  # Run with debug based on config
