# vue.js



1. Node.js 설치 (npm 쓰기위해서)

2. 뷰 설치

3. window 실행 정책 변경 

   ```
   https://bono915.tistory.com/entry/VueJS-Windows-Terminal-%EC%8B%A4%ED%96%89-%EC%98%A4%EB%A5%98-vue-%EC%9D%B4-%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%97%90%EC%84%9C-%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8%EB%A5%BC-%EC%8B%A4%ED%96%89%ED%95%A0-%EC%88%98-%EC%97%86%EC%9C%BC%EB%AF%80%EB%A1%9C-%EC%97%90-%EB%8C%80%ED%95%9C-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95
   ```








## Databinding

1. **문자열**

   ```vue
   {{string}}
   ```

   <br><br>

2. **HTML**

   ```vue
   <template>
   	<div v-html="HTML이름"></div>
   </template>
   ```

   <br><br>

3. **Input**

   ```vue
   <template>
   	<input type="text" v-model="userID">
   	<input type="text" v-model.number="userID"> // 문자형을 숫자형으로 나타냄
   </template>
   <script>
   export default {
     components: {},
     data() {
       return {
         userID: 'inputvalue'
       }
     },
   </script>
   ```

   양방향 databinding임

   (input 값에 따라 실시간으로 `userID`도 변함)

   <br><br>

4. **Select**

   ```vue
   <template>
   	<select v-model="userID">
           <option value=""></option>
           <option value="02">서울</option>
           <option value="051">부산</option>
       </select>
   </template>
   <script>
   export default {
     components: {},
     data() {
       return {
         userID: 'selectvalue'
       }
     },
   </script>
   ```

   마찬가지로 양방향 databinding임

   <br>

   <br>

5. **Checkbox**

   ```vue
   <template>
     <div>
       <div>
           <input type="checkbox" name="" id="html" value="HTML" v-model="userId" />
           <label for="html">HTML</label>
       </div>
       <div>
           <input type="checkbox" name="" id="css" value="CSS" v-model="userId" />
           <label for="css">CSS</label>
       </div>
       <div>
           <input type="checkbox" name="" id="js" value="JS" v-model="userId" />
           <label for="js">JS</label>
       </div>
     </div>
     <div>{{userId}}</div>
   </template>
   <script>
   export default {
     components: {},
     data() {
       return {
         userId: []  // 반드시 배열로
       }
     }
   }
   </script>
   
   ```

   checkbox는 양방향으로 value를 바꿀 수 있는게 아니고 `checked` 속성을 True/False을 양방향으로 바꿔준다.

   <br><br>

6. **Radio**

   ```vue
   <template>
     <div>
       <div>
           <input type="radio" name="" id="html" value="HTML" v-model="userId" />
           <label for="html">HTML</label>
       </div>
       <div>
           <input type="radio" name="" id="css" value="CSS" v-model="userId" />
           <label for="css">CSS</label>
       </div>
       <div>
           <input type="radio" name="" id="js" value="JS" v-model="userId" />
           <label for="js">JS</label>
       </div>
     </div>
     <div>{{userId}}</div>
   </template>
   <script>
   export default {
     components: {},
     data() {
       return {
         userId: ''  // 반드시 문자로 (체크박스는 다수 선택 가능, 라디오는 선택 1개만)
       }
     }
   }
   </script>
   ```

   <br>

   <br>

7. **Attribute**

   ```vue
   <template>
     <div>
       <input type="text" v-bind:value="sampleData" readonly>
       <input type="text" :value="sampleData" readonly>
     </div>
     <input type="search" v-model="text11">
     <button :disabled="text11 ===''"> 조회 </button>
   </template>
   <script>
   
   export default {
     components: {},
     data() {
       return {
         sampleData: 'dasf',
         text11: ''
       }
     },
     setup() {},
     created() {},
     mounted() {},
     unmounted() {},
     methods: {}
   }
   </script>
   
   ```

   `v-bind` 로 HTML 속성을 단방향으로 고정시켜줌

   `v-bind:attribute=""` 인데 `:attribute=""` 로 줄여쓸 수 있다.

   ```vue
   <input type="search" v-model="text11">
   <button :disabled="text11 ===''"> 조회 </button>
   ```

   `input`의 값을 `text11`이라는 데이터랑 바인딩했고 이 값이 비어있으면 `button` 의 `disabled` 를 활성화시켜준다. (속성을 바인딩해준다.)

   <br>

   <br>

8. **list(v-for)**

   ```vue
   <template>
     <div>
       <div>
         <select name="" id="">
           <option :value="city.code" :key="city.code" v-for="city in sampleData">{{city.title}}</option>
         </select>
       </div>
     </div>
   </template>
   <script>
   
   export default {
     components: {},
     data() {
       return {
         sampleData: [
           { title: '서울', code: '02' },
           { title: '부산', code: '05' },
           { title: '제주', code: '032' }
         ]
       }
     },
     setup() {},
     created() {},
     mounted() {},
     unmounted() {},
     methods: {}
   }
   </script>
   ```

   `v-for` 은 반드시 `key`를 입력해주어야한다. (`key` 는 고유한 값으로 )

   만약 고유한 `key`가 없다면 아래처럼 입력한다

   ```vue
   <tr :key="i" v-for="(drink, i) in sample"> </tr>
   // 여기서 i는 인덱스 번호
   ```

   <br>

   <br>

9. **class**

   ```vue
   <template>
     <div>
       <div :class="{ 'text-red' : hasError, active: isActive }"> 클래스 바인딩 </div>
     </div>
   </template>
   <script>
   
   export default {
     components: {},
     data() {
       return {
         isActive: true,
         hasError: false
       }
     },
     setup() {},
     created() {},
     mounted() {},
     unmounted() {},
     methods: {}
   }
   </script>
   
   ```

   class의 key가 true 이면 그 클래스가 활성화되는 개념이다.

   받아오는 데이터에 따라 클래스 속성을 변경시켜주는 엄청 유용한 기능이다.

   <br>

   <br>

# Event

1. click

   





2. Change