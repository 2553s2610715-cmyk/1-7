import streamlit as st
import random
import time

# -----------------------------------
# 페이지 설정
# -----------------------------------
st.set_page_config(
    page_title="전생 직업 감별기",
    page_icon="🔮",
    layout="centered"
)

# -----------------------------------
# 전생 데이터
# -----------------------------------
past_jobs = [
    {
        "job": "왕국의 마법사 🧙",
        "desc": "당신은 사람들의 운명을 바꾸는 강력한 마법사였습니다.",
        "power": 95
    },
    {
        "job": "해적선 선장 ☠️",
        "desc": "바다를 지배하며 전설로 남은 인물이었습니다.",
        "power": 88
    },
    {
        "job": "닌자 암살자 🥷",
        "desc": "그 누구도 당신의 움직임을 눈치채지 못했습니다.",
        "power": 91
    },
    {
        "job": "우주 탐험가 🚀",
        "desc": "지구 밖 미지의 세계를 탐험하던 모험가였습니다.",
        "power": 84
    },
    {
        "job": "용을 길들이는 기사 🐉",
        "desc": "드래곤과 함께 전장을 누비던 전설의 기사였습니다.",
        "power": 97
    },
    {
        "job": "치킨집 사장 🍗",
        "desc": "동네 사람 모두가 인정한 전설의 맛집 주인이었습니다.",
        "power": 100
    }
]

# -----------------------------------
# 제목
# -----------------------------------
st.title("🔮 AI 전생 직업 감별기")
st.write("당신의 이름을 입력하면 전생 직업을 분석합니다.")

st.divider()

# -----------------------------------
# 입력
# -----------------------------------
name = st.text_input("이름 입력")

birth_month = st.selectbox(
    "태어난 월",
    list(range(1, 13))
)

personality = st.radio(
    "성격 선택",
    ["활발함", "조용함", "웃김", "진지함"]
)

st.divider()

# -----------------------------------
# 버튼
# -----------------------------------
if st.button("전생 분석 시작 🚀"):

    if name.strip() == "":
        st.error("이름을 입력해주세요!")
    else:

        # 로딩 연출
        with st.spinner("AI가 전생 기록을 탐색 중입니다..."):
            time.sleep(2)

        result = random.choice(past_jobs)

        st.success(f"{name}님의 전생 분석 완료!")

        st.markdown(f"# {result['job']}")
        st.write(result["desc"])

        st.subheader("⚡ 전설 능력치")
        st.progress(result["power"] / 100)
        st.write(f"능력치: {result['power']}점")

        # 전생 특징
        features = [
            "말빨이 엄청났음 🗣️",
            "숨만 쉬어도 인기 많았음 😎",
            "돈 냄새를 기가 막히게 맡음 💰",
            "운이 비정상적으로 좋았음 🍀",
            "먹을 거 앞에서 진심이었음 🍜"
        ]

        st.subheader("📜 전생 특징")
        st.write(random.choice(features))

        # 오늘의 운세
        luck = random.randint(1, 100)

        st.subheader("🍀 오늘의 운세")
        st.write(f"오늘의 행운 수치: {luck}%")

        if luck >= 80:
            st.info("오늘은 뭘 해도 잘 풀리는 날입니다!")
        elif luck >= 50:
            st.info("무난하게 좋은 하루가 될 것 같네요.")
        else:
            st.info("집에서 쉬면서 에너지 충전 추천 😴")

        st.balloons()
