<template>
  <div class="adminUsers">
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
    <div v-if="totalPages > 1">
      <button :disabled="page === 1 || !prevArrow" @click="prevPage">이전</button>
      <button :disabled="page === totalPages || !nextArrow" @click="nextPage">다음</button>
      <p>{{ page }} / {{ totalPages }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
  name: 'adminUsers',
  data() {
    return {
      admins: [],
      page: 1,
      totalPages: 1,
      prevArrow: false,
      nextArrow: false,
    }
  },
  mounted() {
    this.getUsers();
  },
  methods: {
    getUsers() {
      const cookieToken = Cookies.get('myToken');
      if (!cookieToken) {
        console.error('Token is missing!!');
        return;
      }
      axios.get(`${process.env.VUE_APP_BACKEND_URL}/admins/page/${this.page}`, {
        headers: {
          'Token': `Bearer ${cookieToken}`,
          'Accept': 'application/json; charset=utf-8',
          'Content-Type': 'application/json; charset=utf-8'
        }
      })
        .then(response => {
          this.admins = response.data.user_info.items;
          this.totalPages = response.data.page_info.page_cnt;
          this.prevArrow = response.data.page_info.prev_arrow;
          this.nextArrow = response.data.page_info.next_arrow;
        })
        .catch(error => {
          console.error(error.response);
        });
    },
    prevPage() {
      if (this.page > 1) {
        this.page--;
        this.getUsers();
      }
    },
    nextPage() {
      if (this.page < this.totalPages) {
        this.page++;
        this.getUsers();
      }
    }
  }
}
</script>

<style>
.loginPage {
  width: 40%;
  margin: 0 auto;
  padding: 2%;
  background-color: #f5f5f5;
  box-shadow: 0 0 10px rgba(0,0,0,0.3);
  border-radius: 5px;
  font-family: Arial, sans-serif;
  text-align: center;
}

.loginPage a {
  text-decoration: none;
  color: #444;
}

.loginPage a:hover {
  color: #666;
}

.loginPage input {
  padding: 2%;
  margin-bottom: 2%;
  margin-top: 3%;
  width: 95%;
  border: none;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(0,0,0,0.3);
}

.loginPage input:focus {
  outline: none;
  box-shadow: 0 0 5px rgba(0,0,255,0.5);
}

.loginPage .id {
  margin-top: 20px;
}

.loginPage .password {
  margin-bottom: 20px;
}

.loginPage button {
  background-color: #3498db;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.loginPage button:hover {
  background-color: #2980b9;
}
</style>