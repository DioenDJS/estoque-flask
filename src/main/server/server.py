from src.main.routes.tag_routes import tags_routes_bp
from src.main.routes.product_routes import product_routes_bp
from src.main.routes.user_routes import user_routes_bp
from src.main.routes.employee_routes import employee_routes_bp
from src.main.routes.login_routes import login_route
from flask import Flask
from flask_jwt_extended import JWTManager, jwt_required
from dotenv import load_dotenv

import os

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.getenv("FLASK_SECRET_KEY")
jwt = JWTManager(app)

app.register_blueprint(login_route)
# app.register_blueprint(login_route)
app.register_blueprint(tags_routes_bp)
app.register_blueprint(product_routes_bp)
app.register_blueprint(user_routes_bp)
app.register_blueprint(employee_routes_bp)



