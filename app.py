from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS

from config.database import db

from routes.auth_routes import auth_bp
from routes.task_routes import task_bp
from routes.expense_routes import expense_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///household.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'jwt-secret-key'

db.init_app(app)

bcrypt = Bcrypt(app)

jwt = JWTManager(app)

CORS(app)

app.register_blueprint(auth_bp)

app.register_blueprint(task_bp)

app.register_blueprint(expense_bp)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)