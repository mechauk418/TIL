<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/articles">Article</router-link> |
    <router-link to="/login" v-if="logincheck==false">login |</router-link>
    <a @click="logoutplz()" v-if="logincheck">로그아웃  | </a>
    <router-link to="/signup" v-if="logincheck==false"> SignUp  |</router-link>
    <a @click="refresh()"> Refresh  |</a>  </nav>
  <router-view/>
</template>

<script>
import axios from 'axios'
import loginStore from './store/index'
export default {
  data () {
    return {
      logincheck: '',
    }
  },
  mounted() {
    this.logincheck = loginStore.state.loginStore.isLogin
  },
  methods:{
    logoutplz () {
      this.$store.dispatch('logouttest_act')
    },
    refresh () {
      axios({
        method : 'POST',
        url : 'http://localhost:8000/accounts/auth/token/refresh/',
        withCredentials : true
      })
      .then(res=>{
        console.log(res)
      })

    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.my-shadow {
  box-shadow: 2px 2px 10px rgba(133, 133, 133, 0.378);
}

</style>
