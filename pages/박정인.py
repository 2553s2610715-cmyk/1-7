import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI 진로 상담소", page_icon="🎯")

st.title("🎯 AI 진로 상담소")
st.write("진로 고민을 입력하면 AI가 방향을 추천해줍니다.")

# API KEY
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except:
    st.error("GEMINI_API_KEY가 설정되지 않았습니다.")
    st.stop()

# Gemini 설정
genai.configure(api_key=api_key)

# ✅ 안정 모델 (중요 수정)
model = genai.GenerativeModel("gemini-1.5-flash")

if "history" not in st.session_state:
    st.session_state.history = []

st.subheader("💬 질문 입력")

question = st.text_area("질문", placeholder="예: 컴공 vs 전기공학 고민입니다")

if st.button("질문하기"):

    if not question.strip():
        st.warning("질문을 입력하세요.")
    else:
        try:
            with st.spinner("AI가 분석 중..."):

                prompt = f"""
너는 진로 상담 전문가야.

사용자의 질문에 대해:
- 진로 방향 추천
- 이유 설명
- 필요한 준비

질문:
{question}
"""

                response = model.generate_content(prompt)
                answer = response.text

                st.session_state.history.insert(0, {
                    "q": question,
                    "a": answer
                })

                st.success("완료!")

        except Exception as e:
            st.error("AI 호출 실패")
            st.code(str(e))

# 기록
if st.session_state.history:
    st.divider()
    st.subheader("📌 기록")

    for i, item in enumerate(st.session_state.history):
        with st.expander(f"질문 {i+1}"):
            st.write("질문:", item["q"])
            st.write("답변:", item["a"])
