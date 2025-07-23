import streamlit as st
import random
import time

st.set_page_config(page_title="취미 룰렛", page_icon="🎯", layout="centered")
st.title("🎯 오늘 뭐하지?")

st.markdown("룰렛을 돌려서 오늘의 취미를 정해보세요!")

# 취미 리스트
hobbies = [
    "책 읽기", "요리하기", "산책하기", "그림 그리기", "보드게임",
    "자전거 타기", "영화 보기", "사진 찍기", "헬스장 가기", "뜨개질",
    "코딩 공부", "춤 추기", "음악 듣기", "악기 연주", "명상하기",
    "캠핑 가기", "낚시하기", "조깅하기", "클라이밍", "도예 체험",
    "플라워 클래스", "홈카페 만들기", "수영 배우기", "웹툰 그리기", "퍼즐 맞추기"
]

# 속도 조절 슬라이더
speed = st.slider("룰렛 속도 설정", min_value=1, max_value=10, value=5)
base_delay = 0.03 + (10 - speed) * 0.01  # 속도가 클수록 빠르게

# 룰렛 돌리기 버튼
if st.button("룰렛 돌리기! 🎲"):
    placeholder = st.empty()

    with st.spinner("룰렛을 돌리는 중..."):
        for i in range(30):
            choice = random.choice(hobbies)
            placeholder.markdown(
                f"<div style='text-align:center; font-size:36px;'>{choice}</div>",
                unsafe_allow_html=True
            )
            time.sleep(base_delay + i * 0.005)

    st.success(f"✨ 오늘의 추천 취미는 **{choice}** 입니다!")
