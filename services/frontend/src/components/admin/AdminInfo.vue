<template>
  <div class="admin-info">
    <h1>회원 조회</h1>
    <table>
      <thead>
        <tr>
          <th>아이디</th>
          <th>이름</th>
          <th>가입일</th>
          <th>수정일</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="admin in admins" :key="admin.admin_id">
          <td>{{ admin.admin_id }}</td>
          <td>{{ admin.name }}</td>
          <td>{{ admin.created_at }}</td>
          <td>{{ admin.updated_at }}</td>
        </tr>
      </tbody>
    </table>
    <p style="color:red">{{message}}</p>
    <div class="pagination">
      <button :disabled="!page_info.prev_arrow" @click="getUsers(page_info.request_page - 1)">이전</button>
      <button v-for="page in getPagesArray()" :key="page" :class="{active: page === page_info.request_page}" @click="getUsers(page)">{{ page }}</button>
      <button :disabled="!page_info.next_arrow" @click="getUsers(page_info.request_page + 1)">다음</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import authMixin from '@/mixins/authMixin';

export default {
  name: 'admin-info',
  mixins: [authMixin],
  data() {
    return {
      admins: [],
      page_info: {},
      message: '',
    };
  },
  mounted() {
    this.getUsers();
  },
  methods: {
    getUsers(page = 1) {
      if (!this.checkToken()) {
        return;
      }
      axios
        .get(`${process.env.VUE_APP_BACKEND_URL}/admins/page/${page}`)
        .then((response) => {
          // 서버로부터 받은 회원 정보와 페이지 정보를 Vue.js 컴포넌트 데이터에 할당
          this.admins = response.data.user_info.items;
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
        pagesArray.push(i);
      }
      return pagesArray;
    },
  },
};
</script>

<style>
</style>
