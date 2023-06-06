import streamlit as st
st.title("My Website")
st.header("Welcome to my website!")
st.subheader("This is a subheader")
st.text("This is some text")
age = st.slider("What is your age?", 0, 100, 25)
st.write("Your age is ", age, ".")
