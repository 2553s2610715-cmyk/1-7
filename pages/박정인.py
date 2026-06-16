<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>진로 추천 테스트</title>

<style>
body {
    font-family: "Malgun Gothic", sans-serif;
    background: linear-gradient(135deg, #4facfe, #00f2fe);
    margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

.container {
    background: white;
    width: 90%;
    max-width: 500px;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

h1 {
    text-align: center;
    color: #333;
}

label {
    display: block;
    margin-top: 15px;
    font-weight: bold;
}

select, button {
    width: 100%;
    padding: 12px;
    margin-top: 8px;
    border-radius: 8px;
    border: 1px solid #ccc;
    font-size: 16px;
}

button {
    background: #0078ff;
    color: white;
    border: none;
    cursor: pointer;
    margin-top: 20px;
    font-weight: bold;
}

button:hover {
    background: #005fd1;
}

#result {
    margin-top: 20px;
    padding: 15px;
    background: #f5f5f5;
    border-radius: 10px;
    white-space: pre-line;
    display: none;
}
</style>
</head>

<body>

<div class="container">
    <h1>🎯 진로 추천 테스트</h1>

    <label>좋아하는 활동은?</label>
    <select id="activity">
        <option value="tech">💻 프로그래밍/기술</option>
        <option value="art">🎨 예술/디자인</option>
        <option value="business">📈 경영/마케팅</option>
        <option value="science">🔬 과학/연구</option>
    </select>

    <label>가장 중요하게 생각하는 것은?</label>
    <select id="priority">
        <option value="salary">💰 높은 연봉</option>
        <option value="creativity">✨ 창의성</option>
        <option value="stability">🏢 안정성</option>
        <option value="impact">🌍 사회 기여</option>
    </select>

    <button onclick="recommendCareer()">결과 보기</button>

    <div id="result"></div>
</div>

<script>
function recommendCareer() {
    const activity = document.getElementById("activity").value;
    const priority = document.getElementById("priority").value;

    let career = "";
    let detail = "";

    switch(activity) {
        case "tech":
            career = "소프트웨어 개발자, AI 엔지니어, 데이터 분석가";
            break;
        case "art":
            career = "그래픽 디자이너, UX/UI 디자이너, 영상 제작자";
            break;
        case "business":
            career = "마케터, 사업기획자, 경영 컨설턴트";
            break;
        case "science":
            career = "연구원, 바이오 과학자, 환경 전문가";
            break;
    }

    switch(priority) {
        case "salary":
            detail = "고소득 가능성이 높은 분야를 추천합니다.";
            break;
        case "creativity":
            detail = "창의성을 발휘할 수 있는 분야를 추천합니다.";
            break;
        case "stability":
            detail = "비교적 안정적인 직업군을 추천합니다.";
            break;
        case "impact":
            detail = "사회에 긍정적인 영향을 줄 수 있는 분야를 추천합니다.";
            break;
    }

    const resultBox = document.getElementById("result");
    resultBox.style.display = "block";
    resultBox.innerHTML =
    `✅ 추천 진로

${career}

📌 추천 이유
${detail}

🚀 앞으로 관련 공부와 경험을 쌓아보세요!`;
}
</script>

</body>
</html>
