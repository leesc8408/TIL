WEB_01

# CSS (Cascading Style Sheets)

- HTML로 작성된 문서의 표시 방법을 기술하기 위한 스타일 시트 언어입니다.
- 구조(rule set)
  - 선택자(selector) :  HTML 요소 이름. 이것은 꾸밀 요소를 선택합니다.
  - 선언 : `color: red`와 같은 꾸미기 원하는 요소의 속성과 속성값을 명시합니다.
  - rule set은 반드시 `{ }` 로 감싸져야 합니다


---

#### BOX model

![box model을 구성하는 요소](https://images.velog.io/images/gil0127/post/1b3fcbde-3863-4a5c-909a-8b58e74f73ac/%EB%B0%95%EC%8A%A4%EB%A5%BC%20%EA%B5%AC%EC%84%B1%ED%95%98%EB%8A%94%20%EC%9A%94%EC%86%8C.png)

- margin : **바깥 여백 영역**
  - 테두리 요소를 확장해 요소와 인근 요소 사이의 빈 공간까지 포함
- border : **테두리 영역**
  - 안쪽 여백 영역을 요소의 테두리까지 포함하는 크기
- padding : **안쪽 여백 영역**
  - 콘텐츠 영역을 요소의 안쪽 여백까지 포함하는 크기
- content : **콘텐츠 영역**
  - 글이나 이미지, 비디오 등 요소의 실제 내용을 포함합니다. 