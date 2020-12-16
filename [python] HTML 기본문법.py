# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:33:41 2020

@author: Owner
"""


■ 140. HTML 기본문법
*데이터 분석 순서 
데이터 수집 --> 데이터 유형 및 속성 파악 --> 데이터 변환 --> 데이터 저장 --> 데이터 정제 --> 데이터 분석

*데이터 수집 기술
웹스크롤링

*HTML 이란?
Hyper Text Markup Language 의 약자
여러개의 태그(tag)를 연결해서 모아놓은 문서

예제1. 아주 간단한 html 문서를 만들어 봅니다.
메모장을 열고 아래와 같이 코딩을 하세요.
<html><head><title> 송종미님의 오늘 일정 </title></head>
<body>
<p class="title"> 송종미님은 오늘 점심시간에 우육탕을 먹었습니다. </p>
</body>
</html>

메모장에 파일이름을 a.html 로 바탕화면에 저장하세요.
저장할 때 파일형식은 모든파일로 해주세요.

예제2. 위의 글씨 진하게 하시오!
<html><head><title> 송종미님의 오늘 일정 </title></head>
<body>
<p class="title"> <b> 송종미님은 오늘 점심시간에 우육탕을 먹었습니다. </b></p>
</body>
</html>

설명 : 글씨를 진하게 하려면 <b>를 이용합니다.

예제3. 위의 글씨에 밑줄을 그어보세요!
<html><head><title> 송종미님의 오늘 일정 </title></head>
<body>
<p class="title"> <b><u>송종미님은 오늘 점심시간에 우육탕을 먹었습니다. </u></b></p>
</body>
</html>

설명 : 밑줄을 사용하려면 <u> 를 사용합니다.

예제4. 위의 글씨를 이탤릭체로 변경하시오!
<html><head><title> 송종미님의 오늘 일정 </title></head>
<body>
<p class="title"> <b><u><i>송종미님은 오늘 점심시간에 우육탕을 먹었습니다. </i></u></b></p>
</body>
</html>

설명 : 이탤릭체를 사용하려면 <i> 를 사용합니다.

예제5. <p> 를 추가해서 제목과 내용을 나누시오!
<html><head><title> 송종미님의 오늘 일정 </title></head>
<body>
<p class="title"> <b><u><i>송종미님은 오늘 점심</i></u></b></p>
<p calss="content"> 송종미님은 오늘 점심에 지하식당으로 내려가서 친구들과 같이 우육탕을 먹었습니다. 코로나에 대한 걱정도 있었지만 용기내서 먹었습니다.</p>
</body>
</html>

설명 : 제목은 class title 에 적고 내용은 class content 에 적습니다.

예제6. 위에서 만든 html 문서의 본문에 링크를 거시오!
<html><head><title> 송종미님의 오늘 일정 </title></head>
<body>
<p class="title"> <b><u><i>송종미님은 오늘 점심</i></u></b></p>
<p calss="content"> 송종미님은 오늘 점심에 지하식당으로 내려가서 친구들과 같이 우육탕을 먹었습니다. 코로나에 대한 걱정도 있었지만 용기내서 먹었습니다.
<a href="http://cafe.daum.net/oracleoracle" class="cafe1" id="link1"> 다음카페 </a>
</p>
</body>
</html>

설명 : 워드 문서를 만들때도 그 문서내에 단원도 있고 세부목차도 있듯이 class 에 그 html 문서의 특정 단원이라고 보면 되고 id는 링크를 줄 때 부여하는 제목인데 id는 값이 unique 합니다.
