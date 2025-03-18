import re
import random
import string
import streamlit as st

st.title("PASSWORD STRENGTH METER 🔐")
st.write("🛡️ Test your password and enhance your security!")


def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=12))


COMMON_PASSWORDS = {"password", "123456", "password123", "qwerty", "admin", "welcome"}


def check_strength(password):
    score, feedback = 0, []
    if password.lower() in COMMON_PASSWORDS:
        return 0, ["❌ This password is too common. Choose a unique one!"]
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("⚠️ Password must be at least 8 characters long.")
    if any(letter.isupper() for letter in password) and any(letter.islower() for letter in password):
        score += 1
    else:
        feedback.append("Mix uppercase and lowercase letters for better security.")
    if any(digit.isdigit() for digit in password):
        score += 1
    else:
        feedback.append("Include at least one number.")
    if any(symbol in "!@#$%^&*" for symbol in password):
        score += 1
    else:
        feedback.append("Add a special character (!@#$%^&*) to increase strength.")
    return score, feedback

password = st.text_input("🔑 Enter your password", type="password")

if password:
    score, feedback = check_strength(password)
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider making it stronger!")
    else:
        st.error("❌ Weak Password")
        st.write("\n".join(["- " + msg for msg in feedback]))
        st.write("Suggested Secure Password:", generate_password())

if st.button("Generate Strong Password"):
    st.write("🔑 Suggested Password:", generate_password())
