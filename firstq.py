import streamlit as st

st.title("Login page")
st.divider()
name=st.text_input("Enter your name :")
age=st.number_input("Enter your age :")
profession=st.selectbox("Enter your prifession",("Student","Employee","Businessman","Freelancer"),
                        index=None,accept_new_options=True) 
                        
if st.button("press the button"):
    if name.strip()=="" or age==0 or profession == "Select":
       st.warning("please fill the form")
    else:

      st.success("succesfully fill up")

      st.write(f"your name is {name},your age is {age},ypur prefession is {profession}")

