import smtplib,ssl


def send_mail(message):
    host = "smtp.gmail.com"
    post = 465
    user_name = "XXXXXX@gmail.com"
    password = "XXXXXXXXX"
    receiver = "XXXXXXXXXX@gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, post, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)