import streamlit as st 

st.set_page_config(page_title="Portfolio",page_icon="😜",layout="wide")

st.title("Abhishek Chilakalapalli",anchor=False)

st.subheader("Web Developer", anchor=False)

with st.container( border=True):
    st.info("I am Abhishek,currenty pursuing B.Tech in Vishnu Institute Of Technology under the stream CSE")
    
col1,col2,col3=st.columns(3)
with col1:
    st.image("per.png", width=300)
    
    
with col2:
       with st.expander(label="skills",expanded=False,icon="😎"):
        st.info("Html")
with col3:
    st.header("Contact")
    
