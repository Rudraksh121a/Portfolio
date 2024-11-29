from streamlit import columns
from streamlit_option_menu import option_menu
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

from components.About import about
from components.Project import project
from components.contact import contact

st.set_page_config(layout="wide")
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def localcss(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()} </style>",unsafe_allow_html=True)
localcss("style/style.css")



# Set page layout


# Load Lottie animation
lottie_coder = load_lottie("https://lottie.host/aa8d0a04-3df8-4138-9b41-688dcb40879f/OmPo8mLA4Q.json")
lottie_contact=load_lottie(("https://lottie.host/b8aef14e-87f0-463a-9c84-f50b5f6f833c/iXS7QFew2w.json"))

# Open image
image = Image.open("./Image/123.png")  # Make sure the path is correct

# Page title and description
st.header("Rudraksh Portfolio")
st.write("""This is a content for the portfolio""")
st.write("---")

# Sidebar or horizontal menu options
with st.container():
    selected = option_menu(
        menu_title=None,
        options=["About", "Project", "Contact"],
        icons=['person', 'code-slash', 'chat-left-text-fill'],
        orientation='horizontal'
    )

# About section
about(selected,lottie_coder)
# Projects section
project(selected,image,linkdin="dkfdsf",github="fgkmdkg")
# Contact section
contact(selected,lottie_contact)




