import streamlit as web
from Send_email import send_mail



web.set_page_config()
web.title("Contact me here:")

with web.form(key="email_form",clear_on_submit=True):
    user_email = web.text_input("your email address")
    raw_message = web.text_area("please enter your message here")
    message= f"""\
    subject: email from {user_email}
    from: {user_email}
    
    {raw_message}
"""
    button = web.form_submit_button("Send")

    if button:
        send_mail(message)
        web.info("your message has been sent!")