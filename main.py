import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="룰렛 취미 뽑기", layout="centered")
st.title("🎯 오늘 뭐하지?")

st.markdown("클릭하면 룰렛이 돌아가고, 최종 결과가 아래에 표시됩니다!")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Pretendard&display=swap');

body {
  font-family: 'Pretendard', sans-serif;
  text-align: center;
}

#wheel {
  width: 300px;
  height: 300px;
  border-radius: 50%;
  border: 10px solid #f39c12;
  margin: auto;
  position: relative;
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
  text-align: left;
  padding-left: 10px;
  padding-top: 10px;
  font-size: 14px;
  font-weight: bold;
  color: #fff;
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

#result {
  margin-top: 30px;
  font-size: 24px;
  font-weight: bold;
  color: #2c3e50;
}
</style>
</head>
<body>

<div id="arrow"></div>
<div id="wheel"></div>
<div id="result">👇 룰렛을 클릭해보세요!</div>

<script>
let hobbies = [
  "책 읽기", "요리하기", "산책하기", "그림 그리기", "보드게임",
  "자전거 타기", "영화 보기", "사진 찍기", "헬스장 가기", "뜨개질"
];

const wheel = document.getElementById("wheel");
const result = document.getElementById("result");

// 색상 팔레트
const colors = ["#1abc9c", "#3498db", "#9b59b6", "#e67e22", "#e74c3c", "#f1c40f", "#2ecc71", "#34495e", "#fd79a8", "#00cec9"];

// Create segments
for (let i = 0; i < hobbies.length; i++) {
  let seg = document.createElement("div");
  seg.className = "segment";
  seg.style.background = colors[i % colors.length];
  seg.style.transform = "rotate(" + (i * 360 / hobbies.length) + "deg) skewY(-" + (90 - (360 / hobbies.length)) + "deg)";
  seg.innerHTML = hobbies[i];
  wheel.appendChild(seg);
}

let rotating = false;

function spinWheel() {
  if (rotating) return;
  rotating = true;

  let spins = Math.floor(Math.random() * 5 + 5);  // 5~9회전
  let sectorAngle = 360 / hobbies.length;
  let randomSector = Math.floor(Math.random() * hobbies.length);
  let targetDeg = 360 * spins + (360 - randomSector * sectorAngle - sectorAngle / 2);

  wheel.style.transform = "rotate(" + targetDeg + "deg)";

  setTimeout(() => {
    result.innerHTML = `🎉 오늘의 추천 취미는 <span style='color:#e74c3c;'>${hobbies[randomSector]}</span> 입니다! 🎉`;
    rotating = false;
  }, 5200);
}

document.addEventListener("click", spinWheel);
</script>

</body>
</html>
"""

components.html(html_code, height=500)
