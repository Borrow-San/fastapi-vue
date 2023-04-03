<template>
  <div class="article-delete">
    <h1>게시물 일괄 삭제</h1>
      <select v-model="option">
        <option value="article_id">글번호</option>
        <option value="title">제목</option>
        <option value="type">타입</option>
        <option value="admin_id">작성자</option>
      </select>
      <input type="text" v-model="search">
      <br>
      <button @click.prevent="deleteArticle">삭제하기</button>
      <p style="color:red">{{message}}</p>
  </div>
</template>


<script>
import axios from 'axios';
import authMixin from '@/mixins/authMixin';

export default {
  name: "article-delete",
  mixins: [authMixin],
  data() {
    return {
      search: '',
      message: '',
      option: 'title', // 기본값
    }
  },
  methods: {
    async deleteArticle() {
      try {
        if (!this.checkToken()) { // checkToken() 함수 호출
          return;
        }
        const response = await axios.delete(
          `${process.env.VUE_APP_BACKEND_URL}/articles/remove`,
          {
            data: {
              option: this.option,
              [this.option]: this.search,
            },
          },
        );
        this.message = response.data.msg;
      } catch (error) {
        console.error(error);
        this.message = error.response.data.detail;
      }
    }
  }
}
</script>

<style scoped>

</style>