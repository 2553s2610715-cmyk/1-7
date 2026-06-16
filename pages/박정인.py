import streamlit as st

st.title("진로 알아보기")

career = st.text_input("당신의 진로는 무엇인가요?")

if career:
    st.write("입력한 진로:", career)
