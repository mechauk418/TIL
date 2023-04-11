import testaxios from '@/axios'
import router from '@/router'
import axios from 'axios'
const loginStore = {
  state: {
    userInfo: null,
    isLogin: false,
  },
  mutations: { // 로그인 상태를 변경해주는 코드
    loginSuccess: function (state, payload) {
      state.userInfo = payload
      state.isLogin = true
    },
    loginError: function (state) {
      state.userInfo = null
      state.isLogin = false
    },
    logoutTest: function (state) {
      state.userInfo = null
      state.isLogin = false
      localStorage.removeItem('access_token')
      localStorage.removeItem('vuex')
      testaxios.defaults.headers.Authorization = null
    },
  },
  actions: {
    login (dispatch, loginObj) {
      axios
        .post('http://localhost:8000/accounts/login/', loginObj, { withCredentials : true}) // 로그인 URL로 ID, PW를 보냄
        .then((res) => {
          console.log(res.data)
          const token = res.data.access_token
          localStorage.setItem('access_token', token) // 토큰을 저장함
          axios.defaults.headers.common.Authorization = `Bearer ${token}`
          this.dispatch('getMemberInfo') // 유저 정보를 가져오는 actions 호출
        })
        .catch((error) => {
          const err = error.response.data
          try {
            if(err.email[0] == '이 필드는 null일 수 없습니다.') {
              alert('이메일을 입력하세요.')
            }
          } catch(e) {}
          try {
            if(err.password[0] == '이 필드는 null일 수 없습니다.') {
              alert('비밀번호를 입력하세요.')
            }
          } catch(e) {}
          try {
            if(err.non_field_errors[0] == '주어진 자격 증명으로 로그인이 불가능합니다.') {
              alert('이메일 혹은 비밀번호가 틀렸습니다.')
            }
          } catch(e) {}
        })
    },
    kakaologin(dispatch, code){
      axios.get(`http://localhost:8000/accounts/kakao/callback/?code=${code}`, {withCredentials:true})
      .then((response) => {
        console.log(response)
        const token = response.data.access_token
        localStorage.setItem('access_token', token) // 토큰을 저장함
        axios.defaults.headers.common.Authorization = `Bearer ${token}`
        this.dispatch('getMemberInfo') // 유저 정보를 가져오는 actions 호출
      })
      .catch((err)=>{
        console.log(err)

        // alert('소셜 로그인 오류. 관리자에게 문의하세요.')
      })
    },
    googlelogin(dispatch, code){
      axios.get(`http://localhost:8000/accounts/google/callback/?code=${code}`, {withCredentials:true})
      .then((response) => {
        const token = response.data.access_token
        localStorage.setItem('access_token', token) // 토큰을 저장함
        axios.defaults.headers.common.Authorization = `Bearer ${token}`
        this.dispatch('getMemberInfo') // 유저 정보를 가져오는 actions 호출
      })
      .catch((err)=>{

      })
    },

    logouttest_act ({ commit }) { // 로그아웃 actions
      axios({
        method:'POST',
        url:'http://localhost:8000/accounts/logout/',
        withCredentials:true
      })
      commit('logoutTest')
      window.location.href="http://localhost:8080/"
    },
    getMemberInfo ({ commit }) { // 토큰으로 유저 정보를 받아오는 코드
      const token = localStorage.getItem('access_token') // 저장된 access 토큰을 가져옴
      const config = {
        headers: {
          Authorization: 'Bearer ' + token
        }
      }
      axios
        .get('http://localhost:8000/accounts/user/', config) // 가져온 토큰을 헤더에 Authorization 로 담아서 요청을 보냄
        .then((response) => {
          // console.log(response)
          const userInfo = {
            pk: response.data.pk,
            email: response.data.email,
          } // 유저 정보를 받아옴
          commit('loginSuccess', userInfo) // mutations 호출
          window.location.href="http://localhost:8080/"
          // router.push('logincheck')
        })
        .catch((err) => {
          // alert('이메일과 비밀번호를 확인하세요.')
          console.log(err)
        })
    }
  }
}

export default loginStore
