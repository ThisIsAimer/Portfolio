import streamlit as web


web.set_page_config()
web.title("Contact me here:")

with web.form(key="email_form",clear_on_submit=True):
    user_email = web.text_input("your email address")
    message = web.text_area("please enter your message here")
    button = web.form_submit_button("submit")