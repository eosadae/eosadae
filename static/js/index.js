//카테고리-주제 연결 select box

function categoryChange(ctgry){
    var sbj_a = ["IT교실"]
    var sbj_b = ["비밀정원","요리교실","음식영양소","정보통","지역탐방"];
    var sbj_c = ["노래 소통","오늘의 저녁"];
    var sbj_d = ["마음그림","순이공방","시시콜콜"];
    var sbj_e = ["일어교실","영어교실"];
    var sbj_f = ["순이체육회","순이체조"];
    var sbj_g = ["노래자랑","팝송듣기"];
    var sbj_h = ["무비순이","순이책방"];
    var sbj_i = ["끝말잇기","빙고게임","사자성어","속담퀴즈","신조어퀴즈"];
    var sbj_j = ["꽃말 수업","명언산책","웃음치료"];
    var target = document.getElementById("sbj");

    if(ctgry == "a") var subject = sbj_a;
    else if(ctgry == "b") var subject =sbj_b;
    else if(ctgry == "c") var subject =sbj_c;
    else if(ctgry == "d") var subject =sbj_d;
    else if(ctgry == "e") var subject =sbj_e;
    else if(ctgry == "f") var subject =sbj_f;
    else if(ctgry == "g") var subject =sbj_g;
    else if(ctgry == "h") var subject =sbj_h;
    else if(ctgry == "i") var subject =sbj_i;
    else if(ctgry == "j") var subject =sbj_j;

    console.log(ctgry);
    target.options.length = 1;

    for (x in subject){
        var opt = document.createElement("option");
        opt.value = subject[x];
        opt.innerHTML = subject[x];
        target.appendChild(opt);
    }
}

