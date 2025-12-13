import dateutil.utils
import streamlit as st
from streamlit import title

from app.data.db import connect_database
from app.data.incidents import get_all_incidents, insert_incident
from pathlib import Path
import datetime
conn = connect_database()

st.title("Incidents Dashboard")
if not st.session_state.logged_in:
    st.error("You need to login first to access this page.")
    if st.button("Return to the Login page"):
        st.switch_page("home.py")
        st.stop()
else:
    conn = connect_database()
    incidents = get_all_incidents(conn)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Incidents by severity")
        st.area_chart(incidents['severity'].value_counts())
    with col2:
        st.subheader("Incidents by type")
        st.bar_chart(incidents['incident_type'].value_counts())
    with col3:
        st.subheader("Incidents status")
        st.line_chart(incidents['status'].value_counts())
    incidents = get_all_incidents(conn)
    name = st.text_input("Enter your name")
    if st.button("Submit"):
        st.success(f"Hello {name}")

    incidents = get_all_incidents(conn)
    st.dataframe(incidents, use_container_width=True)

    with st.form("new_incident"):

        title= st.text_input("incident Title")
        severity = st.selectbox("severity", ["High", "Medium", "Low", "Critical"])
        status = st.selectbox("status", ["Open","In Progress" "Resolved"])
        description = st.text_area("Description")

        submitted = st.form_submit_button("Add incident")
        if submitted and title:
            insert_incident(conn,dateutil.utils.today(), title, severity,status,description, st.session_state.username)
            st.success("Incident successfully added")
            st.rerun()


