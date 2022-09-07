

# CSS



### BOX MODEL



CSS는 문서의 레이아웃을 계산할 때, BOX MODEL에 따라 각각의 요소를 사각형 박스로 표현한다.



![](.\images\0831 image1.jpg)

모든 CSS이 위와 같은 방식으로 동작하며 이 BOX의 성질은 `display` 값이나 치수, 외형 등 설정에 따라 다르게 동작한다.  그러나 컨텐츠의 내용이 BOX의 범위를 벗어나면 오버플로우가 발생하므로 BOX를 잘 설정해야하며, `max - content` 와 같은 명령어로 컨텐츠 크기에 맞게 유동적으로 조절하는 방법도 있다.



BOX는 아래와 같은 영역으로 구성되어 있다.

![](.\images\0831 image2.jpg)



- Margin : 테두리와 인접 요소 사이의 공간이며 눈에 보이지 않는다.
- Border : 내용을 감싸는 테두리
- Padding : 내용과 테두리 사이의 공간이며 눈에 보이지 않는다.
- Content : 글이나 그림과 같은 BOX의 실제 내용 



네 개의 박스 영역 모두 CSS를 통해 치수나 성질 등을 원하는 대로 조절할 수 있다.



### 선택자(Selector)

```css
p{
 color :red;
}
```

css에서 특정 요소를 선택하여 스타일을 적용시킬 수 있게 하는 것을 선택자라고 한다.

위의 예시에서 p 가 선택자에 해당하는 부분이다.

|               | 패턴     | 의미                                      |
| ------------- | -------- | ----------------------------------------- |
| 전체 선택자   | *        | HTML 페이지 내부의 모든 태그 선택         |
| 태그 선택자   | tag      | 태그명이 tag 인 모든 태그 선택            |
| 클래스 선택자 | .myClass | 클래스 속성값이 myClass 인 모든 요소 선택 |
| id 선택자     | #myid    | id 속성값이 myid인 모든 요소 선택         |



대표적인 4개의 선택자 외에도 속성 선택자, 복합 선택자 등 더 세부적인 선택이 가능한 선택자가 있다.



### CASCADE



CASCADE는 여러 CSS 규칙이 HTML의 요소에 적용되는 충돌을 피하기 위한 알고리즘이다.

```css
button {
  color: red;
}

button {
  color: blue;
}
```



이렇게 button 태그에 color에 대한 두가지 규칙이 입력되었을때에 사용하는 알고리즘이다.

CASCADE 알고리즘은 3단계로 나누어져있다.

1. 중요성 : !important 선언은 최우선으로 작동한다. 그러나 코드가 꼬일 가능성이 있으므로 사용에 주의한다.

2. 특성 : 선택자의 우선권에 대한 척도

   - 인라인 (1000점) > id (100점)  > class, 속성, pseudo-class (10점) > 요소, pseudo-element (1점) > 전체선택 (0점)

3. CSS 파일 로딩 순서 : 중요성, 특성 모두 없거나 특성이 동일한 점수일때는 순서대로 적용되어 가장 마지막 스타일이 적용된다.

   

### Inheritance

상속은 부모 요소의 특성을 자식 요소에게 적용시키는 것이다.

- 상속 되는 특성  : 
  - TEXT 관련 특성, opacity, visibility
- 상속되지 않는 특성 :
  - BOX MODEL 관련 특성, Position 관련 특성



### FLEXBOX



- **justify-content** : 가로축을 기준으로 좌우 정렬한다.

  - `flex-start`: 요소들을 컨테이너의 왼쪽으로 정렬한다.

  - `flex-end`: 요소들을 컨테이너의 오른쪽으로 정렬한다.

  - `center`: 요소들을 컨테이너의 가운데로 정렬한다.

  - `space-between`: 요소들 사이에 동일한 간격을 둔다.

  - `space-around`: 요소들 주위에 동일한 간격을 둔다.

- **align-items** : 세로축을 기준으로 상하 정렬한다.

  - `flex-start`: 요소들을 컨테이너의 꼭대기로 정렬한다.

  - `flex-end`: 요소들을 컨테이너의 바닥으로 정렬한다.

  - `center`: 요소들을 컨테이너의 세로선 상의 가운데로 정렬한다.

  - `baseline`: 요소들을 컨테이너의 시작 위치에 정렬한다.

  - `stretch`: 요소들을 컨테이너에 맞도록 늘린다.

- **flex-direction** : 정렬할 방향을 지정한다.

  - `row`: 요소들을 텍스트의 방향과 동일하게 정렬한다.

  - `row-reverse`: 요소들을 텍스트의 반대 방향으로 정렬한다.

  - `column`: 요소들을 위에서 아래로 정렬한다.

  - `column-reverse`: 요소들을 아래에서 위로 정렬한다.

    ( **justify-content** 와 **flex-direction** 을 같이 사용할 경우 start와 end의 방향도 바뀐다.)



- order : flex 속성의 순서를 지정한다. (기본값 0)
- align-self : 지정된 `align-items` 값을 무시하고 Flex 요소를 세로선 상에서 정렬한다.

- **flex-wrap** : flex 속성을 한줄 또는 여러줄에 걸쳐 정렬한다.

  - `nowrap`: 모든 요소들을 한 줄에 정렬한다.
  - `wrap`: 요소들을 여러 줄에 걸쳐 정렬한다.
  - `wrap-reverse`: 요소들을 여러 줄에 걸쳐 반대로 정렬한다. 

- **flex-flow** : **flex-direction** + **flex-wrap** 이다.

  - `<flex-direction> <flex-wrap>` : 각각의 인자를 받는다. (ex. flex-flow : column wrap;)

- **align-content** : 세로선 상에 여분의 공간이 있는 경우 Flex 컨테이너 사이의 간격을 조절한다.

  - `flex-start`: 여러 줄들을 컨테이너의 꼭대기에 정렬한다.
  - `flex-end`: 여러 줄들을 컨테이너의 바닥에 정렬한다.
  - `center`: 여러 줄들을 세로선 상의 가운데에 정렬한다.
  - `space-between`: 여러 줄들 사이에 동일한 간격을 둔다.
  - `space-around`: 여러 줄들 주위에 동일한 간격을 둔다.
  - `stretch`: 여러 줄들을 컨테이너에 맞도록 늘린다.

  