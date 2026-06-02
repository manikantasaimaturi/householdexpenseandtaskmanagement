from flask import Flask, render_template, jsonify
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flasgger import Swagger

from config.database import db
from routes.auth_routes import auth_bp
from routes.task_routes import task_bp
from routes.expense_routes import expense_bp

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///household.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'jwt-secret-key'

app.config['SWAGGER'] = {
    'title': 'Shared Household Operations API',
    'uiversion': 3,
    'description': 'Household Expense and Task Management System'
}

db.init_app(app)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

CORS(
    app,
    resources={
        r"/*": {"origins": "*"}
    }
)

swagger = Swagger(app)

app.register_blueprint(auth_bp)
app.register_blueprint(task_bp)
app.register_blueprint(expense_bp)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({
        "status": "running",
        "message": "Shared Household Management API Working"
    })

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({
        "message": "Token expired"
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        "message": "Invalid token"
    }), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        "message": "Authorization token required"
    }), 401

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )