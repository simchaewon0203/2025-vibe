import streamlit as st
import random
import time

st.set_page_config(page_title="취미 룰렛", page_icon="🎯", layout="centered")
st.title("🎯 오늘 뭐하지?")

st.markdown("룰렛을 돌려서 오늘의 취미를 정해보세요!")

# 취미별 이미지 매핑 (URL 또는 로컬 경로 가능)
hobby_images = {
    "책 읽기": "https://cdn.pixabay.com/photo/2016/11/29/05/10/adult-1867665_960_720.jpg",
    "요리하기": "https://cdn.pixabay.com/photo/2015/04/08/13/13/food-712665_960_720.jpg",
    "산책하기": "https://cdn.pixabay.com/photo/2020/10/19/17/13/walk-5667200_960_720.jpg",
    "그림 그리기": "https://cdn.pixabay.com/photo/2016/02/19/10/00/pencil-1209747_960_720.jpg",
    "보드게임": "https://cdn.pixabay.com/photo/2016/11/29/04/18/board-game-1867606_960_720.jpg",
    "자전거 타기": "https://cdn.pixabay.com/photo/2016/11/18/15/03/bicycle-1834265_960_720.jpg",
    "영화 보기": "https://cdn.pixabay.com/photo/2014/04/03/10/32/cinema-312320_960_720.png",
    "사진 찍기": "https://cdn.pixabay.com/photo/2016/11/29/05/08/camera-1867184_960_720.jpg",
    "헬스장 가기": "https://cdn.pixabay.com/photo/2016/11/29/06/15/sports-1867830_960_720.jpg",
    "뜨개질": "https://cdn.pixabay.com/photo/2016/11/29/12/40/yarn-1868496_960_720.jpg",
    "코딩 공부": "https://cdn.pixabay.com/photo/2014/12/27/15/40/code-581337_960_720.jpg",
    "춤 추기": "https://cdn.pixabay.com/photo/2016/11/22/22/18/dancer-1850147_960_720.jpg",
    "음악 듣기": "https://cdn.pixabay.com/photo/2016/11/29/06/15/headphones-1868612_960_720.jpg",
    "악기 연주": "https://cdn.pixabay.com/photo/2014/10/23/18/05/violin-500156_960_720.jpg",
    "명상하기": "https://cdn.pixabay.com/photo/2017/03/27/13/28/yoga-2176668_960_720.jpg",
    "캠핑 가기": "https://cdn.pixabay.com/photo/2016/11/29/09/16/camping-1868290_960_720.jpg",
    "낚시하기": "https://cdn.pixabay.com/photo/2015/03/26/09/54/fishing-690547_960_720.jpg",
    "조깅하기": "https://cdn.pixabay.com/photo/2015/01/15/12/46/jogging-600274_960_720.jpg",
    "클라이밍": "https://cdn.pixabay.com/photo/2016/11/29/07/20/rock-climbing-1868412_960_720.jpg",
    "도예 체험": "https://cdn.pixabay.com/photo/2014/09/14/18/16/clay-445872_960_720.jpg",
    "플라워 클래스": "https://cdn.pixabay.com/photo/2017/08/01/08/29/flowers-2569483_960_720.jpg",
    "홈카페 만들기": "https://cdn.pixabay.com/photo/2016/11/18/14/35/coffee-1835927_960_720.jpg",
    "수영 배우기": "https://cdn.pixabay.com/photo/2016/11/29/04/17/swimming-1867418_960_720.jpg",
    "웹툰 그리기": "https://cdn.pixabay.com/photo/2020/05/01/17/47/illustration-5118399_960_720.jpg",
    "퍼즐 맞추기": "https://cdn.pixabay.com/photo/2016/11/21/14/40/jigsaw-puzzle-1841190_960_720.jpg"
}

# 전체 취미 리스트
hobbies = list(hobby_images.keys())

# 속도 설정 슬라이더
speed = st.slider("룰렛 속도 설정", min_value=1, max_value=10, value=5, step=1)
base_delay = 0.03 + (10 - speed) * 0.01  # 속도 반비례 설정

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

    # 이미지 출력
    image_url = hobby_images.get(choice)
    if image_url:
        st.image(image_url, caption=f"{choice} 예시 이미지", use_column_width=True)
