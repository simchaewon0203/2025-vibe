import streamlit as st
import random

# 기본 메뉴 리스트
if 'menu_list' not in st.session_state:
    st.session_state.menu_list = [
        "김치찌개", "된장찌개", "불고기", "삼겹살", "비빔밥",
        "치킨", "피자", "햄버거", "초밥", "떡볶이",
        "쌀국수", "짜장면", "짬뽕", "라면", "파스타"
    ]

st.title("🍽 오늘 저녁 뭐 먹지?")
st.write("버튼을 눌러 메뉴를 추천받으세요!")

# 추천 메뉴 출력 영역
if st.button("메뉴 추천 받기 🎲"):
    if st.session_state.menu_list:
        choice = random.choice(st.session_state.menu_list)
        st.success(f"오늘의 추천 메뉴는 **{choice}** 입니다!")
    else:
        st.warning("메뉴 리스트가 비어 있어요. 메뉴를 추가해주세요.")

# 메뉴 추가
with st.expander("메뉴 추가하기 ➕"):
    new_menu = st.text_input("추가할 메뉴 이름", key="add_input")
    if st.button("추가"):
        if new_menu:
            st.session_state.menu_list.append(new_menu)
            st.success(f"{new_menu} 메뉴가 추가되었습니다!")
        else:
            st.error("메뉴 이름을 입력해주세요.")

# 메뉴 삭제
with st.expander("메뉴 삭제하기 ➖"):
    if st.session_state.menu_list:
        menu_to_delete = st.selectbox("삭제할 메뉴 선택", st.session_state.menu_list)
        if st.button("삭제"):
            st.session_state.menu_list.remove(menu_to_delete)
            st.success(f"{menu_to_delete} 메뉴가 삭제되었습니다.")
    else:
        st.info("삭제할 수 있는 메뉴가 없습니다.")

# 현재 메뉴 리스트 보기
with st.expander("현재 메뉴 리스트 보기 📋"):
    if st.session_state.menu_list:
        st.write(", ".join(st.session_state.menu_list))
    else:
        st.write("메뉴가 없습니다.")
