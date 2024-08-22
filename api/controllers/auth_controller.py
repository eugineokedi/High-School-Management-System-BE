 # Handles authentication logic (login, signup, password reset)
from flask import Blueprint, request, jsonify, jsonify, url_for
from app import bcrypt
from flask_mail import Message, mail
from models import User, Student, Parent, Teacher, RoleEnum, db
from datetime import datetime, timezone, timedelta
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity,  decode_token


auth_bp = Blueprint('auth_bp', __name__)

#---SIGNUPS---

# Sign up for student
@auth_bp.route('/student_signup', methods=['POST'])
def signup():
  data = request.get_json()

  # Validate input data
  if not all(key in data for key in('first_name', 'last_name', 'admission_number', 'gender', 'grade_level')):
    return jsonify({"error": "Missing required fields"}), 400
  
  # Check if admission number already exists
  if Student.query.filter_by(admission_number=data['admission_number']).first():
    return jsonify({"error": "Admission number already exists"}), 409
  
  try:
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(
      email = None,
      password_hash = hashed_password,
      created_at=datetime.now(timezone.utc),
      role=RoleEnum.student
    )
    db.session.add(new_user)
    db.session.flush()

    new_student = Student(
      first_name = data['first_name'],
      last_name = data['last_name'],
      admission_number = data['admission_number'],
      date_of_birth = data['date_of_birth'],
      gender = data['gender'],
      grade_level = data['grade_level'],
      enrollment_date = datetime.now(timezone.utc),
      user_id = new_user.id
    )
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"message": "Student registered successfully", "student_id": new_student.id}), 201
  
  except Exception as e:
    db.session.rollback()
    return jsonify({"error": str(e)}), 500
  

# Signup for teacher
@auth_bp.route('/signup_teacher', methods=['POST'])
def signup_teacher():
  data = request.get_json()

  # Validate input data
  if not all(key in data for key in('name', 'email', 'subject', 'hire_date', 'qualification', 'password')):
    return jsonify({"error": "Missing required fields"}), 400
  
  # Check if email already exists
  if User.query.filter_by(email=data['email']).first():
    return jsonify({"error": "Email already exists"}), 409
  
  try:
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(
      email = data['email'],
      password_hash = hashed_password,
      created_at=datetime.now(timezone.utc),
      role=RoleEnum.teacher
    )
    db.session.add(new_user)
    db.session.flush()

    new_teacher = Teacher(
      name = data['name'],
      subject = data['subject'],
      hire_date=datetime.now(timezone.utc),
      qualification = data['qualification'],
      user_id = new_user.id
    )
    db.session.add(new_teacher)
    db.session.commit()

    return jsonify({"message": "Teacher registered successfully", "teacher_id": new_teacher.id}), 201
  
  except Exception as e:
    db.session.rollback()
    return jsonify({"error": str(e)}), 500


# Signup for parent
@auth_bp.route('/parent_signup', methods=['POST'])
def signup_parent():
  data = request.get_json()

  # Validate input data
  if not all(key in data for key in('name', 'email', 'contact_number', 'address', 'password')):
    return jsonify({"error": "Missing required fields"}), 400
  
  # Check if email already exists
  if User.query.filter_by(email=data['email']).first():
    return jsonify({"error": "Email already exists"}),409
  
  try:
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(
      email = data['email'],
      password_hash = hashed_password,
      created_at=datetime.now(timezone.utc),
      role=RoleEnum.parent
    )
    db.session.add(new_user)
    db.session.flush()

    new_parent = Parent(
      name = data['name'],
      contact_number = data['contact_number'],
      address = data['address'],
      user_id = new_user.id
    )
    db.session.add(new_parent)
    db.session.commit()

    return jsonify({"message": "Parent registered successfully", "parent_id": new_parent.id}), 201
  
  except Exception as e:
    db.session.rollback()
    return jsonify({"error": str(e)}), 500
  
# --- LOGIN ROUTES ---

# Login for Student
@auth_bp.route('/student_login', methods=['POST'])
def login_student():
  data = request.get_json()

  # Validate input data
  if not all(key in data for key in ('admission_number', 'password')):
    return jsonify({"error": "Missing required credentials"}), 400
  
  student = Student.query.filter_by(admission_number=data['admission_number']).first()
  if not student:
    return jsonify({"error": "Invalid admission number"}), 401
  
  user = User.query.get(student.user_id)
  if not bcrypt.check_password_hash(user.password_hash, data['password']):
    return jsonify({"error": "Invalid password"}), 401
  
  # Generate JWT with the user's ID and role
  access_token = create_access_token(identity={"user_id": user.id, "role": user.role.value})
  
  # Placeholder token, replace with JWT or other token-based auth
  return jsonify({"message": "Login successful", "token": access_token, "role": user.role.value}), 200

# Login for Teacher/Parent (Email)
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not all(key in data for key in ('email', 'password')):
        return jsonify({"error": "Missing required fields"}), 400

    user = User.query.filter_by(email=data['email']).first()
    if not user or not bcrypt.check_password_hash(user.password_hash, data['password']):
        return jsonify({"error": "Invalid email or password"}), 401
    
    # Generate JWT with the user's ID and role
    access_token = create_access_token(identity={"user_id": user.id, "role": user.role.value})

    # Placeholder token, replace with JWT or other token-based auth
    return jsonify({"message": "Login successful", "token": access_token, "role": user.role.value}), 200

# --- PROTECTED ROUTE ---
@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # Get the current user's identity from the token
    current_user = get_jwt_identity()

    return jsonify({"message": "Access granted", "user_id": current_user["user_id"], "role": current_user["role"]}), 200

# --- FORGOT PASSWORD ---
# Request Password Reset
@auth_bp.route('/forgot-password', methods=['POST'])
def forgot_password():
  data = request.get_json()

  # Validate email
  if 'email' not in data:
     return jsonify({"error": "Email is required"}), 400
  
  # Check if email exists in the database
  user = User.query.filter_by(email=data['email']).first()
  if not user:
      return jsonify({"error": "No account with that email exists."}), 404
  
  # Generate a reset token
  reset_token = create_access_token(identity={"user_id": user.id}, expires_delta=timedelta(hours=1))

  # Build the reset URL with the token
  reset_url = url_for('auth.reset_password', token=reset_token, _external=True)

  # Send the reset email
  msg = Message('Password Reset Request', recipients=[user.email])
  msg.body = f'Please click the link to reset your password: {reset_url}'
  mail.send(msg)

  return jsonify({"message": "Password reset email sent"}), 200

# Password Reset Form (protected by token)
@auth_bp.route('/reset_password/<token>', methods=['POST'])
def reset_password(token):
  data = request.get_json()

  # Validate new password
  if 'password' not in data:
     return jsonify({"error": "Password is required"}), 400
  
  try:
    # Decode the reset token
    decoded_token = decode_token(token)
    user_id = decoded_token['sub']['user_id']

    # Find the user
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "Invalid token or user not found."}), 404
    
    # Hash the new password and update the user record
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user.password_hash = hashed_password
    db.session.commit()

    return jsonify({"message": "Password updated successfully."}), 200
  
  except Exception as e:
        return jsonify({"error": "Invalid or expired token"}), 401
