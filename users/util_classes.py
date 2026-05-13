from email.message import EmailMessage
import smtplib
from pathlib import Path

from config import EmailConfig


# class for exception
class EmailSendError(Exception):
    pass


# email sender class
class EmailSender:
    SERVER = EmailConfig.EMAIL_SERVER
    PORT = EmailConfig.EMAIL_PORT
    FROM = EmailConfig.EMAIL_FROM
    PASSWORD = EmailConfig.EMAIL_PASSWORD

    @classmethod
    def _get_message_body(cls, first_name: str, last_name: str) -> str:
        file_path = Path(__file__).parent / "data" / "message_text.txt"

        with open(file_path, "r", encoding="utf-8") as file:
            message = file.read()
            message = message.replace("{first_name}", f"{first_name} {last_name}")
            message = message.replace("{app_name}", "Cyb Company")

        return message

    # method for create message obj
    @classmethod
    def _create_message(
        cls, receiver: str, first_name: str, last_name: str, subject: str
    ) -> EmailMessage:
        # create message obj
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = cls.FROM
        msg["To"] = receiver
        msg.set_content(cls._get_message_body(first_name, last_name))

        return msg

    # method for send message
    @classmethod
    def send_email(
        cls, receiver: str, first_name: str, last_name: str, subject: str = 'Hello, friend'
    ) -> bool:
        msg = cls._create_message(receiver, first_name, last_name, subject)

        try:
            with smtplib.SMTP(cls.SERVER, cls.PORT) as server:
                server.starttls()
                server.login(cls.FROM, cls.PASSWORD)
                server.send_message(msg)

            return True
        except smtplib.SMTPAuthenticationError as e:
            raise EmailSendError(f"SMTP Authentication Error: {e}")
        except smtplib.SMTPRecipientsRefused as e:
            raise EmailSendError(f"Invalid recipient email: {receiver} {e}")
        except Exception as e:
            raise EmailSendError(f"Failed to send email: {e}")
