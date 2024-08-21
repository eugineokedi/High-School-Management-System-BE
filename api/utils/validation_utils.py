import re

def is_valid_email(email):
    """Check if the email is in a valid format."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def is_unique_username(username, UserModel):
    """Check if the username is unique in the database."""
    return UserModel.query.filter_by(username=username).first() is None
