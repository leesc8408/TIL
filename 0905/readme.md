### 📕Table

- table의 각 영억을 명시하기 위해  `<thead>`, `<tbody>`, `<tfoot>` 요소를 활용

- table 태그 기본 구성

  ```html
  <body>
       <table>    <!-- 테이블 태그 -->
          <thead> <!-- 헤드 요소 -->
              <tr>    <!-- 테이블 행 -->
                  <th>ID</th> <!-- 행에 열로써 들어가는 데이터 셀-->
                  <th>NAME</th>   <!-- 헤드에 들어가는 데이터 셀은 <th>로 입력 -->
                  <th>MAJOR</th>
              </tr>
          </thead>
          <tbody> <!-- 바디 요소 -->
              <tr>
                  <td>1</td>  <!-- 헤드 이외의 요소의 데이터 셀은 <td>로 입력 -->
                  <td>홍길동</td>
                  <td>computer science</td>
              </tr>
          </tbody>
          <tbody>
              <tr>
                  <td>2</td>
                  <td>김철수</td>
                  <td>business</td>
              </tr>
          </tbody>
          <tfoot> <!-- 풋 요소 -->
              <td>총계</td>
              <td colspan="2">2명</td>    <!-- 입력 셀이 다른 데이터의 3셀과 달리 2셀일 경우 셀을 colspan으로 셀을 병합한다. -->
          </tfoot>
          <caption>1반 학색 명단</caption>
      </table>
  </body>
  ```

  