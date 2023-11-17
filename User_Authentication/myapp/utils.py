from django.core.mail import EmailMessage
import os


class Util:
    @staticmethod
    def sent_mail(data):
        email = EmailMessage(subject=data['subject'],
                             body=data['body'],
                             from_email="durairsdk@gmail.com",
                             to=data["to_email"])
        print("email Sended")
        email.send()
        # return email
