
import streamlit as st

st.title("Even or Odd Number")

num = st.number_input(
    "Enter an integer",
    value=0,
    step=1
)

if st.button("Check"):
    if num % 2 == 0:
        st.success(f"{int(num)} is Even")
    else:
        st.success(f"{int(num)} is Odd")