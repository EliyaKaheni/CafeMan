from utils import load_css, login_check, switch_page, signup_user
import streamlit as st

# Initial settings
st.set_page_config(page_title="کافی من", page_icon="☕️")
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
                st.switch_page('pages/salesman.py')

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
