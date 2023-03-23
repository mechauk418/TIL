import axios from 'axios'
import store from '../store'

const testaxios = axios.create()
testaxios.defaults.withCredentials = true
testaxios.interceptors.response.use(
  function (response) {
    // 200대 response를 받아 응답 데이터를 가공하는 작업
    return response
  },
  async (error) => {
    console.log('interceptors 시작')
    const {
      config,
      response: { status }
    } = error
    if (status === 401) {
      if (error.response.data.detail === '이 토큰은 모든 타입의 토큰에 대해 유효하지 않습니다') { // 응답이 영어면 영어로 수정해서 사용한다.
        const originalRequest = config
        console.log('여기')
        await store.dispatch('refreshtt')
        const newAccessToken = localStorage.getItem('access_token')
        axios.defaults.headers.common.Authorization = `Bearer ${newAccessToken}`
        testaxios.defaults.headers.common.Authorization = `Bearer ${newAccessToken}`
        originalRequest.headers.Authorization = `Bearer ${newAccessToken}` // 새로운 토큰을 헤더에 담아줌
        // 401로 요청 실패했던 요청 새로운 accessToken으로 재요청
        return axios(originalRequest)
      }
    }
    return Promise.reject(error)
  }
)
export default testaxios
