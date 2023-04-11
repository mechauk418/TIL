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
    <div class="social-container">
      <img @click="googlelogin()" src='data:image/png;base64,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' class="kakao_btn my-shadow">
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
    },
    googlelogin() {
      const SOCIAL_AUTH_GOOGLE_CLIENT_ID= '319698127254-ci76jba5ro0oj9ugs7qhfq3a5sp6irrv.apps.googleusercontent.com'
      const GOOGLE_CALLBACK_URI= 'http://localhost:8080/login'
      const scope = "https://www.googleapis.com/auth/userinfo.email"
      window.location.href = `https://accounts.google.com/o/oauth2/v2/auth?client_id=${SOCIAL_AUTH_GOOGLE_CLIENT_ID}&response_type=code&redirect_uri=${GOOGLE_CALLBACK_URI}&scope=${scope}`
    },
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
