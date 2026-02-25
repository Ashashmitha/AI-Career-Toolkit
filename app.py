import streamlit as st

st.set_page_config(page_title="AI Career Toolkit", layout="centered")

st.title("🚀 AI Career Toolkit")

option = st.sidebar.selectbox(
    "Choose a Tool",
    ["Resume Builder", "Cover Letter Generator", "Portfolio Builder"]
)

if option == "Resume Builder":
    import resume

elif option == "Cover Letter Generator":
    import cover_letter

elif option == "Portfolio Builder":
    import portfolio