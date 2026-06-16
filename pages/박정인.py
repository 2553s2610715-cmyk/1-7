import streamlit as st
import google.generativeai as genai

# 페이지 설정
st.set_page_config(
    page_title="AI 진로 상담소",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 AI 진로 상담소")
st.write("진로, 전공, 취업, 직무 선택에 대해 자유롭게 질문해보세요.")

# API 키 확인
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    api_key = None

if not api_key:
    st.error("GEMINI_API_KEY가 설정되지 않았습니다.")
    st.stop()

# Gemini 설정
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash-lite")
except Exception as e:
    st.error(f"AI 모델 초기화 오류: {e}")
    st.stop()

# 세션 상태
if "history" not in st.session_state:
    st.session_state.history = []

# 예시 질문
with st.expander("💡 예시 질문 보기"):
    st.markdown("""
    - 컴퓨터공학과에 가면 어떤 직업을 가질 수 있나요?
    - 저는 사람들과 대화하는 것을 좋아하는데 어떤 직업이 맞을까요?
    - AI 분야로 취업하려면 무엇을 공부해야 하나요?
    - 문과 학생도 데이터 분석가가 될 수 있나요?
    - 진로를 아직 정하지 못했는데 어떻게 시작해야 할까요?
    """)

question = st.text_area(
    "질문을 입력하세요",
    height=120,
    placeholder="예: 저는 수학을 좋아하는 고등학생인데 어떤 진로가 잘 맞을까요?"
)

if st.button("질문하기", type="primary"):

    if not question.strip():
        st.warning("질문을 입력해주세요.")
    else:
        with st.spinner("진로 상담 중..."):

            prompt = f"""
당신은 친절한 진로 상담 전문가입니다.

사용자의 질문에 대해:
1. 이해하기 쉽게 설명
2. 적합한 직업 또는 진로 방향 제안
3. 필요한 공부나 준비 방법 제시
4. 장단점도 함께 설명

질문:
{question}
"""

            try:
                response = model.generate_content(prompt)

                answer = response.text

                st.session_state.history.insert(
                    0,
                    {
                        "question": question,
                        "answer": answer
                    }
                )

                st.success("답변이 생성되었습니다.")

            except Exception as e:
                st.error(
                    f"AI 응답 생성 중 오류가 발생했습니다.\n\n오류 내용: {e}"
                )

# 최근 답변
if st.session_state.history:

    st.divider()
    st.subheader("📌 상담 기록")

    for idx, item in enumerate(st.session_state.history, start=1):
        with st.expander(f"상담 {idx}"):
            st.markdown("**질문**")
            st.write(item["question"])

            st.markdown("**답변**")
            st.write(item["answer"])
