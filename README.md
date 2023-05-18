# 현재 진행도

### 현재는 js파일 미작성 상태
-> 추가사항으로만 작성하여 open ai api통신 가능  
<br/>

### <구현되지 않은것들 (js파일에 들어갈것)>
* 카테고리 및 주제, 별점, 사유 송신해서 전체 출력 및 재출력 연결
* 카테고리에 따른 주제 Listing
*  - 카테고리 선택-> 주제선택 종속 js로 구현                                 (1)
*  - 기타 카테고리 설정 시 주제 선택 self box 구현                           (2)
* 별점 및 재출력 hidden처리
* 누적 출력값 Indexing 하여 새 출력값이 있을 때마다 New Tab생성하여 저장       (3)
* 선택한 탭 output내용 저장
<br/>

### <미구현 사항 참고 레퍼>  
[HTML/CSS/JS 연결방법](https://basemenks.tistory.com/20)  
(1) [카테고리에 따른 주제 연동](https://chichi-story.tistory.com/18)  
(2) [select box에서 직접입력란 생성](https://hiworldbye.tistory.com/43)  
(3) 새 출력값마다 New Tab 생성하여 저장 레퍼 코드 하단확인  
<br/>

 ********************************************************************
 
```

<!DOCTYPE html>
<html>
<head>
  <title>누적 값 확인</title>
  <script>
    var tabs = []; // 탭을 저장할 배열
    var currentTab = null; // 현재 선택된 탭

    function addTab() {
      var tabName = prompt("새 탭의 이름을 입력하세요:");
      if (tabName) {
        // 새 탭 생성
        var tab = {
          name: tabName,
          values: []
        };

        // 탭 배열에 추가
        tabs.push(tab);

        // 탭 선택
        selectTab(tab);
      }
    }

    function selectTab(tab) {
      // 현재 선택된 탭 스타일 제거
      if (currentTab) {
        currentTab.element.classList.remove("selected");
      }

      // 선택된 탭 스타일 적용
      tab.element.classList.add("selected");
      currentTab = tab;

      // 출력란 업데이트
      updateOutput();
    }

    function addValue() {
      if (!currentTab) {
        addTab();
      }

      var input = document.getElementById("inputValue");
      var value = input.value;

      // 값 추가
      currentTab.values.push(value);

      // 입력 필드 비우기
      input.value = "";

      // 출력란 업데이트
      updateOutput();
    }

    function updateOutput() {
      var output = document.getElementById("outputValue");
      output.innerHTML = "";

      if (currentTab) {
        // 선택된 탭의 값 출력
        for (var i = 0; i < currentTab.values.length; i++) {
          output.innerHTML += currentTab.values[i] + "<br>";
        }
      }
    }
  </script>
  <style>
    .selected {
      font-weight: bold;
    }
  </style>
</head>
<body>
  <button onclick="addTab()">새 탭 생성</button>
  <hr>
  <input type="text" id="inputValue" placeholder="값을 입력하세요">
  <button onclick="addValue()">추가</button>
  <hr>
  <div id="outputValue"></div>
</body>
</html>

```
