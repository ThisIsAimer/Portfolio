import smtplib,ssl
import Important



def send_mail(message):
    host = "smtp.gmail.com"
    post = 465
    user_name = Important.get_mail()
    password = Important.get_pass()
    receiver = Important.get_mail()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, post, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)
