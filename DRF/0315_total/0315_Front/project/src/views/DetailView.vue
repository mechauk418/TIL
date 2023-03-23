<template>
  <div>
    <h1 style="margin-bottom:3rem"> Board </h1>
    <div class="article_box">
      <div class="title"><p>{{article_title  }}</p></div>
      <div class="writer"><p> 작성자 :  {{ article_user }}</p> </div>
      <div class="content"> <p> 내용 : {{ article_content }}</p></div>
      <p> 추천수 : {{ article_like }}</p>
      <div class="div_btn">
        <button @click="like" class="btn"> 좋아요 </button>
        <router-link to="/articles"> <button class="bnt"> 목록 </button></router-link>
      </div>
    </div>
  </div>

</template>

<script>
import testaxios from '../../src/axios'
import axios from 'axios'
// @ is an alias to /src

export default {
  data() {
    return {
      article:null,
      article_title:null,
      article_content:null,
      article_user:null,
      article_like:null,
    }
  },
  mounted() {
    axios({
      method: "GET",
      url: 'http://localhost:8000/articles/' + this.$route.params.pk + '/'
    })
    .then(res =>{
      console.log(res.data)
      this.article = res.data
      this.article_title = res.data.title
      this.article_content = res.data.content
      this.article_user = res.data.user
      this.article_like = res.data.like_article.length
    })

  },
  methods: {
    like() {
      testaxios.post('http://localhost:8000/articles/' + this.$route.params.pk + '/like/', {} ,{headers:
          {Authorization : 'Bearer ' + localStorage.getItem('access_token')}
        })
      .then(
        axios({
          method: "GET",
          url: 'http://localhost:8000/articles/' + this.$route.params.pk + '/'
        })
        .then(res =>{
          this.article_like = res.data.like_article.length
        })
      )
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
</style>