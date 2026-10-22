
import streamlit as st

st.title("Student Result Calculator")

name = st.text_input("Enter Student Name")

m1 = st.number_input("Enter Subject 1 Marks", min_value=0, max_value=100)
m2 = st.number_input("Enter Subject 2 Marks", min_value=0, max_value=100)
m3 = st.number_input("Enter Subject 3 Marks", min_value=0, max_value=100)

if st.button("Calculate Result"):
    if name.strip() == "":
        st.warning("Please enter student name")
    else:
        total = m1 + m2 + m3
        percentage = total / 3

        st.write("Student Name:", name)
        st.write("Total Marks:", total, "/ 300")
        st.write(f"Percentage: {percentage:.2f}%")

        if m1 >= 40 and m2 >= 40 and m3 >= 40:
            st.success("Result: PASS")
        else:
            st.error("Result: FAIL")