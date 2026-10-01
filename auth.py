import streamlit as st

def check_login():
    """Verifies credentials against Streamlit Secrets securely."""
    try:
        correct_username = st.secrets["credentials"]["username"]
        correct_password = st.secrets["credentials"]["password"]
        
        if st.session_state.username == correct_username and st.session_state.password == correct_password:
            st.session_state.logged_in = True
            del st.session_state.username
            del st.session_state.password
        else:
            st.error("❌ Incorrect username or password")
    except KeyError:
        st.error("🔒 App Setup Incomplete: Secrets configuration is missing on the dashboard.")

def logout():
    """Logs out the user and clears the session."""
    st.session_state.logged_in = False
    st.rerun()

def show_login_page():
    """Renders the login screen. Returns True if logged in, False otherwise."""
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.title("🔒 Member Login")
        st.write("Please enter your credentials to access the application.")
        
        st.text_input("Username", key="username")
        st.text_input("Password", type="password", key="password")
        st.button("Log In", on_click=check_login, type="primary")
        return False
        
    # User is logged in, show a logout button in the sidebar
    st.sidebar.button("Log Out", on_click=logout)
    return True
