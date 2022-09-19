

# JavaScript



JavaScript는 표준 웹 기술이라고 불리는 3가지 요소 중 하나로 HTML, CSS 그리고 나머지 한가지가 바로 JavaScript이다.

HTML이 콘텐츠의 구조를 짜고 의미를 부여한다면

CSS는 이러한 HTML에 색상이나 글꼴 등의 스타일을 입혀준다.

JavaScript는 이렇게 구성된 콘텐츠를 동적으로 활용할 수 있게 해주는 스크립팅 언어다.

예를 들면 HTML이 웹에 단어를 보여주면 CSS는 이러한 단어에 배경색이나 글꼴 등의 스타일을 입힐 수가 있고 JavaScript는 단어를 클릭했을때 알림창을 띄우는 등의 동적인 활용을 가능하게 해준다.



JavaScript는 다양한 기능이 있지만 가장 중요한 기능은 API (Application Programming Interface)이다.

API는 JavaScript에서 자주 쓰이는 클래스 및 인터페이스를 제공하는 라이브러리로 일반적으로 두가지로 구분 가능하다.

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

(호이스팅이란 변수를 끌어오는 개념)

```
print(a)
a = 5
```

이러한 코드가 파이썬에선 안되지만 자바스크립트에서는 가능하다.



초기값이 없이 선언된 변수는 `undefined` 값을 가지며 `False` 와 같다.

|        | `undefined` | `null`  |
| ------ | ----------- | ------- |
| 수치   | `NaN`       | 0       |
| 불리언 | `False`     | `False` |



### 함수



```javascript
함수 선언식
function checkGuess() {
  alert('I am a placeholder');
}

함수 표현식
const func = function checkGuess() {
  alert('I am a placeholder');
}
```



다른 언어의 함수와 비슷한 기능을 하며 작성 방식은 위처럼 function 함수명() { 코드 } 의 형식을 가진다.

JavaScript에서는 함수를 정의할때 함수 선언식과 함수 표현식을 사용할 수 있다.

함수선언식은 함수명을 선언하고 끝인데 함수 표현식은 선언한 함수를 변수에 할당까지 해야한다.

그래서 함수 선언식은 익명함수가 불가능하지만 함수 표현식은 함수의 이름이 없는 익명 함수가 가능하다.

함수 선언식과 표현식은 호이스팅에서 차이가 있다.

**함수선언식으로는 호이스팅되지만 함수 표현식으로는 호이스팅이 되지 않는다.**

**매개변수의 갯수가 달라도 된다.**



### Arrow 함수



함수를 간단하게 정의하여 사용하는 함수이다.

```javascript
const arrow1 = function (name){
    return 'hello, ${name}'
}

이러한 함수가 있다면

 // 1. function 키워드 삭제

const arrow2 = (name) => {return 'hello, ${name}'}

// 2. 매개변수가 1개일 경우 ( ) 생략 가능.

const arrow3 = name => {return 'hello, ${name}'}

// 3. 함수 바디가 return 을 포함한 표현식 1개일 경우 {} & return 삭제

const arrow4	 = name => 'hello, ${name}'
```







### 데이터 구조 및 형



JavaScript 데이터형은 아래와 같이 구분된다.

- 원시 데이터 (primary data) : 변수에 해당하는 값이 담김. (값을 복사함)
  - `Boolean` 	
  - `null`
  - `undefined`
  - `Number`
  - ` BigInt` 
  - `String`
  - `Symbol`

- 참조 데이터, 객체 (reference data / Object) : 변수에 해당하는 객체의 참조값이 담김 (참조값을 복사함)
  - `function`
  - `array` 



JavaScript는 동적 형지정 언어다. 변수를 선언할때 따로 데이터 형을 지정할 필요 없이 필요한 경우에 자동으로 데이터의 형을 변환해준다.

```javascript
var ans = 31

ans = '데이터의 구조'

# 덧셈
x = 'The answer is ' + 31 // "The answer is 31"
```

이런 식으로 숫자가 있던 변수에 문자를 재할당해도 문제가 없다.

또한, 이러한 특성 때문에 문자와 숫자를 더해도 숫자가 자동으로 문자형으로 변환된다. (덧셈만)

만약 반대로 문자를 숫자로 변환하여 셈을 하려면 문자 앞에 `+` 를 붙인다.

```javascript
+'5' - +'2'
```





### 연산자



사칙연산은 `+ - * /`  연산자를 사용한다. ( `+` 는 문자열에도 사용 가능하다.)

파이썬처럼 `+=` 과 같은 연산자도 사용 가능하며 

`x++`  `x--` 과 같은 연산자는 1씩 증감을 하는 연산자이다.

비교연산자는 `===` `!==` `<` `>` 을 사용한다.

`==` 같은 경우 동등 비교 연산자로써 값을 비교하여 **`boolean` 값을 반환한다.**

논리연산자는 `&&` , `||` , `!`  을 사용한다.

삼항연산자는 `(조건문) ? (참일때) : (거짓일때);` 와 같은 형태로 쓰인다.

```javascript
(True ? 1:2) // 1
```





### 이벤트

이벤트란 브라우저를 통해 발생하는 여러 일 (버튼 클릭, 페이지 로딩, 비디오 재생 등)을 말한다.

이벤트 수신기가 특정 이벤트의 발생을 감지하고, 이벤트 처리기를 호출하면 이벤트 처리기가 이벤트에 반응한다.

```javascript
guessSubmit.addEventListener('click', checkGuess);
// checkGuess 는 함수

guessSubmit.addEventListener('click', function(){
    console.log(a)
})
// 이런 식으로 함수를 바로 작성하는 것도 가능하다.
```



위의 코드에서 `addEventListener(이벤트 유형, 함수)` 가 이벤트 수신기 메서드이다.

(함수에는 () 를 붙이지 않는다. )



이벤트 유형 참고 -> https://developer.mozilla.org/en-US/docs/Web/Events





### 반복문

JavaScript의 반복은 `for` ,  `do .. while` , `while` , `for .. in` ,  `for .. of`  등 다양한 반복문을 사용한다.



1. `for` 반복문

   어떤 특정한 조건이 거짓일때까지 계속 반복한다. 

   다음과 같은 형태로 쓸 수 있다.

   

   ```javascript
       for ([초기문]; [조건문]; [증감문])
         문장
         
       for (let i = 0; i < 6; i++){
           console.log(i) // 0,1,2,3,4,5
       }
   ```

   <br>

   <br>

2. `while` 반복문

   어떤 특정한 조건이 참이면 반복한다.

   파이썬의 while과 똑같다.

   ```javascript
   let i = 0
   while (i < 6){
       console.log(i)
       i+=1
   }
   ```

   <br>

   <br>

3. `for .. in` 반복문

   객체의 Key를 순회할 때 사용

   ```javascript
   const capitals = {
       korea: 'seoul',
       france: 'paris',
       USA: 'washington D.C'
   }
   
   for (let capital in capitals) {
       console.log(capital) // korea, france, USA
   }
   ```

   <br>

   <br>

   

4. `for .. of` 반복문

   반복가능한 객체를 순회하며 값을 꺼낼때 사용한다.

   

   ```javascript
   const fruits = ['apples', 'bananas', 'cherries'];
   for (const fruit of fruits) {
     console.log(fruit); // 
   }
   ```

   

### 조건문



JavaScript에서는 반복문으로 `if ... else` 문과 `switch` 문을 사용한다.

 `if ... else` 의 구조는 다음과 같다.

```javascript
if (condition) {
  statement_1;
} else {
  statement_2;
}
```

`condition` 이 `True` 이면 `statement_1`을 실행하고 `False` 이면 `statement_2` 를 실행한다.

파이썬의 `elif` 와 비슷한 기능으로  `else if` 를 사용할 수 있다.



- JavaScript에서 `False`로 판단하는 값:
  - `false`
  - `undefined`
  - `null`
  - `0`
  - `NaN`
  - `""` (빈 문자열)



`switch` 문의 구조는 다음과 같다.

```javascript
switch (expression) {
  case label_1:
    statements_1;
    break;
  case label_2:
    statements_2;
    break;
    …
  default:
    statements_default;
}
```



`switch` 문의 동작 순서

1. `expression` 표현식과 일치하는 `case`절을 찾아 실행한다.
2. `break` 문을 만나면 `switch`문을 종료하나 `break` 문이 없으면 **조건 여부에 상관없이** 해당 `case` 절 아래의 `case` 문을 실행한다.
3. 1의 조건에 해당하는 `case`절이 없으면 `default` 절을 실행한다.
4.  `default` 절이 없으면 `switch` 문 종료



### 예외 처리 명령문



`throw` 문을 사용하면 예외를 선언할 수 있고 여기서 선언된 예외를 `try ... catch` 문으로 처리할 수 있다.

예외가 아닌데 내가 사용할 함수에서는 예외로 처리하고 싶을 때 사용하기 위함이다.

`throw`문은 간단하게 다음과 같이 선언할 수 있으며 문자, 숫자, 함수 등 모든 것을 예외처리 가능하다.

```javascript
throw expression;
```



이렇게 선언된 예외를 `try ... catch`문으로 처리할 수 있는데, `try ... catch` 문의 구조는 다음과 같다.

```javascript
try {
    코드1
} catch(err){
    코드2
} finally {
    코드3
}
```



1. `try` 문 안의 `코드1` 이 실행된다.
2. `코드1` 문에서 오류가 발생할 경우 `catch`블록으로 이동하여 `err`에 에러 정보를 담는다.
3. `코드2`를 실행한다.
4. `try ... catch` 문의 모든 과정이 처리가 끝나면 `finally` 블록의 `코드3`을 실행한다.



### String



문자열 관련 주요 메소드로는 `includes` , `split` , `replace` , `trim`  등이 있다.

```javascript

// 1. includes : 특정 문자열이 존재 여부를 판단하여 True / False 를 반환
const str = 'A BCD EFG'
str.includes('BCD') // True 반환

// 2. Split : 문자열을 인자로 나눈 배열을 반환
str.split() // [ 'A BCD EFG' ]
str.split('') // ['A', '', 'B','C','D','','E','F','G']
str.split(' ') // ['A', 'BCD', 'EFG']

// 3. replace : 특정 문자열을 교체하여 반환
//    replaeceAll : 특정 문자열을 모두 교체하여 반환     

str.replace( 'BC' , 'ZX') // 'A ZXD EFG'

// 4. trim : 문자열의 좌우 공백을 제거하여 반환 (파이썬의 strip)

const str = '        hello       '

str.trim() // 'hello'
str.trimStart() // 'hello    '  문자열 시작 앞부분 공백을 제거
str.trimEnd() // '      hello'  문자열 시작 끝부분 공백을 제거
```





### 배열 (Array)



파이썬의 list와 비슷한 기능을 한다.

**그러나 인덱스에 음수를 사용할 수 없다.**

```javascript
// 배열의 길이를 나타내는 방법 : array.length
const numbers = [1,2,3,4,5]
console.log(numbers.length) // 5

// 역순으로 접근하는 방법 : array.length - 1
console.log(numbers[numbers.length-1]) // 5
```



- 배열에서 주로 사용하는 메소드 : `reverse` , `push & pop` , `unshift & shift` , `includes` , `indexOF` , `join` 

  

  ```javascript
  const numbers = [1,2,3,4,5]
  
  // 1. reverse : 배열의 순서를 반대로 정렬
  numbers.reverse()
  console.log(numbers) // [5,4,3,2,1]
  
  // 2. push & pop : 배열의 가장 뒤에서 요소를 추가 / 제거 (파이썬에서 append, pop과 유사)
  numbers.push(100)
  console.log(numbers) // [1,2,3,4,5,100]
  
  numbers.pop()
  console.log(numbers) // [1,2,3,4,5]
  
  // 3. unshift & shift : 배열의 가장 앞쪽에서 요소를 추가 / 제거
  
  numbers.unshift(100)
  console.log(numbers) // [100,1,2,3,4,5]
  
  numbers.shift()
  console.log(numbers) // [1,2,3,4,5]
  
  // 4. includes : 배열에 특정 값이 있는지 여부에 따라 True / False 반환
  
  // 5. indexOF : 배열에 특정 값을 확인해서 가장 빠른 인덱스를 반환 (없으면 -1 반환)
  
  // 6. join : 배열의 모든 요소를 연결하여 반환
  ```

  

- Spread operator (전개 연산자)

  `...` 으로 사용하며 배열을 전개할 수 있다.

  ```javascript
  const array = [1,2,3]
  const newarray = [0, ...array, 4]
  
  console.log(newarray) // [0,1,2,3,4]
  ```



- Array Helper Methods 

  배열을 순회하며 특정 로직을 수행하는 메소드 (파이썬의 map과 유사한 기능)

  메소드 호출시 인자로 callback 함수를 받는다.

  

  - forEach : 배열의 각 요소에 대해 콜백함수를 한번씩 실행
  - map : 콜백 함수의 반환값을 요소로 하는 새로운 배열을 반환
  - filter : 콜백 함수의 반환값이 참인 요소들의 배열을 반환
  - reduce : 콜백 함수의 반환값들을 acc에 다 더해서 반환
  - find : 콜백 함수의 반환값이 참이면 해당 요소를 반환
  - some : 배열의 요소 중 하나라도 판별 함수를 통과하면 참을 반환
  - every : 배열의 모든 요소가 판별 함수를 통과하면 참을 반환

  

  

  

