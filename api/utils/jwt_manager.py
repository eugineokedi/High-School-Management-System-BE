from flask_jwt_extended import create_access_token, decode_token
from datetime import timedelta

def generate_jwt_token(identity):
    """Generate a JWT token for the given identity (e.g., user ID)."""
    expires = timedelta(hours=1)  # Token expires in 1 hour
    token = create_access_token(identity=identity, expires_delta=expires)
    return token

def decode_jwt_token(token):
    """Decode a JWT token and return the identity."""
    decoded_token = decode_token(token)
    return decoded_token['sub']
