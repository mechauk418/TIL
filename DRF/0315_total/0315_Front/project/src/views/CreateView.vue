<template>
  <div>
    <div>
      <label for="title">제목</label>
      <input type="text" id="title" v-model="title" class="input-text">
    </div>
    <div>
      <label for="content">내용</label>
      <input type="text" id="content" v-model="content" class="input-text">
    </div>
    <div>
      <input multiple @change="OnArticleImage()" ref="ArticleImage" type="file" />
    </div>
    <div>
      <button @click="create"> 글 쓰기 </button>
    </div>
  </div>
    
  </template>
  
  <script>
import testaxios from '../../src/axios'
import loginStore from '../store/index'

  export default {
    data () {
      return {
        title: '',
        content: '',
        islogin:'',
        images:'',
        images2:'',
      }
    },
    mounted() {
      this.islogin = loginStore.state.loginStore.isLogin
      if (this.islogin) {

      } else {
        alert('로그인해주세요')
        this.$router.go(-1)
      }
    },
    methods:{
      create () {
        const createdata = new FormData()
        // createdata.title = this.title
        // createdata.content = this.content
        // createdata.images = this.images
        createdata.append('title',this.title)
        createdata.append('content',this.content)
        for (const i of this.images) {
          createdata.append('image',i)
          console.log(i)
        }
        console.log(createdata)
        testaxios({
          method: 'POST',
          url: 'http://localhost:8000/articles/', 
          data: createdata,
          withCredentials : true,
          headers:{
            'Content-Type': 'multipart/form-data'
          }
          
        })
        .then(response => {
          const article_pk = response.data.pk
          // window.location.href="http://localhost:8080/detail/" + article_pk +'/'
        })
        .catch(error =>{
          console.log(error)
        })
      },
      OnArticleImage() {
        this.images = this.$refs.ArticleImage.files
      }
    }
  }
  </script>
  
  <style>
  
  </style>