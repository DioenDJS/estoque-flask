from src.main.routes.tag_routes import tags_routes_bp
from src.main.routes.product_routes import product_routes_bp
from src.main.routes.user_routes import user_routes_bp
from src.main.routes.employee_routes import employee_routes_bp
from datetime import timedelta
from src.auth.auth import auth_bp
from flask import Flask
from flask_jwt_extended import JWTManager

import os

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.getenv("FLASK_JWT_SECRET_KEY")
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(tags_routes_bp)
app.register_blueprint(product_routes_bp)
app.register_blueprint(user_routes_bp)
app.register_blueprint(employee_routes_bp)
