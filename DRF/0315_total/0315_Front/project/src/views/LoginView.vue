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

  },
  methods:{
    login () {
      const logindata = {}
      logindata.email = this.email
      logindata.password = this.password
      axios.post('http://localhost:8000/accounts/auth/token/',logindata)
      .then(res => {
        console.log(res.data)
      })
      this.$store.dispatch('login',logindata)

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
