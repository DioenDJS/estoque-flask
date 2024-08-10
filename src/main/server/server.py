from src.main.routes.tag_routes import tags_routes_bp
from src.main.routes.product_routes import product_routes_bp
from src.main.routes.user_routes import user_routes_bp
from src.main.routes.employee_routes import employee_routes_bp
from src.main.routes.final_user_routes import final_users_routes_bp
from src.utils.schedule_handler import scheduling_excluding_records_deleted_thirty_days_ago
from datetime import timedelta
from src.auth.auth import auth_bp
from flask import Flask
from flask_jwt_extended import JWTManager
import os
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import croniter


app = Flask(__name__)


cron_expression = '* * * * * *'
scheduler = BackgroundScheduler()
scheduler.add_job(func=scheduling_excluding_records_deleted_thirty_days_ago, trigger='cron', second='*', args=[croniter.croniter(cron_expression)])
scheduler.start()


# Agendando a função de desligamento do agendador no encerramento do aplicativo
atexit.register(lambda: scheduler.shutdown())

app.config['JWT_SECRET_KEY'] = os.getenv("FLASK_JWT_SECRET_KEY")
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
jwt = JWTManager(app)


app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(tags_routes_bp)
app.register_blueprint(product_routes_bp)
app.register_blueprint(user_routes_bp)
app.register_blueprint(employee_routes_bp)
app.register_blueprint(final_users_routes_bp)

