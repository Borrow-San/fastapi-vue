<template>
  <div class="admin-users">
    <h1>회원 조회</h1>
      <table>
        <tr>
          <th>아이디</th>
          <th>이름</th>
          <th>가입일</th>
          <th>수정일</th>
        </tr>
        <tr v-for="admin in admins" :key="admin.admin_id">
          <td>{{ admin.admin_id }}</td>
          <td>{{ admin.name }}</td>
          <td>{{ admin.created_at }}</td>
          <td>{{ admin.updated_at }}</td>
        </tr>
      </table>
      <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
      <div class="pagination">
        <button :disabled="page_info.prev_arrow === false" @click="getUsers(page_info.request_page - 1)">이전</button>
        <button v-for="page in getPagesArray()" :key="page" :class="{active: page === page_info.request_page}" @click="getUsers(page)">{{ page }}</button>
        <button :disabled="page_info.next_arrow === false" @click="getUsers(page_info.request_page + 1)">다음</button>
      </div>
  </div>
</template>
<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
  name: 'admin-users',
  data() {
    return {
      admins: [],
      page_info: {},
      errorMessage: '',
    }
  },
  mounted() {
    this.getUsers()
  },
  methods: {
    getUsers(page = 1) {
      const cookieToken = Cookies.get('myToken'); // 쿠키에서 토큰을 가져옴
      if (!cookieToken) {
        console.error('Token is missing!!'); // 에러 로그 출력
        this.errorMessage = '접근 권한이 없습니다.';
        return;
      }
      // console.log(cookieToken); // 토큰 출력
      axios.get(`${process.env.VUE_APP_BACKEND_URL}/admins/page/${page}`, {
        headers: {
          'Token': `Bearer ${cookieToken}`,
          'Accept': 'application/json; charset=utf-8',
          'Content-Type': 'application/json; charset=utf-8'
        }
      })
        .then(response => {
          // 서버로부터 받은 회원 정보와 페이지 정보를 Vue.js 컴포넌트 데이터에 할당
          this.admins = response.data.user_info.items
          this.page_info = response.data.page_info
        })
        .catch(error => {
          console.error(error.response);
        });
    },
    getPagesArray() {
      let page_start = this.page_info.page_start
      let page_end = this.page_info.page_end
      let pagesArray = []
      for (let i = page_start; i <= page_end; i++) {
        pagesArray.push(i+1)
      }
      return pagesArray
    }
  }
}
</script>

<style>
</style>
