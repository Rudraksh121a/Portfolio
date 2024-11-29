import streamlit as st
from streamlit_lottie import st_lottie
def contact(selected,lottie_contact):
    if selected == 'Contact':
        st.header("Get in touch!")
        st.write("##")
        st.write("##")
        contact_form = """
        <form action="https://formsubmit.co/Rudrakshkanungo2024@gmail.com" method="POST">
         <input type="text" name="name" required>
         <input type="email" name="email" required>
         <button type="submit">Send</button>
    </form>
        """
        left_col, right_col = st.columns((2, 1))
        with left_col:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_col:
            st_lottie(lottie_contact, height=300)