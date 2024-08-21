from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    """Hash a plaintext password using bcrypt."""
    return generate_password_hash(password)

def verify_password(password, hashed_password):
    """Verify a plaintext password against a hashed password."""
    return check_password_hash(hashed_password, password)
