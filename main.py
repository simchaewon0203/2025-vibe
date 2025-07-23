import streamlit as st
import plotly.graph_objects as go
import random

st.set_page_config(page_title="룰렛 메뉴 추천", page_icon="🎡")

st.title("🎡 진짜 룰렛으로 메뉴를 골라보자!")
st.write("음식 종류를 선택한 뒤, 룰렛을 돌려 메뉴와 가격을 추천받으세요!")

# 기본 메뉴
default_menus = {
    "한식": [
        {"name": "김치찌개", "price": 9000},
        {"name": "된장찌개", "price": 8500},
        {"name": "불고기", "price": 12000},
        {"name": "삼겹살", "price": 15000},
        {"name": "비빔밥", "price": 9000},
        {"name": "갈비탕", "price": 11000}
    ],
    "중식": [
        {"name": "짜장면", "price": 7000},
        {"name": "짬뽕", "price": 8000},
        {"name": "탕수육", "price": 13000},
        {"name": "마파두부", "price": 9000},
        {"name": "고추잡채", "price": 11000}
    ],
    "일식": [
        {"name": "초밥", "price": 13000},
        {"name": "라멘", "price": 9500},
        {"name": "돈까스", "price": 10000},
        {"name": "우동", "price": 8500},
        {"name": "규동", "price": 9000}
    ],
    "양식": [
        {"name": "파스타", "price": 12000},
        {"name": "피자", "price": 15000},
        {"name": "햄버거", "price": 9000},
        {"name": "스테이크", "price": 20000},
        {"name": "리조또", "price": 13000}
    ]
}

# 상태 초기화
if "menus" not in st.session_state:
    st.session_state.menus = default_menus.copy()

# 카테고리 선택
category = st.radio("🍱 음식 종류 선택", list(st.session_state.menus.keys()))

menu_list = st.session_state.menus[category]

if menu_list:
    labels = [f"{m['name']} ({m['price']:,}원)" for m in menu_list]
    values = [1] * len(menu_list)

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.2,
        direction="clockwise",
        sort=False,
        textinfo='label',
    )])

    fig.update_layout(
        title=f"🎯 {category} 룰렛 돌리기",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

    if st.button("🎰 룰렛 돌리기!"):
        selected = random.choice(menu_list)
        st.success(f"✨ 오늘의 메뉴는 **{selected['name']}**!\n💸 평균 가격: **{selected['price']:,}원**")

else:
    st.warning("이 카테고리에 메뉴가 없습니다. 메뉴를 추가해주세요.")

# 메뉴 추가
with st.expander("➕ 메뉴 추가하기"):
    new_name = st.text_input("메뉴 이름", key="add_name")
    new_price = st.number_input("평균 가격 (원)", min_value=0, max_value=100000, step=500, key="add_price")
    if st.button("추가", key="add_btn"):
        if new_name:
            exists = any(m['name'] == new_name for m in menu_list)
            if not exists:
                st.session_state.menus[category].append({"name": new_name, "price": int(new_price)})
                st.success(f"{category}에 '{new_name}'이 추가되었습니다!")
            else:
                st.warning("이미 등록된 메뉴입니다.")
        else:
            st.error("메뉴 이름을 입력해주세요.")

# 현재 메뉴 리스트
with st.expander("📋 현재 메뉴 보기"):
    if menu_list:
        for m in menu_list:
            st.write(f"• {m['name']} - {m['price']:,}원")
    else:
        st.write("등록된 메뉴가 없습니다.")
