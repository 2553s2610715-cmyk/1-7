import streamlit as st
import pandas as pd
import json
import os
from collections import Counter

st.set_page_config(
    page_title="우리 반 취향 연결 지도",
    page_icon="🌱",
    layout="wide"
)

DATA_FILE = "preferences.json"


def load_data():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return []
    except Exception:
        return []


def save_data(data):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False


def similarity(user1, user2):
    score = 0

    keys = ["music", "game", "food", "activity"]

    for key in keys:
        if user1.get(key) == user2.get(key):
            score += 1

    return score


st.title("🌱 우리 반 취향 연결 지도")
st.caption("공통 관심사를 발견하고 새로운 친구와 대화를 시작해 보세요.")

data = load_data()

tab1, tab2, tab3 = st.tabs(
    ["📝 취향 등록", "🔍 비슷한 친구 찾기", "📊 우리 반 취향 보기"]
)

# --------------------
# 취향 등록
# --------------------
with tab1:

    st.subheader("취향 등록")

    with st.form("survey_form"):

        nickname = st.text_input(
            "닉네임",
            max_chars=20,
            placeholder="예: 별빛고양이"
        )

        music = st.selectbox(
            "좋아하는 음악",
            [
                "K-POP",
                "발라드",
                "힙합",
                "록",
                "클래식",
                "애니송",
                "기타"
            ]
        )

        game = st.selectbox(
            "좋아하는 게임/취미",
            [
                "게임",
                "독서",
                "그림",
                "운동",
                "영상시청",
                "음악감상",
                "기타"
            ]
        )

        food = st.selectbox(
            "좋아하는 음식",
            [
                "치킨",
                "피자",
                "떡볶이",
                "햄버거",
                "라면",
                "초밥",
                "기타"
            ]
        )

        activity = st.selectbox(
            "쉬는 시간에 하고 싶은 것",
            [
                "대화",
                "산책",
                "보드게임",
                "운동",
                "혼자 쉬기",
                "독서"
            ]
        )

        submitted = st.form_submit_button("저장하기")

        if submitted:

            if not nickname.strip():
                st.error("닉네임을 입력해주세요.")
            else:

                exists = False

                for person in data:
                    if person["nickname"] == nickname:
                        person["music"] = music
                        person["game"] = game
                        person["food"] = food
                        person["activity"] = activity
                        exists = True
                        break

                if not exists:
                    data.append(
                        {
                            "nickname": nickname,
                            "music": music,
                            "game": game,
                            "food": food,
                            "activity": activity
                        }
                    )

                if save_data(data):
                    st.success("취향이 저장되었습니다.")
                else:
                    st.error("저장 중 오류가 발생했습니다.")


# --------------------
# 비슷한 친구 찾기
# --------------------
with tab2:

    st.subheader("비슷한 취향의 친구 찾기")

    if len(data) < 2:
        st.info("최소 2명 이상의 데이터가 필요합니다.")
    else:

        names = [x["nickname"] for x in data]

        selected_name = st.selectbox(
            "내 닉네임 선택",
            names
        )

        me = None

        for p in data:
            if p["nickname"] == selected_name:
                me = p
                break

        results = []

        for p in data:

            if p["nickname"] == selected_name:
                continue

            score = similarity(me, p)

            results.append(
                {
                    "친구": p["nickname"],
                    "취향 일치 수": score
                }
            )

        results = sorted(
            results,
            key=lambda x: x["취향 일치 수"],
            reverse=True
        )

        if results:

            best = results[0]

            st.success(
                f"가장 비슷한 친구는 '{best['친구']}' 입니다! "
                f"(일치 {best['취향 일치 수']}개)"
            )

            st.dataframe(
                pd.DataFrame(results),
                use_container_width=True
            )


# --------------------
# 취향 통계
# --------------------
with tab3:

    st.subheader("우리 반 취향 통계")

    if not data:
        st.info("아직 등록된 데이터가 없습니다.")
    else:

        df = pd.DataFrame(data)

        col1, col2 = st.columns(2)

        with col1:
            st.write("### 음악 취향")
            music_count = df["music"].value_counts()
            st.bar_chart(music_count)

        with col2:
            st.write("### 음식 취향")
            food_count = df["food"].value_counts()
            st.bar_chart(food_count)

        st.divider()

        st.write("### 🌟 소수 취향 발견")

        categories = ["music", "game", "food", "activity"]

        rare_items = []

        for category in categories:

            counts = Counter(df[category])

            for item, count in counts.items():

                if count == 1:
                    owner = df[df[category] == item].iloc[0]["nickname"]

                    rare_items.append(
                        {
                            "분야": category,
                            "취향": item,
                            "학생": owner
                        }
                    )

        if rare_items:
            st.dataframe(
                pd.DataFrame(rare_items),
                use_container_width=True
            )

            st.info(
                "소수 취향은 이상한 것이 아니라 특별한 개성입니다. "
                "같은 취향을 가진 친구를 찾거나 관심을 가져보세요."
            )
        else:
            st.success("현재 모든 취향이 최소 2명 이상에게 공유되고 있습니다!")

        st.divider()

        st.write("### 등록 현황")
        st.dataframe(
            df,
            use_container_width=True
        )
