import streamlit as st

st.title("🎯 진로 추천기")

job = st.selectbox(
    "관심 분야를 선택하세요",
    ["프로그래밍", "디자인", "마케팅", "과학"]
)

if st.button("추천받기"):
    if job == "프로그래밍":
        st.success("추천 직업: 개발자, AI 엔지니어")
    elif job == "디자인":
        st.success("추천 직업: UI/UX 디자이너")
    elif job == "마케팅":
        st.success("추천 직업: 마케터")
    else:
        st.success("추천 직업: 연구원, 과학자")
