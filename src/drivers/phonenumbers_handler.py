from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
client = Client(os.getenv("ACCOUNT_SID"), os.getenv("AUTH_TOKEN"))


class PhonenumbersHandler:

    def generate_and_send_sms(self, smartphone: str, code: str):
        try:
            if smartphone:
                formatted_phone_number=f"+55{smartphone}"
                client.messages.create(
                    body=f"seu codigo de verificação: {code}",
                    from_=os.getenv("TWILIO_PHONE_NUMBER"),
                    to=formatted_phone_number
                )
            else:
                print("User not found")
        except Exception as e:
            print(f"falha no envio do SMS: {e}")
