WEB_01

# HTML

- HyperText : 웹 페이지를 다른 페이지로 연결하는 링크
- Markup Language : 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

---

HTML 태그

- \<head>
  - 기계가 식별할 수 있는 문서의 정보(제목, 스크립트, 스타일시트 등)를 담는다. 

  - 가능한 부모 요소 : `<html>` 요소의 첫번째 자식으로 배치.

  - HTML5 호환 브라우저는 `<head>`가 없는 경우 자동으로 생성.

  - 배치가능 요소

    `<title>`, `<base>`, `<link>`, `<style>`, `<meta>`, `<script>`, `<noscript>`, `<template>`

    ```html
    <!doctype html>
    <html>
      <head>
        <title>문서 제목</title>
      </head>
    </html>
    ```

- \<title>

  - 브라우저의 제목 표시줄이나 페이지 탭에 보이는 문서 제목을 정의합니다.

    **텍스트만 포함**할 수 있으며 `<head>`안에서 사용

  - 가능한 부모 요소 : 다른 `<title>` 요소를 포함하지 않은 `<head>`

    ```html
    <!doctype html>
    <html>
      <head>
        <title>엄청 흥미로운 내용</title>
      </head>
    </html>
    ```

- \<body>

  - HTML 문서의 내용을 나타내며 한 문서에 하나의 `<body>` 요소만 존재할 수 있습니다

  - 가능한 부모 요소 : `<html>` 요소의 두번째 자식 요소로 배치.

    ```html
    <html>
      <head>
        <title>문서 제목</title>
      </head>
      <body>
        <p>문단입니다</p>
      </body>
    </html>
    
    ```

- \<a>

  - `href`특성을 통해 다른 페이지나 같은 페이지의 어느 위치, 파일, 이메일 주소와 그 외 다른 URL로 연결할 수 있는 하이퍼링크를 만듭니다.
  - 가능한 부모 요소 : 구문 콘텐츠를 허용하는 모든 요소

  ```html
  <a href="https://www.mozilla.com">
    Mozilla
  </a>
  ```

- \<b>

  - 중요성이 없는 텍스트를 굵은 글씨로 나타낼때 사용합니다.

    *중요성, 강조, 관련성이 있는 텍스트는 `<strong>`, `<em>`, `<mark>`를 사용권장

  - 가능한 부모 요소 : 구문 콘텐츠를 허용하는 모든 요소

    ```html
    <p>Keywords are displayed with the default style of the <b>element, likely in bold</b>.</p>
    ```

- \<strong>

  - 중대하거나 긴급한 콘텐츠를 나타냅니다.

  - 가능한 부모 요소 : 구문 콘텐츠를 허용하는 모든 요소

    ```html
    <p>Before proceeding, <strong>make sure you put on your safety goggles</strong>.</p>
    ```

- \<i>

  - 텍스트에서 주위와 구분해야 하는 부분에 사용하며 기울림꼴로 표시됩니다. 

  - 가능한 부모 요소 : 구문 콘텐츠를 허용하는 모든 요소

    ```html
    <p>라틴어 문구 <i>Veni, vidi, vici</i>는 음악과 예술, 문학에 자주 등장합니다.</p>
    ```

- \<em>

  - 텍스트를 강조 합니다.

  - `<i>`와 같이 기울림꼴이지만 `<em>`은 구분보다는 강조를 의미하므로 사용시 차이를 생각한다.

    ```html
    <p>
      과거에 <em>block-level</em>이라 불렸던
      콘텐츠는 HTML 5부터 <em>flow</em> 콘텐츠라고
      말합니다.
    </p>
    ```

- \<img>

  - 문서에 이미지를 넣습니다.

  - `src` 특성은 **필수**이며, 포함하고자 하는 이미지로의 경로를 지정

    `alt` 특성은 경로오류 시 이미지의 텍스트 설명이며 필수는 아님.

    ```html
    <img src="favicon144.png"
         alt="MDN logo">
    ```

- \<span>

  - 별도의 스타일을 지정하기 위해 사용합니다.

  - `<span>`은 `<div>`와 매우 유사하지만, 

    `<div>`는 블록 레벨 요소인 반면 `<span>`은 인라인 요소입니다.

    ```html
    <p>
      과거에 <span class="point">block-level</span>이라 불렸던 콘텐츠는 HTML 5부터 
      flow 콘텐츠라고 말합니다.
    </p>
    ```

- \<div>

  - 플로우 콘텐츠를 위한 통용 컨테이너입니다.

    ***CSS**로 꾸미기 전에는 콘텐츠나 레이아웃에 어떤 영향도 주지 않습니다.

  - 다른 요소 여럿을 묶어 속성으로 꾸미기 쉽도록 돕거나, 

    문서의 특정 구역이 다른 언어입을 표시하는 용도로 사용가능.

    ```html
    <div class="warning">
        <img src="/media/examples/leopard.jpg"
             alt="An intimidating leopard.">
        <p>Beware of the leopard</p>
    </div>
    ```

- \<p>

  - 하나의 문단을 나타내며 블록 레벨 요소입니다. 

    ```html
    <p>첫 번째 문단입니다.
      첫 번째 문단입니다.
      첫 번째 문단입니다.
      첫 번째 문단입니다.</p>
    <p>두 번째 문단입니다.
      두 번째 문단입니다.
      두 번째 문단입니다.
      두 번째 문단입니다.</p>
    ```

- \<br>

  - 텍스트 블록에서 줄을 바꿉니다. (enter를 표현)

    ```html
    <p>첫 번째 문단입니다.
      첫 번째 문단입니다.
      첫 번째 문단입니다.
      첫 번째 문단입니다.</p>
    <p>두 번째 문단입니다.<br>
      두 번째 문단입니다.<br>
      두 번째 문단입니다.<br>
      두 번째 문단입니다.</p>
    ```

- \<hr>

  - 수평선(가로줄)을 생성하여 문단 레벨 요소에서 주제의 분리를 나타냅니다.

    ***CSS**로 꾸미기가 가능합니다.

    ```html
    <p>첫 번째 문단입니다.
      첫 번째 문단입니다.
      첫 번째 문단입니다.
      첫 번째 문단입니다.</p>
    <hr>
    <p>두 번째 문단입니다.<br>
      두 번째 문단입니다.<br>
      두 번째 문단입니다.<br>
      두 번째 문단입니다.</p>
    ```

- \<ul>

  - 순서가 없는 리스트를 생성합니다.

    ```html
    <ul>
      <li>first item</li>
      <li>second item</li>
      <li>third item</li>
    </ul>
    ```

- \<ol>

  - 순서가 있는 리스트를 생성합니다.

    ```html
    <ol>
      <li>first item</li>
      <li>second item</li>
      <li>third item</li>
    </ol>
    ```

    

- \<pre>

  - HTML에 **작성한 내용 그대로 표현**합니다. 

    텍스트는 보통 고정폭 글꼴을 사용해 렌더링하고, 요소 내 **공백문자를 그대로 유지**합니다.

    *`<br>` 사용 없이 줄을 바꿀 수 있음.

    ```html
    <p>CSS로 글자 색을 바꾸는건 쉽습니다.</p>
    <pre>
    body {
      color:red;
    }
    </pre>
    
    ```

- \<blockquote>

  - 텍스트를 인용문으로 나타냅니다. 

    ***CSS**로 꾸미기가 가능합니다.

    ```html
    <blockquote>
    <p>Words can be like X-rays, if you use them properly—they’ll go through anything. You read and you’re pierced.</p>
    </blockquote>
    <p>—Aldous Huxley, <cite>Brave New World</cite></p>
    ```

- \<h1> ~ \<h6>

  - 6단계의 구획 제목을 나타냅니다.

    ```html
    <h1>Heading level 1</h1>
    <h2>Heading level 2</h2>
    <h3>Heading level 3</h3>
    <h4>Heading level 4</h4>
    <h5>Heading level 5</h5>
    <h6>Heading level 6</h6>
    ```

    