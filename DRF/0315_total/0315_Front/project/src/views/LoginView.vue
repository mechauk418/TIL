<template>
<div class="login-container my-shadow">
  <div class="myform">
    <h1 class="form-title">로그인</h1>
    <div class="input-wrap">
      <label for="email">아이디</label>
      <input type="email" id="email" v-model="email" class="input-text">
    </div>
    <div class="input-wrap">
      <label for="password">비밀번호</label>
      <input type="password" id="password" v-model="password" class="input-text">
    </div>
    <div style="max-width: 350px; margin: 0 auto;">
      <button @click="login" class="form-btn my-shadow">로그인</button>
    </div>
    <div class="social-text">
      <hr>
      <div class="alert-text" style="margin: 10px;">소셜로 로그인하기</div>
      <hr>
    </div>
    <div class="social-container">
      <img @click="kakaologin()" src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAnFBMVEX/3AAAAB//4gD/4AD/5AD/3gD/4QAABh8ACB//5gAABx8AAB792gARFB8ACx99bRhcUhnKrwxzZRfewAkeHh0HDh+kjxLuzgXStgtZTxrDqQ4oJh331QOqlBGBcRa9pA9pXRiMehU8NxwbHB4TFh5QRxpJQhu4nxCOfBU1MRzy0QavmBGXgxR4aRgxLRxAOhskIx3jxAhsXxhNRRpm5ptnAAAD50lEQVR4nO3Y2XajOhAFUJekAmSDZwbbGI/xnMHJ///bLQk7nYdOnnqgc89+sTFZLA4llURaLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD4f2Ctvzz9p+7jt+HT9Px5RG3y+A/ezG+herQ2n53UxYxO/3oVVRXtPk+4ICq/QcK3756w/fBVws4/n9D07gl/JHn/pvcUfoOE4cQnDE7KfXBgLGurfC5J2K0Tqrrfsg6UUR96r6w1uuGPQBL2XcJgQHO5VS7P/Q7R+OCDBedO6r+YYeHyay6yqncp1C2U1qPFfnAyjc5oHn1CnafJJuaW6pPTCZ/kwCVMXEKTEQ10S0/H/iz164FsBkd/+Fh+uWn4y8wwXJoW83PSzeU+9XQ5zctTRuFKihbMQxc7KChdusdQ0PNqPpeH0HNlN2dKx71Dn7ovTZ6s5tUltI8RDQJ3zEozs626T66GWTiOmU9JsvZV46tSQWBXqVtD+ErJJDbK3vI3lSR8NVINyj7epB74hbBOqHd1fVu3Lss5UaFlBqdJPUnnIV2bW0SzDId2ROGjvf3AWiklv/iEl/ZLy/ZCKoL730uBdWtDC0nYSSv/VLhMoyz46dWbwPTDXrxNJveer8r9papWw8QlVJf2LJD6nm/1ZWXy0eg6GktCqWS4rytrnru95g5TMwmrnLb3hGZed0sak+usl+gpps3R1ieZLxt/ckNTWSh8f62vEQ2bndAuqF2PUj0lWl3LspRPl/AQPRlZ9Vf1EFYTWRmy8znzCQs/G/01+u3HBid8CytlL7dOYx6ioZWpJuv/LeFR29VtmMouNRrZIFDxVqrHP2pod1GTR+nOrXxmkrpuwjwjP7ekl3ZcwlW01hw8JDTSbpPe6bticpm4hCVF83qBaY27B/V3Y3zBrkO5O45n21RWBEk4l/Vf2yy6J5Tc5Xi7kRdh89rx002XqauePSYP9dAu3qvZRPbYvsjz17J8r5lNPz3mgS5eadN1Cavo2e1lRpTsApYxO2Ml7bSfuBnomuzCSon1Oplxc9dD+0J+hCl52a2Uy0Kzrnzd1gnD3W1/Fg5d90zW2UXazYvvMfqtS4fRdbFOm1xCaSbVwt+eXQ1lRqlil3Zeele7HvuEnWffQmyPLnJ4rvfd+dIn5LjeplO4aG6fEer+uqcDN9K0KU/aMCt3xHFZ76k5LlwIle/n+9zIO5P//xSrolouX7OyuRuan/o4pfh+wO9vwG5rwPcdkFbGmKC5cxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAfrn/ADCaOc2HgoxfAAAAAElFTkSuQmCC' class="kakao_btn my-shadow">
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      email: '',
      password: '',
    }
  },
  mounted() {
    const urlSearch = new URLSearchParams(location.search);
    const code = urlSearch.get('code')
    const scope_test = urlSearch.get('scope')
    console.log(code)
    console.log(scope_test)
    if (code != null && scope_test == null) {
      this.$store.dispatch('kakaologin', code)
    } else if (code != null && scope_test) {
      this.$store.dispatch('googlelogin', code)
    } else {
    }
  },
  methods:{
    login () {
      const logindata = {}
      logindata.email = this.email
      logindata.password = this.password
      this.$store.dispatch('login',logindata)
    },
    kakaologin() {
      const KAKAO_REST_API_KEY ='17927c83c8f77eef6c83ef6dd7ff221c'
      const KAKAO_REDIRECT_URI = 'http://localhost:8080/login'
      window.location.href = `https://kauth.kakao.com/oauth/authorize?client_id=${KAKAO_REST_API_KEY}&redirect_uri=${KAKAO_REDIRECT_URI}&response_type=code&scope=account_email`
  }
}
}
</script>

<style scoped>
.login-container {
  max-width: 550px;
  margin: 20vh auto 0;
}
.form-title {
  text-align: center;
  margin-bottom: 70px;
  font-size: 23px;
  font-weight: 500;
  margin-top: 0;
}
.input-wrap {
  max-width: 350px;
  margin: 20px auto;
  display: flex;
  justify-content: space-between;
}
.myform {
  padding: 10vmin 15px;
}
.input-wrap>label {
  width: 95px;
  text-align: start;
}
.input-text {
  max-width: 250px;
  padding: 7px 10px;
  border: 1px solid rgb(180, 180, 180);
  border-radius:  3px;
  font-size: 15px;
}
.form-btn {
  display: block;
  width: 100%;
  background-color: pink;
  border: 0;
  padding: 7px 0;
  margin-top: 40px;
  border-radius:  3px;
  font-family: 'Pretendard-Regular';
  font-size: 15px;
  transition: 0.14s all ease-in;
}
.form-btn:hover {
  background-color: #FF719B;
  font-family: 'Pretendard-Regular';
  color: white;
  transition: 0.14s all ease-in;
}
.google_btn {
  width: 350px;
  border: 0;
  padding: 7px 0;
  border-radius:  3px;
  transition: 0.14s all ease-in;
}
.kakao_btn {
  width: 350px;
  border: 0;
  padding: 7px 0;
  border-radius:  3px;
  transition: 0.14s all ease-in;
}
.alert-text {
  display: block;
  font-size: 15px;
  color: gray;
  margin: 15px 0;
}
.social-text {
  display: flex;
  align-items:center;
  justify-content: center;
  margin: 40px 0 20px;
}
.signup-text:hover {
  color: black;
}
.social-text>hr {
  color: lightgray;
  width: 20%;
  margin: 0;
}
.social-container {
  display: flex;
  justify-content: center;
}
.social-container>img {
  width: 60px;
  height: 60px;
  object-fit: cover;
  border-radius: 50%;
  padding: 0;
  margin: 0 15px;
}
@media (max-width: 600px) {
  .social-container>img {
    width: 50px;
    height: 50px;
  }
}
@media (max-width: 380px) {
  .input-wrap {
    margin: 20px auto;
    display: flex;
    flex-direction: column;
    align-items: start;
    justify-content: center;
  }
  .input-wrap>label {
    margin-bottom: 5px;
  }
  .input-wrap>input {
    max-width: 100%;
  }
}
</style>
