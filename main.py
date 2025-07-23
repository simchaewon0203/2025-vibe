import streamlit as st
import random
import time

st.set_page_config(page_title="룰렛 메뉴 추천", page_icon="🎡")

st.title("🎡 오늘 저녁 뭐 먹지? 룰렛 돌리기!")
st.write("음식 종류를 선택한 후, 룰렛을 돌려 메뉴를 추천받으세요!")

# 기본 메뉴 (카테고리별, 평균 가격 포함)
default_menusdefault_menus = {
    "한식": [
        "김치찌개",
        "된장찌개",
        "불고기",
        "삼겹살",
        "비빔밥",
        "갈비탕",
        "제육볶음",
        "부대찌개",
        "순두부찌개",
        "닭갈비",
        "냉면",
        "오징어볶음"
    ],
    "중식": [
        "짜장면",
        "짬뽕",
        "탕수육",
        "마파두부",
        "고추잡채",
        "깐풍기",
        "유린기",
        "양장피",
        "멘보샤",
        "볶음밥",
        "칠리새우"
    ],
    "일식": [
        "초밥",
        "라멘",
        "돈까스",
        "우동",
        "규동",
        "가츠동",
        "연어덮밥",
        "텐동",
        "모밀",
        "나베",
        "사케동"
    ],
    "양식": [
        "파스타",
        "피자",
        "햄버거",
        "스테이크",
        "리조또",
        "라자냐",
        "크림스프",
        "그라탱",
        "바베큐립",
        "치킨텐더",
        "까르보나라",
        "명란파스타"
    ]
}

# 세션 상태 초기화
if "menus" not in st.session_state:
    st.session_state.menus = default_menus.copy()

# 카테고리 선택
category = st.radio("🍱 음식 종류 선택", list(st.session_state.menus.keys()))

# 룰렛 시뮬레이션
if st.button("🎰 룰렛 돌리기!"):
    menu_list = st.session_state.menus[category]

    if not menu_list:
        st.warning("해당 카테고리에 메뉴가 없습니다. 메뉴를 추가해주세요.")
    else:
        roulette_placeholder = st.empty()
        spin_times = random.randint(12, 20)  # 룰렛 회전 횟수

        for i in range(spin_times):
            selected = menu_list[i % len(menu_list)]
            roulette_placeholder.markdown(f"""
                <div style='text-align:center; font-size: 32px; padding: 20px; border: 3px dashed #f39c12; border-radius: 10px;'>
                    🎡 {selected['name']} <br/>💸 {selected['price']:,}원
                </div>
            """, unsafe_allow_html=True)
            time.sleep(0.9 + (i * 0.03))  # 점점 느려지는 효과

        st.success(f"✨ 최종 선택: **{selected['name']}** ({selected['price']:,}원)")

# 메뉴 추가
with st.expander("➕ 메뉴 추가하기"):
    new_menu_name = st.text_input("추가할 메뉴 이름", key="add_name")
    new_menu_price = st.number_input("평균 가격 (원)", min_value=0, max_value=100000, step=500, key="add_price")
    if st.button("추가", key="add_btn"):
        if new_menu_name:
            exists = any(menu['name'] == new_menu_name for menu in st.session_state.menus[category])
            if not exists:
                st.session_state.menus[category].append({
                    "name": new_menu_name,
                    "price": int(new_menu_price)
                })
                st.success(f"{category}에 '{new_menu_name}' 메뉴가 추가되었습니다!")
            else:
                st.warning("이미 등록된 메뉴입니다.")
        else:
            st.error("메뉴 이름을 입력해주세요.")

# 현재 메뉴 보기
with st.expander("📋 현재 메뉴 리스트 보기"):
    current_list = st.session_state.menus[category]
    if current_list:
        for menu in current_list:
            st.write(f"• {menu['name']} - {menu['price']:,}원")
    else:
        st.write("메뉴가 없습니다.")
