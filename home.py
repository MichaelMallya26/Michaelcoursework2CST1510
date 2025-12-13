import pandas as pd
import streamlit as st
import numpy as np
from streamlit import session_state

from app.services.user_service import login_user, register_user
from pandas.core.methods.selectn import SelectNSeries
from app.data.users import get_role_by_username

st.title("Home")
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "users"not in st.session_state:
    st.session_state.users = []

st.set_page_config(
    page_title="Login page")
tab_login, tab_register = st.columns(2)
with tab_login:
    st.header("Login")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login"):
        success, msg = login_user(username, password)
        if success:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = get_role_by_username(username)
            st.success("Login successful!")
            st.switch_page("pages/incidents_dashboard.py")
        else:
            st.error(f"Login failed: {msg}")
with tab_register:
    if not session_state.logged_in:
        st.header("Register")
        new_username = st.text_input("New Username", key="register_username")
        new_password = st.text_input("New Password", type="password", key="register_password")
        role = st.selectbox("Role", ["user", "admin"], key="register_role")
        if st.button("Register"):
            success, msg = register_user(new_username, new_password, role)
            if success:
                st.success("Registration successful! You can now log in.")
                st.info("Please switch to the Login tab to log in.")
                st.rerun()
            else:
                st.error(f"Registration failed: {msg}")


if st.session_state.logged_in:
    df = pd.DataFrame({
    "User": ["Michael", "Laura", "Yvette"],
    "Math Score": [78, 67, 89]
     })
    st.dataframe(df)

    data = pd.DataFrame(
    np.random.randn(20,3),
        columns = ["michael", "laura", "yvette"]
    )
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.info("You have been logged out")












