import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="진짜 룰렛", layout="centered")
st.title("🎯 취미 룰렛 - 진짜 회전판!")

st.markdown("버튼을 눌러 룰렛을 돌려보세요!")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
#wheel {
  width: 300px;
  height: 300px;
  border-radius: 50%;
  border: 10px solid #f39c12;
  position: relative;
  margin: auto;
  box-shadow: 0 0 10px rgba(0,0,0,0.3);
  transition: transform 5s cubic-bezier(0.33, 1, 0.68, 1);
}

#wheel .segment {
  position: absolute;
  width: 50%;
  height: 50%;
  top: 50%;
  left: 50%;
  transform-origin: 0% 0%;
  background: #f1c40f;
  text-align: left;
  padding-left: 10px;
  padding-top: 10px;
  font-size: 14px;
  font-weight: bold;
}

#arrow {
  width: 0;
  height: 0;
  border-left: 20px solid transparent;
  border-right: 20px solid transparent;
  border-bottom: 30px solid red;
  position: absolute;
  top: -40px;
  left: 50%;
  transform: translateX(-50%);
}
</style>
</head>
<body>

<div id="arrow"></div>
<div id="wheel">
</div>

<script>
let hobbies = [
  "책 읽기", "요리하기", "산책하기", "그림 그리기", "보드게임",
  "자전거 타기", "영화 보기", "사진 찍기", "헬스장 가기", "뜨개질"
];

const wheel = document.getElementById("wheel");

// Create segments
for (let i = 0; i < hobbies.length; i++) {
  let seg = document.createElement("div");
  seg.className = "segment";
  seg.style.transform = "rotate(" + (i * 360 / hobbies.length) + "deg) skewY(-" + (90 - (360 / hobbies.length)) + "deg)";
  seg.innerHTML = hobbies[i];
  wheel.appendChild(seg);
}

// Spin function
function spinWheel() {
  let spins = Math.floor(Math.random() * 5 + 5);  // 5~9회전
  let deg = spins * 360 + Math.floor(Math.random() * 360);  // random angle
  wheel.style.transform = "rotate(" + deg + "deg)";
}

document.addEventListener("click", spinWheel);
</script>

</body>
</html>
"""

components.html(html_code, height=400)
