import random
import phonenumbers
from phonenumbers import PhoneNumberFormat
from twilio.rest import Client
from dotenv import load_dotenv
import os

client = Client(os.getenv("ACCOUNT_SID"), os.getenv("AUTH_TOKEN"))


class PhonenumbersHandler:


    def generate_and_send_sms(self, smartphone: str):

        if smartphone:
            # Generate a 4-digit code
            verification_code = str(random.randint(1000, 9999))

            # user.verification_code = verification_code

            user_phone_number = smartphone

            # Format the phone number using the phonenumbers library

            formatted_phone_number=f"+55{user_phone_number}"

            self.send_sms(formatted_phone_number, verification_code)
        else:
            print("User not found")

    def send_sms(self, phone_number: str, code: str):
        try:
            message = client.messages.create(
                body=f"seu codigo de verificação: {code}",
                from_=os.getenv("TWILIO_PHONE_NUMBER"),
                to=phone_number
            )
        except Exception as e:
            print(f"falha no envio do SMS: {e}")


