import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="중앙 고정 화살표 룰렛", layout="centered")
st.title("🎯 중앙에서 쏘는 화살표 룰렛")

st.markdown("룰렛을 클릭하면 중심 화살표가 가리키는 오늘의 취미가 결정됩니다!")

html_code = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=SUIT&display=swap');

    body {
      font-family: 'SUIT', sans-serif;
      background-color: #f9f9f9;
      text-align: center;
    }

    #canvas-container {
      position: relative;
      display: inline-block;
      margin-top: 10px;
    }

    canvas {
      border-radius: 50%;
      background-color: #ffffff;
    }

    #center-arrow {
      position: absolute;
      top: 0%;
      left: 50%;
      transform: translate(-50%, -50%) rotate(0deg);
      z-index: 10;
      pointer-events: none;
    }

    #center-arrow::after {
      content: "";
      width: 0;
      height: 0;
      border-left: 8px solid transparent;
      border-right: 8px solid transparent;
      border-top: 30px solid red;
      display: block;
      margin: 0 auto;
    }

    #result {
      margin-top: 40px;
      font-size: 28px;
      font-weight: bold;
      color: #2c3e50;
    }

    .highlight {
      color: #e74c3c;
      font-size: 36px;
      animation: pop 0.6s ease-out;
    }

    @keyframes pop {
      0% { transform: scale(0.5); opacity: 0; }
      50% { transform: scale(1.2); opacity: 1; }
      100% { transform: scale(1); }
    }
  </style>
</head>
<body>

<h3>룰렛을 클릭하세요!</h3>
<div id="canvas-container">
  <canvas id="wheelCanvas" width="400" height="400"></canvas>
  <div id="center-arrow"></div>
</div>

<div id="result">👇 돌려보세요!</div>

<script>
const hobbies = [
  "책 읽기", "요리하기", "산책하기", "그림 그리기", "보드게임", "자전거 타기",
  "영화 보기", "사진 찍기", "헬스장 가기", "뜨개질", "코딩 공부", "명상하기",
  "플라워 클래스", "홈카페 만들기", "웹툰 그리기", "퍼즐 맞추기", "클라이밍",
  "댄스 배우기", "마크라메", "캘리그래피", "도예 체험", "수영 배우기", "낚시하기"
];

const canvas = document.getElementById("wheelCanvas");
const ctx = canvas.getContext("2d");
const radius = canvas.width / 2;
let startAngle = 0;
const arc = Math.PI * 2 / hobbies.length;
let spinning = false;

function drawWheel() {
  for (let i = 0; i < hobbies.length; i++) {
    const angle = startAngle + i * arc;
    ctx.beginPath();
    ctx.fillStyle = i % 2 === 0 ? "#f39c12" : "#f1c40f";
    ctx.moveTo(radius, radius);
    ctx.arc(radius, radius, radius, angle, angle + arc, false);
    ctx.fill();

    ctx.save();
    ctx.fillStyle = "#fff";
    ctx.translate(radius, radius);
    ctx.rotate(angle + arc / 2);
    ctx.textAlign = "right";
    ctx.font = "bold 12px SUIT";
    ctx.fillText(hobbies[i], radius - 10, 5);
    ctx.restore();
  }
}

function spinWheel() {
  if (spinning) return;
  spinning = true;
  let spinAngle = Math.random() * 20 + 30;
  let spinTime = 0;
  const spinTimeTotal = 5000;

  function rotate() {
    spinTime += 30;
    const progress = spinTime / spinTimeTotal;
    const ease = Math.pow(1 - progress, 3);
    startAngle += (spinAngle * ease) * Math.PI / 180;

    drawRoulette();

    if (spinTime < spinTimeTotal) {
      requestAnimationFrame(rotate);
    } else {
      stopWheel();
    }
  }

  rotate();
}

function stopWheel() {
  let degrees = (startAngle * 180 / Math.PI + 90) % 360;  // 위쪽이 기준이므로 +90 → +270
  const arcDegrees = arc * 180 / Math.PI;
  const index = Math.floor((360 - degrees) / arcDegrees) % hobbies.length;
  const selected = hobbies[index];

  const result = document.getElementById("result");
  result.innerHTML = `🎉 오늘의 취미는 <span class='highlight'>${selected}</span> 입니다! 🎉`;
  spinning = false;
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

components.html(html_code, height=600)
