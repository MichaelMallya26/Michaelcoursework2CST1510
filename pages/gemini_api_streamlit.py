import streamlit as st
from google import genai


# Initialize client
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.title("Gemini API")
#if not logged in prevent usage
if st.session_state.logged_in:

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display past messages
    for message in st.session_state.messages:
        role = "assistant" if message["role"] == "model" else message["role"]
        with st.chat_message(role):
            st.markdown(message["parts"][0]["text"])

    # Chat input
    prompt = st.chat_input("Ask Something")

    if prompt:
        # Show user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Save user message
        st.session_state.messages.append({
            "role": "user",
            "parts": [{"text"  : prompt}]
        })

        # Stream response from Gemini
        response = client.models.generate_content_stream(
            model="gemini-2.5-flash",
            contents=st.session_state.messages,
        )

        with st.chat_message("assistant"):
            container = st.empty()
            full_reply = ""
            for chunk in response:
                if hasattr(chunk, "text"):
                    full_reply += chunk.text
                    container.markdown(full_reply)

        # Save assistant reply
        st.session_state.messages.append({
            "role": "model",
            "parts": [{"text": full_reply}]
        })
else:
    st.error("You need to login first")
    if st.button("Return to Login page"):
        st.switch_page("home.py")