import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="취미 매칭 게시판",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 취미 매칭 게시판")
st.write("같은 취미를 가진 사람들을 찾아보세요!")

# 데이터 저장
if "users" not in st.session_state:
    st.session_state.users = []

hobbies = [
    "게임",
    "독서",
    "운동",
    "음악 감상",
    "영화 보기",
    "그림 그리기",
    "요리",
    "사진 촬영",
    "코딩",
    "기타"
]

with st.form("user_form"):
    name = st.text_input("이름")
    hobby = st.selectbox("취미 선택", hobbies)

    submitted = st.form_submit_button("등록하기")

    if submitted:
        try:
            name = name.strip()

            if not name:
                st.error("이름을 입력해주세요.")
            else:
                st.session_state.users.append(
                    {
                        "이름": name,
                        "취미": hobby
                    }
                )
                st.success("등록 완료!")
        except Exception:
            st.error("등록 중 오류가 발생했습니다.")

st.divider()

st.subheader("👥 등록된 사용자")

if st.session_state.users:
    df = pd.DataFrame(st.session_state.users)
    st.dataframe(df, use_container_width=True)

    st.divider()

    st.subheader("🤝 취미 매칭 결과")

    for user in st.session_state.users:
        matches = [
            person["이름"]
            for person in st.session_state.users
            if person["취미"] == user["취미"]
            and person["이름"] != user["이름"]
        ]

        if matches:
            st.success(
                f"{user['이름']} ({user['취미']}) → "
                + ", ".join(matches)
            )
        else:
            st.info(
                f"{user['이름']} ({user['취미']}) → 현재 매칭 없음"
            )

else:
    st.info("아직 등록된 사용자가 없습니다.")

st.divider()

if st.button("🗑️ 전체 초기화"):
    st.session_state.users = []
    st.success("데이터가 초기화되었습니다.")
    st.rerun()
