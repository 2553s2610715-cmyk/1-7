import streamlit as st

st.set_page_config(
    page_title="우리반 친구 매칭",
    page_icon="🤝",
    layout="centered"
)

st.title("🤝 우리반 친구 매칭")
st.write("성격과 취미를 선택하면 잘 맞는 친구 유형을 추천해드립니다!")

# 성격 데이터
friend_data = {
    "외향적": {
        "match": "활발하고 긍정적인 친구",
        "tip": "점심시간에 함께 놀자고 먼저 말해보세요."
    },
    "내향적": {
        "match": "차분하고 배려심 많은 친구",
        "tip": "공통 관심사 이야기를 천천히 시작해보세요."
    },
    "리더형": {
        "match": "협동을 잘하는 친구",
        "tip": "모둠 활동에서 함께 역할을 나눠보세요."
    },
    "배려형": {
        "match": "친절하고 공감 능력이 높은 친구",
        "tip": "상대방 이야기를 잘 들어주면 가까워질 수 있어요."
    }
}

try:
    name = st.text_input("이름을 입력하세요")

    personality = st.selectbox(
        "성격을 선택하세요",
        ["외향적", "내향적", "리더형", "배려형"]
    )

    hobby = st.selectbox(
        "좋아하는 취미를 선택하세요",
        ["운동", "게임", "독서", "음악", "그림", "영화"]
    )

    style = st.radio(
        "친구를 사귈 때 나는?",
        [
            "먼저 다가간다",
            "상대가 다가오길 기다린다",
            "공통 관심사가 있으면 말한다"
        ]
    )

    if st.button("🔍 친구 찾기"):

        result = friend_data[personality]

        st.success(f"{name}님과 잘 맞는 친구 유형")

        st.subheader("추천 친구")
        st.write(f"👉 {result['match']}")

        st.subheader("공통 취미 추천")
        st.write(f"👉 {hobby} 활동을 함께 하면 친해질 가능성이 높아요.")

        st.subheader("친구 사귀기 팁")
        st.info(result["tip"])

        if style == "상대가 다가오길 기다린다":
            st.warning(
                "가끔은 먼저 인사하는 작은 용기가 새로운 친구를 만들 수 있어요!"
            )

        st.balloons()

except Exception as e:
    st.error("오류가 발생했습니다.")
    st.error(str(e))
