from src.main.domain.models.models import Users, FinalUsersPhysicalPerson
from src.controllers.final_user.final_user_controller import FinalUserController
from src.database.database import get_connect
import os
from datetime import datetime, timedelta

# Defina o fuso horário desejado
os.environ['TZ'] = 'America/Sao_Paulo'
final_user_controller = FinalUserController()

def scheduling_excluding_records_deleted_thirty_days_ago(cron):
    print('Schedule triggered at:', datetime.now())
    db = get_connect()
    try:
        with db.atomic() as txn:
            current_time = datetime.now()

            users_to_delete = Users.select().where(
                (Users.deleted_at < current_time) &
                ((current_time - Users.deleted_at) > timedelta(days=30))
            )
            for user in users_to_delete:
                id = FinalUsersPhysicalPerson.get(user=user.id)
                final_user_controller.one_delete(id)

            txn.commit()
    except Exception as e:
        txn.rollback()
        print(e)
