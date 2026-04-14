import streamlit as st
#take the numbers
number1=st.number_input("please enter first number")
number2=st.number_input("please enter second number")

#slect option
operator=st.selectbox("please select one",
                             options=["+","-","*","/"])

if st.button("caculate"):
    if operator=="+":
        result=number1 + number2
    elif operator=="-":
        result=number1 - number2
    elif operator=="*":
        result=number1 * number2
    elif operator=="/":
        if number2!=0:
            result=number1 / number2    
        else:
            result="cannot divide sorry"
    st.success(f"result :{result}")
    #sob condition check korei final
    #result ta show korbe