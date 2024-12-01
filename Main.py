import streamlit as web


web.set_page_config(layout="wide")
column1, column2 = web.columns(2)

with column1:
    web.image("images\gitProfile.jpg",width=600)

with column2:
    web.title("Raunak Biswas")
    about_me = """
    Hello this is Raunak! I am a python programmer, a student who is hardworking and ambitious. I completed by school in the year 2023.
    I wanna become a great developer and take part in many projects and help make an impact in the world as we know it. 
    """
    web.info(about_me)