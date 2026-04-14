import streamlit as st

txt=st.text_input("please enter any text")

if txt.strip()=="":
    st.warning("Please write something ")
else:
    st.title(txt)
    st.divider()

    st.header(txt)
    st.divider()

    st.subheader(txt)
    st.divider()

    st.text(txt)
    st.divider()


