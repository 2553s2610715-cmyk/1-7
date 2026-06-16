import streamlit as st
import google.generativeai as genai

st.title("🎯 진로 상담")

api_key = st.secrets.get("GEMINI_API_KEY", None)

if not api_key:
    st.error("Secrets에 GEMINI_API_KEY 없음")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

q = st.text_input("질문")

if st.button("질문"):
    try:
        r = model.generate_content(q)
        st.write(r.text)
    except Exception as e:
        st.error("오류 발생")
        st.code(str(e))
