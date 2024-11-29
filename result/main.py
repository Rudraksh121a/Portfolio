import streamlit as st
import pandas as pd
import requests
import json

st.title("SemAnalysis")

code = st.text_input("Enter your code", placeholder='0403')
branch = st.text_input("Enter your Branch", placeholder="AL")
year = st.text_input("Enter your Year", placeholder='22')
starting = st.text_input("Enter your starting number", placeholder='1001')
ending = st.text_input("Enter your ending number", placeholder='1020')
sem=st.selectbox(
    'sem',
    [str(i) for i in range(1,9)]
)


enrollment = code + branch + year


if st.button("Click Me"):

    try:
        starting = int(starting)
        ending = int(ending)


        for i in range(starting, ending + 1):
            get_res=enrollment + str(i)
            respond = requests.get(f'http://127.0.0.1:5000/get_input?enrollment={get_res}&sem={sem}')
            respond_res=respond.text
            data = json.loads(respond_res)
            result = {**data[0], **data[1], **data[2]}
            df=pd.DataFrame([result])
            


    except ValueError:
        st.error("Please enter valid numbers for starting and ending.")


