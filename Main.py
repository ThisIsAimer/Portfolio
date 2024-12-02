import streamlit as web
import pandas


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

description="""
below are Some of the apps that i have built or will build with python! please feel free to contact me:
"""
web.write(f"<b>{description}</b>",unsafe_allow_html=True)

column3 ,  column4 = web.columns(2)

data = pandas.read_csv("data.csv",sep=";")
print(data)

with column3:
    for index,row in data[:10].iterrows():
        web.header(row["title"])
with column4:
    for index,row in data[10:].iterrows():
        web.header(row["title"])