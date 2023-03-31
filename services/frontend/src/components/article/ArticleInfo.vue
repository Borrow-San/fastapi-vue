<template>
  <div class="article-info">
    <h1>게시물 조회</h1>
    <table>
      <thead>
        <tr>
          <th>번호</th>
          <th>제목</th>
          <th>작성일</th>
          <th>작성자</th>
          <th>내용</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="article in articles" :key="article.article_id">
          <td>{{ article.article_id }}</td>
          <td>{{ article.title }}</td>
          <td>{{ article.created_at }}</td>
          <td>{{ article.admin_id }}</td>
          <td>{{ article.text }}</td>
        </tr>
      </tbody>
    </table>
    <p style="color:red">{{message}}</p>
    <div class="pagination">
      <button :disabled="!page_info.prev_arrow" @click="getArticles(page_info.request_page - 1)">이전</button>
      <button v-for="page in getPagesArray()" :key="page" :class="{active: page === page_info.request_page}" @click="getArticles(page)">{{ page }}</button>
      <button :disabled="!page_info.next_arrow" @click="getArticles(page_info.request_page + 1)">다음</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import authMixin from "@/mixins/authMixin";

export default {
  name: 'article-info',
  mixins: [authMixin],
  data() {
    return {
      articles: [],
      page_info: {},
      message: '',
    };
  },
  mounted() {
    this.getArticles();
  },
  methods: {
    getArticles(page = 1) {
      if (!this.checkToken()) {
        return;
      }
      axios
        .get(`${process.env.VUE_APP_BACKEND_URL}/articles/page/${page}`)
        .then((response) => {
          // 서버로부터 받은 회원 정보와 페이지 정보를 Vue.js 컴포넌트 데이터에 할당
          this.articles = response.data.article_info.items;
          this.page_info = response.data.page_info;
        })
        .catch((error) => {
          console.error(error.response);
        });
    },
    getPagesArray() {
      const { page_start, page_end } = this.page_info;
      const pagesArray = [];
      for (let i = page_start; i <= page_end; i++) {
        pagesArray.push(i + 1);
      }
      return pagesArray;
    },
  },
};
</script>

<style>
</style>
