import streamlit as st

st.set_page_config(
    page_title="진로 친구 찾기",
    page_icon="🤝",
    layout="centered"
)

st.title("🤝 진로 친구 찾기")
st.write("비슷한 진로를 가진 친구를 찾아보세요!")

# 세션 상태 초기화
if "students" not in st.session_state:
    st.session_state.students = []

careers = [
    "의사",
    "간호사",
    "교사",
    "프로그래머",
    "게임개발자",
    "디자이너",
    "요리사",
    "경찰",
    "소방관",
    "운동선수",
    "유튜버",
    "사업가",
    "기타"
]

career_groups = {
    "의사": "의료",
    "간호사": "의료",
    "교사": "교육",
    "프로그래머": "IT",
    "게임개발자": "IT",
    "디자이너": "예술",
    "요리사": "서비스",
    "경찰": "공공",
    "소방관": "공공",
    "운동선수": "체육",
    "유튜버": "미디어",
    "사업가": "경영",
    "기타": "기타"
}

st.header("학생 등록")

name = st.text_input("이름 입력")
career = st.selectbox("희망 진로 선택", careers)

if st.button("등록하기"):
    try:
        if not name.strip():
            st.warning("이름을 입력해주세요.")
        else:
            exists = any(
                student["name"] == name.strip()
                for student in st.session_state.students
            )

            if exists:
                st.warning("이미 등록된 이름입니다.")
            else:
                st.session_state.students.append({
                    "name": name.strip(),
                    "career": career
                })
                st.success("등록 완료!")
    except Exception as e:
        st.error(f"오류 발생: {e}")

st.divider()

st.header("친구 추천")

if st.session_state.students:

    student_names = [
        student["name"]
        for student in st.session_state.students
    ]

    selected_name = st.selectbox(
        "내 이름 선택",
        student_names
    )

    if st.button("친구 찾기"):

        try:
            me = next(
                student
                for student in st.session_state.students
                if student["name"] == selected_name
            )

            same_career = [
                student
                for student in st.session_state.students
                if student["career"] == me["career"]
                and student["name"] != me["name"]
            ]

            if same_career:
                friend = same_career[0]

                st.success(
                    f"추천 친구: {friend['name']}"
                )

                st.write(
                    f"공통 진로 관심사: {friend['career']}"
                )

                st.info(
                    "대화 시작 질문:\n\n"
                    f"'{friend['career']}가 되고 싶은 이유는 뭐야?'"
                )

            else:
                my_group = career_groups.get(
                    me["career"],
                    "기타"
                )

                similar = [
                    student
                    for student in st.session_state.students
                    if career_groups.get(
                        student["career"],
                        "기타"
                    ) == my_group
                    and student["name"] != me["name"]
                ]

                if similar:
                    friend = similar[0]

                    st.success(
                        f"비슷한 분야 친구: {friend['name']}"
                    )

                    st.write(
                        f"{me['career']} ↔ {friend['career']}"
                    )

                    st.info(
                        "대화 시작 질문:\n\n"
                        "진로를 선택하게 된 계기가 있어?"
                    )

                else:
                    st.warning(
                        "현재 비슷한 진로 친구가 없습니다."
                    )

        except Exception as e:
            st.error(f"오류 발생: {e}")

else:
    st.info("먼저 학생을 등록해주세요.")

st.divider()

st.header("현재 등록된 학생")

if st.session_state.students:
    for student in st.session_state.students:
        st.write(
            f"👤 {student['name']} - {student['career']}"
        )
else:
    st.write("등록된 학생이 없습니다.")
