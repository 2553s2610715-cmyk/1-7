import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="연애 코드 테스트",
    page_icon="💕",
    layout="centered"
)

# 제목
st.title("💕 연애 코드 테스트")
st.write("당신의 연애 스타일을 확인해보세요!")

# 사용자 입력
name = st.text_input("이름을 입력하세요")

# 질문
q1 = st.radio(
    "좋아하는 사람에게 먼저 연락하나요?",
    ["자주 한다", "가끔 한다", "잘 안 한다"]
)

q2 = st.radio(
    "데이트 스타일은?",
    ["로맨틱", "편안함", "재미"]
)

# 결과 버튼
if st.button("결과 보기"):
    
    results = [
        "당신은 다정한 연애 스타일 💖",
        "당신은 츤데레 연애 스타일 😎",
        "당신은 설레는 로맨티스트 🌹",
        "당신은 친구 같은 연애 스타일 😊"
    ]

    result = random.choice(results)

    st.success(f"{name}님의 연애 유형 결과!")
    st.subheader(result)

    # 점수 표시
    love_score = random.randint(70, 100)
    st.progress(love_score / 100)

    st.write(f"연애 매력 점수: {love_score}점 ❤️")
