import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="원형 룰렛", layout="centered")
st.title("🎯 진짜 원형 룰렛으로 취미 뽑기")

st.markdown("룰렛을 클릭해 돌려보세요! 화살표가 가리키는 곳이 오늘의 취미입니다.")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=SUIT&display=swap');

body {
  font-family: 'SUIT', sans-serif;
  text-align: center;
  background-color: #f9f9f9;
}

canvas {
  margin-top: 20px;
}

#arrow {
  position: absolute;
  top: 95px;
  left: 50%;
  transform: translateX(-50%);
  width: 0; 
  height: 0; 
  border-left: 20px solid transparent;
  border-right: 20px solid transparent;
  border-bottom: 30px solid red;
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
<canvas id="wheelCanvas" width="400" height="400"></canvas>
<div id="result">👇 룰렛을 클릭하세요!</div>

<script>
const hobbies = [
  "책 읽기", "요리하기", "산책하기", "그림 그리기", "보드게임",
  "자전거 타기", "영화 보기", "사진 찍기", "헬스장 가기", "뜨개질"
];

const canvas = document.getElementById("wheelCanvas");
const ctx = canvas.getContext("2d");
const radius = canvas.width / 2;
let startAngle = 0;
let arc = Math.PI * 2 / hobbies.length;
let spinAngle = 0;
let spinning = false;

function drawWheel() {
  for (let i = 0; i < hobbies.length; i++) {
    const angle = startAngle + i * arc;
    ctx.beginPath();
    ctx.fillStyle = i % 2 == 0 ? "#f39c12" : "#f1c40f";
    ctx.moveTo(radius, radius);
    ctx.arc(radius, radius, radius, angle, angle + arc, false);
    ctx.fill();
    
    ctx.save();
    ctx.fillStyle = "white";
    ctx.translate(radius, radius);
    ctx.rotate(angle + arc / 2);
    ctx.textAlign = "right";
    ctx.font = "bold 16px SUIT";
    ctx.fillText(hobbies[i], radius - 10, 10);
    ctx.restore();
  }
}

function spinWheel() {
  if (spinning) return;
  spinning = true;
  let spinTime = 0;
  let spinTimeTotal = 4000;
  let spinAngleStart = Math.random() * 10 + 10;

  function rotate() {
    spinTime += 30;
    if (spinTime >= spinTimeTotal) {
      stopRotateWheel();
      return;
    }
    let spinAngleIncrement = easeOut(spinTime, 0, spinAngleStart, spinTimeTotal);
    startAngle += (spinAngleIncrement * Math.PI / 180);
    drawRoulette();
    requestAnimationFrame(rotate);
  }

  rotate();
}

function stopRotateWheel() {
  let degrees = startAngle * 180 / Math.PI + 90;
  let arcDeg = arc * 180 / Math.PI;
  let index = Math.floor((360 - degrees % 360) / arcDeg) % hobbies.length;
  document.getElementById("result").innerHTML = `🎉 오늘의 취미는 <span style="color:#e74c3c;">${hobbies[index]}</span> 입니다! 🎉`;
  spinning = false;
}

function easeOut(t, b, c, d) {
  let ts = (t/=d)*t;
  let tc = ts*t;
  return b+c*(tc + -3*ts + 3*t);
}

function drawRoulette() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawWheel();
}

canvas.addEventListener("click", spinWheel);
drawWheel();
</script>

</body>
</html>
"""

components.html(html_code, height=500)
