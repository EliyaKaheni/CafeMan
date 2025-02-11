import hashlib
import streamlit as st
from db import DatabaseManager

# Hashing the passwords
def hash(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()

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
    if db.signin(username, hash(password)):
        st.success('در حال ورود به حساب ...')
        return True
    else:
        st.error('نام کاربری یا رمز عبور اشتباه است.')
        return False

# Signup function
def signup_user(username, password, confirm_password):
    if password == confirm_password:
        db = DatabaseManager()
        if not db.user_exist(username):
            if db.signup(username, hash(password)):
                st.success('ثبت نام با موفقیت انجام شد.')
                st.switch_page('pages/salesman.py')
            else:
                st.error('ثبت نام انجام نشد, لطفامجددا امتحان کنید.')
        else:
            st.error('این ایمیل قبلا استفاده شده است.')
    else:
        st.error('رمز عبور و تکرار آن تطابق ندارند.')
