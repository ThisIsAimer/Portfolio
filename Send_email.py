import smtplib,ssl


host ="smtp.gmail.com"

post = 465

user_name = "XXX@gmail.com"
password = "XXXXXXXXXXXXXXXX"

receiver = "XXXX@gmail.com"

text = """\
subject: hi 
how are you
bye
"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, post, context=context) as server:
    server.login(user_name,password)
    server.sendmail(user_name, receiver, text)