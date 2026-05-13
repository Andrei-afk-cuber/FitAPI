from email.message import EmailMessage
import smtplib
from pathlib import Path

from config import EmailConfig

class EmailSender:
    SERVER = 'smtp.mail.ru'
    PORT = 587
    FROM = EmailConfig.EMAIL_FROM
    PASSWORD = EmailConfig.EMAIL_PASSWORD

    @classmethod
    def _get_message_body(cls) -> str:
        file_path = Path(__file__).parent / 'data' / 'message_text.txt'

        with open(file_path, 'r', encoding='utf-8') as file:
            message = file.read()

        return message

    # method for create message obj
    @classmethod
    def _create_message(cls, receiver: str, subject: str = 'Test Email') -> EmailMessage:
        # create message obj
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = cls.FROM
        msg['To'] = receiver
        msg.set_content(cls._get_message_body())

        return msg

    # method for send message
    @classmethod
    def send_email(cls, receiver: str, subject: str):
        msg = cls._create_message(receiver, subject)

        try:
            with smtplib.SMTP(cls.SERVER, cls.PORT) as server:
                server.starttls()
                server.login(cls.FROM, cls.PASSWORD)
                server.send_message(msg)

            return True
        except Exception as e:
            print(f'Message sent failed with {e}')
            return False