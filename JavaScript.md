

# JavaScript



JavaScript는 표준 웹 기술이라고 불리는 3가지 요소 중 하나로 HTML, CSS 그리고 나머지 한가지가 바로 JavaScript이다.

HTML이 콘텐츠의 구조를 짜고 의미를 부여한다면

CSS는 이러한 HTML에 색상이나 글꼴 등의 스타일을 입혀준다.

JavaScript는 이렇게 구성된 콘텐츠를 동적으로 활용할 수 있게 해주는 스크립팅 언어다.

예를 들면 HTML이 웹에 단어를 보여주면 CSS는 이러한 단어에 배경색이나 글꼴 등의 스타일을 입힐 수가 있고 JavaScript는 단어를 클릭했을때 알림창을 띄우는 등의 동적인 활용을 가능하게 해준다.



JavaScript는 다양한 기능이 있지만 가장 중요한 기능은 API (Application Programming Interface)이다.

API는 자바에서 자주 쓰이는 클래스 및 인터페이스를 제공하는 라이브러리로 일반적으로 두가지로 구분 가능하다.

1. 브라우저 API

   브라우저 API는 웹 브라우저에 내장된 것으로서 현재 컴퓨터 환경에 관한 데이터를 제공하거나 여러가지 유용하고 복잡한 일을 수행한다. DOM AIP, Geolocation API, WebGL API 등이 있다.

   

2. 서프파티 API

   브라우저에 탑재되지 않은 API를 말한다. (트위터, 구글 등 각종 공개 API)





### JavaScript가 하는 일



웹페이지를 불러오면 브라우저는 HTML, CSS, JavaScript를 실행환경에서 실행한다.

여기서 보통 JavaScript는 DOM API를 통해 HTML과 CSS를 동적으로 수정, UI를 업데이트 하는 일에 가장 많이 쓰인다.



### 브라우저 보안

각각의 브라우저 탭은 코드를 실행하기 위한 독립적인 그릇 (실행 환경이라 부름)이다.



### JavaScripit 실행 순서

다른 언어와 마찬가지로 일반적으로 위에서 아래로 코드가 실행된다.



### 서버사이드와 클라이언트 사이드 코드



클라이언트 사이드 코드는 사용자의 컴퓨터에서 동작하는 코드를 말한다.

웹 페이지를 방문하면 브라우저가 코드를 다운받아 실행하여 동작한다.

반면 서버 사이드 코드는 서버에서 동작하는 코드로 실행 결과를 브라우저가 다운로드해서 화면에 띄운다. 

서버사이드 웹 언어로는 PHP, Python, 루비 등이 있고 JavaScript도 여기에 포함된다. (Node.js)



### JavaScript 파일 (.js) 생성하기



```html
<script src="script_name.js" defer> Code </script>
```



HTML파일과 같은 폴더에 script_name.js 로 새로운 파일을 만들고 `<script>` 요소에 다음 코드를 입력하여 저장한다.

JavaScript 파일을 외부로 분리하여 여러 HTML 파일에서 같은 JS 코드를 재사용할수 있게 해준다.



### 인라인 JavaScript



```javascript
function createParagraph() {
  const para = document.createElement('p');
  para.textContent = 'You clicked the button!';
  document.body.appendChild(para);
}
```



```html
<button onclick="createParagraph()">Click me!</button>
```



위의 JS 코드를 아래와 같이 HTML에 입력할 수 있다.

그러나 이러한 방법은 효율적이지 못해 잘 사용하지 않는다.



### 스크립트 로딩 전략

스크립트를 적절한 시점에 불러오는 것은 중요한 문제이다.

만약 아무런 작업도 하지 않았다면 페이지는 위에서 아래까지 순서대로 코드를 실행할 것이다.

JS를 사용해서 페이지 내의 요소를 조작하려고 할 때, 해당 요소를 포함한 HTML 코드보다 JS를 먼저 불러와버리면 코드가 올바르게 동작할 수 없다.

이러한 문제를 막기위해 `defer` 과 `async` 를 사용한다.

`async` 특성은 스크립트를 가져오는 동안 페이지 로딩을 계속 한다. 그러나 스크립트 다운이 끝나면 스크립트가 바로 실행되는데 이때 페이지 렌더링이 중단된다.

따라서 스크립트가 실행되는 순서를 조절하기 어렵다.

반면 `defer` 특성은 지정한 스크립트는 페이지 내에서 배치한 순서대로 불러오게 된다.

또한, 페이지 콘텐츠를 모두 불러오기 전까지는 실행하지 않아 페이지 요소를 수정하거나 추가하는 등 DOM 작업을 기대하는 스크립트에 유용하다.



![](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript/async-defer.jpg)

특성 별 스크립트의 로딩 전략







### 주석

- 한줄 주석

  ```javascript
  // 주석
  ```

  

- 여러줄 주석

  ```javascript
  /*
  1 
  2
  3
  */
  ```

  



### 변수 선언



JavaScript에서는 변수와 상수가 존재하며 변수의 값은 바꿀 수 있지만 상수의 값은 바꿀 수 없다.

변수는 `let` 를 통해 선언하고 상수는 `const`를 통해 선언한다.

상수 HTML 요소 내부의 텍스트는 바꿀 수 있지만 상수가 가르키는 요소 그 자체를 바꿀 수는 없다.



구버전의 JavaScript에서는 변수와 상수 모두 `var`로 선언했지만 몇가지 문제로 인해 현 버전에서는 `let`와 `const`가 그 역할을 나누어서 하고있다.

여전히 `var`은 사용가능하지만 차이점이 있다.

1. `var`은 중복 선언이 가능하지만 `let`, `const` 는 중복 선언이 불가능하다.
2. `var`은 함수 레벨 범위를 가지지만 `let`, `const`는 블록레벨 범위를 가진다.
3. `var`은 변수 호이스팅이 발생하지만 `let`, `const`는 호이스팅이 발생하지만 값을 참조할 수 없는 호이스팅이 발생한다.



### 함수



```javascript
function checkGuess() {
  alert('I am a placeholder');
}
```



다른 언어의 함수와 비슷한 기능을 하며 작성 방식은 위처럼 function 함수명() { 코드 } 의 형식을 가진다.



### 연산자



사칙연산은 `+ - * /`  연산자를 사용한다. ( `+` 는 문자열에도 사용 가능하다.)

파이썬처럼 `+=` 과 같은 연산자도 사용 가능하다

비교연산자는 `===` `!==` `<` `>` 을 사용한다.



### 이벤트

이벤트란 브라우저를 통해 발생하는 여러 일 (버튼 클릭, 페이지 로딩, 비디오 재생 등)을 말한다.

이벤트 수신기가 특정 이벤트의 발생을 감지하고, 이벤트 처리기를 호출하면 이벤트 처리기가 이벤트에 반응한다.

```javascript
guessSubmit.addEventListener('click', checkGuess);
```



위의 코드에서 `addEventListener(이벤트 유형, 함수)` 가 이벤트 수신기 메서드이다.

(함수에는 () 를 붙이지 않는다. )



### 반복

JavaScript의 반복은 `for .. of` 를 사용한다.

아래는 JavaScript 반복문의 예시이다.

```javascript
const fruits = ['apples', 'bananas', 'cherries'];
for (const fruit of fruits) {
  console.log(fruit);
}
```



Python의 반복문과 비슷한 구조를 가지고있다. (in 대신 of를 사용)



```python
fruits = ['apples', 'bananas', 'cherries']
for fruit in fruits:
    console.log(fruit)
```

(파이썬으로 작성했을때 이러한 느낌)



### JavaScript 문법



JavaScript의 문법은 대부분 Java, C, C++에서 왔으며 그 외에 Awk, Perl, Python의 영향도 받았다.

