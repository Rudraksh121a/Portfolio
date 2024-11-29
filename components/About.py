import streamlit as st
from  streamlit_lottie import  st_lottie
def about(selected,lottie_coder):
    if selected == 'About':
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.write("##")
                st.subheader("I am Rudraksh Kanungo")
                st.title("Data Scientist")
            with col2:
                st_lottie(lottie_coder)

        st.write("---")
        with st.container():
            col3, col4 = st.columns(2)
            with col3:
                st.title("""
                Education
                - Rajiv Gandhi Proudyogiki Vishwavidyalaya
                    - Bachelor of Computer Science (Artificial Intelligence And Machine Learning)
                 - Central Board of Secondary Education
                    - X
                    - XII
                """)
            with col4:
                st.title("""
                Skills
                - Python
                - Web Scraping
                - Machine Learning
                - Deep Learning
                - NLP
                """)
