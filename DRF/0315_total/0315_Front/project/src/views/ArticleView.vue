<template>
  <div>
    <h1> Board </h1>
    <br><br>
    <div class="container" style="width:90%; margin:0 auto;">
      <table style="margin : 0 auto; width:80%;">
        <tr>
          <th> 번호 </th>
          <th style="width:50%"> 제목 </th>
          <th> 작성자 </th>
          <th> 작성일 </th>
          <th> 조회수 </th>
          <th> 추천수 </th>
        </tr>
        <tr v-for="(article, index) in articles" :key="index" class="list">
          <td><p> {{ article.pk }}  </p> </td>
          <td><router-link :to="'/articles/' + article.pk">{{ article.title }} </router-link></td>
          <td><p> {{ article.user }}  </p> </td>
          <td><p> {{ article.created_at.slice(5,10) }}  </p> </td>
          <td><p> {{ article.hits }}  </p> </td>
          <td><p> {{article.like_article.length}}  </p> </td>
        </tr>
      </table>
      <button @click="prev" v-if="page_prev"> 이전 페이지 </button>
      <button @click="next" v-if="page_next"> 다음 페이지 </button>
      <div>
        <router-link to="/create"><button> 글 쓰기 </button></router-link>
      </div>
    </div>
  </div>
</template>

<script>
import testaxios from '../../src/axios'
export default {
  data () {
    return {
      articles: [],
      page_next:null,
      page_prev:null,
      islogin:'',
      year:null,
      month:null,
      date:null,
    }
  },
  mounted() {
    testaxios.get('http://localhost:8000/articles/')
    .then(response => {
      this.articles = response.data.results
      this.page_next= response.data.next
      this.page_prev = response.data.previous
      const today = new Date()
      this.year = today.getFullYear();
      this.month = today.getMonth();
      this.date = today.getDate();
    })
    .catch(error =>{
      console.log(error)
    })
  },
  methods:{
    next(){
      testaxios.get(this.page_next)
      .then(response => {
        this.articles = response.data.results
        this.page_next= response.data.next
        this.page_prev = response.data.previous
      })
      .catch(error =>{
        console.log(error)
      })
    },
    prev(){
      testaxios.get(this.page_prev)
      .then(response => {
        this.articles = response.data.results
        this.page_next= response.data.next
        this.page_prev = response.data.previous
      })
      .catch(error =>{
        console.log(error)
      })
    }
  }
}
</script>

<style>


</style>

