//카테고리-주제 연결 select box

function categoryChange(ctgry){
    var sbj_a = ["IT교실"]
    var sbj_b = ["비밀정원","요리교실","음식영양소","정보통","지역탐방"];
    var sbj_c = ["노래_소통","오늘의_저녁"];
    var sbj_d = ["마음그림","순이공방","시시콜콜"];
    var sbj_e = ["일어교실","영어교실"];
    var sbj_f = ["순이체육회","순이체조"];
    var sbj_g = ["노래자랑","팝송듣기"];
    var sbj_h = ["무비순이","순이책방"];
    var sbj_i = ["끝말잇기","빙고게임","사자성어","속담퀴즈","신조어퀴즈"];
    var sbj_j = ["꽃말 수업","명언산책","웃음치료"];
    var target = document.getElementById("sbj");

    if(ctgry == "IT") var subject = sbj_a;
    else if(ctgry == "생활") var subject =sbj_b;
    else if(ctgry == "소통") var subject =sbj_c;
    else if(ctgry == "예술") var subject =sbj_d;
    else if(ctgry == "외국어") var subject =sbj_e;
    else if(ctgry == "운동") var subject =sbj_f;
    else if(ctgry == "음악") var subject =sbj_g;
    else if(ctgry == "인문") var subject =sbj_h;
    else if(ctgry == "퀴즈") var subject =sbj_i;
    else if(ctgry == "힐링") var subject =sbj_j;

    target.options.length = 1;

    for (x in subject){
        var opt = document.createElement("option");
        opt.value = subject[x];
        opt.innerHTML = subject[x];
        target.appendChild(opt);
    }
}
$('#chat-form').on('submit', function(e) {
    e.preventDefault();
    var ctgry = $('#Category').val();
    var sbj = $('#sbj').val();
    var additionalRequest = $('#input').val();

    console.log('Category:', ctgry);
    console.log('Subject:', sbj);
    console.log('Additional request:', additionalRequest);

    $.ajax({
        url: '/user_input',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            'category': ctgry,
            'topic': sbj,
            'additional_request': additionalRequest,
        }),
        success: function(response) {
            console.log(response);
            $('.table_rec').html("<p>" + response.script + "</p>");  // script 키로 접근
        }
    });
});
$('#image').on('submit', function(e) {
    e.preventDefault();
    var imageKeyword = $('#input_image').val(); // 이미지 키워드 값을 가져옴

    console.log('Image keyword:', imageKeyword);

    $.ajax({
        url: '/image_input',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            'image_keyword': imageKeyword,
        }),
        success: function(response) {
            console.log(response);
            var imageTag = $("<img>"); // 새로운 img 태그를 생성합니다.
            imageTag.attr("src", response.script); // 받은 이미지 URL을 src 속성에 할당합니다.
            $(".table_rec.image").html(imageTag); // table_rec 클래스를 가진 요소의 내용을 새로 생성한 이미지 태그로 바꿉니다.
        }
    });
});
$('#rating-reason').on('submit', function(e) {
    e.preventDefault();
    var ctgry = $('#Category').val();
    var sbj = $('#sbj').val();
    var additionalRequest = $('#input').val();
    var feedbackScore = $('input[name="rating"]:checked').val();
    var feedbackText = $('#feedback_text').val();

    console.log('Category:', ctgry);
    console.log('Subject:', sbj);
    console.log('Additional request:', additionalRequest);
    console.log('Feedback score:', feedbackScore);
    console.log('Feedback text:', feedbackText);

    $.ajax({
        url: '/regenerate_input',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            'category': ctgry,
            'topic': sbj,
            'additional_request': additionalRequest,
            'feedback_score': feedbackScore,
            'feedback_text': feedbackText
        }),
        success: function(response) {
            console.log(response);
            $('.table_rec').html("<p>" + response.script + "</p>");  // script 키로 접근
        }
    });
});