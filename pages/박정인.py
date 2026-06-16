<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>진로 상담</title>

<style>
body{
    font-family: Arial, sans-serif;
    background:#f0f4f8;
    margin:0;
    padding:40px;
}
.box{
    max-width:500px;
    margin:auto;
    background:white;
    padding:20px;
    border-radius:10px;
    box-shadow:0 0 10px rgba(0,0,0,0.1);
}
select,button{
    width:100%;
    padding:10px;
    margin-top:10px;
}
#result{
    margin-top:20px;
    padding:15px;
    background:#eef;
    border-radius:8px;
}
</style>
</head>

<body>

<div class="box">
    <h1>진로 추천</h1>

    <p>관심 분야를 선택하세요.</p>

    <select id="field">
        <option value="개발자">프로그래밍</option>
        <option value="디자이너">디자인</option>
        <option value="마케터">마케팅</option>
        <option value="연구원">과학</option>
    </select>

    <button id="btn">추천받기</button>

    <div id="result">결과가 여기에 표시됩니다.</div>
</div>

<script>
document.getElementById("btn").addEventListener("click", function () {

    var field = document.getElementById("field").value;
    var text = "";

    if (field === "개발자") {
        text = "추천 직업: 개발자, AI 엔지니어, 데이터 분석가";
    } else if (field === "디자이너") {
        text = "추천 직업: UI/UX 디자이너, 그래픽 디자이너";
    } else if (field === "마케터") {
        text = "추천 직업: 마케팅 전문가, 브랜드 매니저";
    } else {
        text = "추천 직업: 연구원, 과학자";
    }

    document.getElementById("result").textContent = text;
});
</script>

</body>
</html>
