from src.main.routes.tag_routes import tags_routes_bp
from src.main.routes.product_routes import product_routes_bp
from flask import Flask

app = Flask(__name__)

app.register_blueprint(tags_routes_bp)
app.register_blueprint(product_routes_bp)
