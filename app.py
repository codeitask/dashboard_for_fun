import streamlit as st
from auth import show_login_page

if show_login_page():

    st.title("Welcome To Dashboard")
    st.write("All contents will be shown here after login...")
    
