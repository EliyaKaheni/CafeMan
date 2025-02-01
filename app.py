import streamlit as st
from db import DatabaseManager

# Load external CSS
def load_css():
    css_file = open('styles/main_style.css').read()
    st.markdown(f"""
        <style>
            {css_file}
        </style>
    """, unsafe_allow_html=True)

# Function to toggle pages
def switch_page():
    if st.session_state.page == "signin":
        st.session_state.page = "signup"
    else:
        st.session_state.page = "signin"

# Login function
def login_check(username, password):
    db = DatabaseManager()
    if db.signin(username, password):
        st.success('در حال ورود به حساب ...')
    else:
        st.error('نام کاربری یا رمز عبور اشتباه است.')

def signup_user(username, password, confirm_password):
    if password == confirm_password:
        db = DatabaseManager()
        if not db.user_exist(username):
            if db.signup(username, password):
                st.success('ثبت نام با موفقیت انجام شد.')
            else:
                st.error('ثبت نام انجام نشد, لطفامجددا امتحان کنید.')
        else:
            st.error('این ایمیل قبلا استفاده شده است.')
    else:
        st.error('رمز عبور و تکرار آن تطابق ندارند.')

# Apply CSS
load_css()

# Initialize session state for page toggle
if "page" not in st.session_state:
    st.session_state.page = "signin"

# CSS Loading
st.markdown('<div class="container">', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="form-box">', unsafe_allow_html=True)

    # Signin section
    if st.session_state.page == "signin":
        st.title("ورود به حساب")
        email = st.text_input("ایمیل", key="email_signin")
        password = st.text_input("رمز عبور", type="password", key="password_signin")
        if st.button("ورود"):
            if login_check(email, password):
                pass

        if st.button("حساب کاربری ندارید؟"):
            switch_page()

    # Signup section
    else:
        st.title("ثبت نام")
        email = st.text_input("ایمیل", key="email_signup")
        password = st.text_input("رمز عبور", type="password", key="password_signup")
        confirm_password = st.text_input("تکرار رمز عبور", type="password", key="confirm_password_signup")
        
        if st.button("ثبت نام"):
            signup_user(email, password, confirm_password)


        if st.button("قبلا ثبت نام کرده‌اید؟"):
            switch_page()

    st.markdown('</div>', unsafe_allow_html=True)  

st.markdown('</div>', unsafe_allow_html=True) 
