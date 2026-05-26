import streamlit as st
import random

# -----------------------------
# 기본 설정
# -----------------------------
st.set_page_config(
    page_title="연애 코드 분석기",
    page_icon="💘",
    layout="centered"
)

# -----------------------------
# 데이터
# -----------------------------
love_types = {
    "직진형": {
        "emoji": "🔥",
        "desc": "좋아하면 숨기지 못하는 스타일. 표현력이 강하고 적극적입니다."
    },
    "츤데레형": {
        "emoji": "😎",
        "desc": "무심한 척하지만 사실 누구보다 상대를 많이 챙기는 스타일."
    },
    "감성형": {
        "emoji": "🌙",
        "desc": "분위기와 감정을 중요하게 생각하는 로맨티스트."
    },
    "안정형": {
        "emoji": "🫶",
        "desc": "편안하고 오래가는 연애를 추구하는 스타일."
    }
}

# -----------------------------
# 제목
# -----------------------------
st.title("💘 연애 코드 분석기")
st.caption("간단한 질문으로 알아보는 나의 연애 스타일")

st.divider()

# -----------------------------
# 입력
# -----------------------------
name = st.text_input("이름")

age = st.slider("나이", 15, 40, 20)

mbti = st.selectbox(
    "MBTI 선택",
    [
        "INTJ","INTP","ENTJ","ENTP",
        "INFJ","INFP","ENFJ","ENFP",
        "ISTJ","ISFJ","ESTJ","ESFJ",
        "ISTP","ISFP","ESTP","ESFP"
    ]
)

date_style = st.radio(
    "선호하는 데이트 스타일",
    ["카페", "드라이브", "집데이트", "여행"]
)

contact_style = st.radio(
    "연락 스타일",
    ["바로 답장", "천천히 답장", "생각날 때만"]
)

st.divider()

# -----------------------------
# 결과 생성 함수
# -----------------------------
def analyze_love_style(mbti, date_style, contact_style):
    
    if mbti.startswith("E"):
        return "직진형"
    
    if "F" in mbti:
        return "감성형"
    
    if contact_style == "천천히 답장":
        return "츤데레형"
    
    return "안정형"

# -----------------------------
# 버튼
# -----------------------------
if st.button("내 연애 코드 확인하기 💖"):

    if name.strip() == "":
        st.warning("이름을 입력해주세요!")
    else:
        
        result = analyze_love_style(
            mbti,
            date_style,
            contact_style
        )

        info = love_types[result]

        st.success(f"{name}님의 연애 코드 분석 완료!")

        st.markdown(f"# {info['emoji']} {result}")
        st.write(info["desc"])

        # 연애 매력 점수
        score = random.randint(72, 99)

        st.subheader("💯 연애 매력 점수")
        st.progress(score / 100)
        st.write(f"### {score}점")

        # 궁합 추천
        compatibility = random.choice([
            "ENFP ❤️",
            "INFJ 💕",
            "ESFP 💘",
            "INTJ 💓"
        ])

        st.subheader("💑 잘 맞는 타입")
        st.info(compatibility)

        # 한줄 조언
        tips = [
            "감정 표현을 조금 더 해보세요 😊",
            "연락 템포를 맞추면 관계가 오래갑니다 💌",
            "너무 분석하지 말고 마음을 믿어보세요 🌸",
            "가끔은 먼저 다가가는 용기도 필요해요 ✨"
        ]

        st.subheader("📌 연애 한줄 조언")
        st.write(random.choice(tips))

        st.balloons()
