import  streamlit as st
def project(selected,image,linkdin,github):
    if selected == 'Project':
        with st.container():
            st.header("My Projects")
            st.write("##")
            col5, col6,col7 = st.columns(3)
            with col5:
                st.image(image)
                st.subheader("Project Title")
                linkdin,github=st.columns(2)
                with linkdin:
                    st.button("Linkdin")
                with github:
                    st.button("Github")