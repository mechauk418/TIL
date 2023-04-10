<template>
  <div>
    <h1 style="margin-bottom:3rem"> Board </h1>
    <div class="article_box">
      <div class="title"><p>{{article_title  }}</p></div>
      <div class="writer"><p> 작성자 :  {{ article_user }}</p> </div>
      <div class="content"> <p> 내용 : {{ article_content }}</p></div>
      <div v-for="image in article_image" :key="image">
        <img :src="image.image_original" v-if="image.image == null">
        <img :src="image.image" v-else>
      </div>
      <p> 추천수 : {{ article_like }}</p>
      <div class="div_btn">
        <button @click="like" class="btn"> 좋아요 </button>
        <button @click="delete_article" class="btn" v-show="article_user == login_user"> 삭제 </button>
        <router-link to="/articles"> <button class="bnt"> 목록 </button></router-link>
      </div>
      <div v-for="(comment,index) in comments_list" :key="index" style="margin:2rem 0">
        <div class="comment">
          <div class="comment_user">
            <p> {{comment.user  }} </p>
          </div>
          <div class="comment_content">
            <p> {{comment.content  }} </p>
          </div>
        </div>
      </div>
      <form v-show="login_user" @submit.prevent="create_comment" class="myform">
        <div class="input-wrap">
          <input type="text" id="comment" v-model="comments_content" class="my-shadow no-kg-font" autocomplete="off" />
          <button type="submit" class="my-shadow no-kg-font" style="cursor:pointer;">작성</button>
        </div>
      </form>
    </div>

  </div>

</template>

<script>
import testaxios from '../../src/axios'
import axios from 'axios'
// @ is an alias to /src
import loginStore from '../store/index'
export default {
  data() {
    return {
      article:null,
      article_title:null,
      article_content:null,
      article_user:null,
      article_like:null,
      login_user : null,
      article_image : [],
      comments_content:null,
      comments_list : [],
    }
  },
  mounted() {
    if (loginStore.state.loginStore.isLogin) {
      this.login_user = loginStore.state.loginStore.userInfo.email
    }
    axios({
      method: "GET",
      url: 'http://localhost:8000/articles/' + this.$route.params.pk + '/',
      withCredentials:true
    })
    .then(res =>{
      this.article = res.data
      this.article_title = res.data.title
      this.article_content = res.data.content
      this.article_user = res.data.user
      this.article_like = res.data.like_article.length
      this.article_image = res.data.images
      this.comments_list = res.data.comments
    })

  },
  methods: {
    like() {
      testaxios.post('http://localhost:8000/articles/' + this.$route.params.pk + '/like/')
      .then(
        axios({
          method: "GET",
          url: 'http://localhost:8000/articles/' + this.$route.params.pk + '/'
        })
        .then(res =>{
          this.article_like = res.data.like_article.length
        })
      )
    },
    delete_article() {
      testaxios.delete('http://localhost:8000/articles/' + this.$route.params.pk + '/')
      .then(res => {
        this.$router.push('../articles')
      })
    },
    create_comment() {
      const comment_data = {
        'content': this.comments_content
      }
      testaxios.post('http://localhost:8000/articles/' + `${this.$route.params.pk}/comment/`, comment_data)
          .then((response) => {
            axios({ // 댓글 작성해서 리스트를 다시 불러옴
              method: 'GET',
              url: 'http://localhost:8000/articles/' + this.$route.params.pk + '/',
              headers: {
                Authorization: 'Bearer ' + localStorage.getItem('access_token')
              }
            })
            .then(res => {
              this.article = res.data
              this.article_title = res.data.title
              this.article_content = res.data.content
              this.article_user = res.data.user
              this.article_like = res.data.like_article.length
              this.article_image = res.data.images
              this.comments_list = res.data.comments
            })
            .catch(response => {
            })
          })
    }

  },
}
</script>

<style scoped>

.article_box {
  border: 1px solid black;
  border-radius: 1cm;
  width:70%;
  padding: 2rem;
  margin: auto;
}

.title {
  text-align: left;
  font-size : 1.5rem;
  margin-left: 1.5rem;
  margin-bottom: 2rem;
}

.writer {
  text-align: right;
  font-size : 1rem;
  margin-bottom: 3rem;
}

.content {
  text-align: left;
  font-size : 1rem;
  margin-left: 1.5rem;
  margin-bottom: 3rem;
}


.btn{
  margin:0.2rem
}

.input-wrap {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.input-wrap>input {
  width: 90%;
  height: 33px;
  border-radius: 3px;
  border: 0;
  padding: 0 20px;
  font-size: 16px;
  text-align: center;
}

.input-wrap>button {
  width: 90px;
  height: 33px;
  margin-left: 15px;
  background-color: rgb(73, 73, 73);
  color: white;
  font-size: 16px;
  border: 0;
  border-radius: 3px;
}

.myform {
  margin-bottom : 0.5rem;
  margin-top : 0.5rem;

}

.comment {
  display : flex;
}

.comment_user{
  border-right: solid 1px black;
  padding: 0.5rem;
  margin: 0.5rem;
}

.comment_content{
  border-right: solid 1px black;
  padding: 0.5rem;
  margin: 0.5rem;
  width : 70%;
  text-align: left;
}

</style>