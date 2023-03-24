<template>
  <div class="admin_user_list">
    <h1>회원 조회</h1>
      <table>
        <tr>
          <th>아이디</th>
          <th>이름</th>
          <th>가입일</th>
          <th>수정일</th>
        </tr>
        <tr v-for="admin in admins" :key="admin.name">
          <td>{{ admin.admin_id }}</td>
          <td>{{ admin.name }}</td>
          <td>{{ admin.created_at }}</td>
          <td>{{ admin.updated_at }}</td>
        </tr>
      </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'adminUsers',
  data() {
    return {
      admins: []
    }
  },
  mounted() {
    this.getUsers()
  },
  methods: {
    getUsers() {
      axios.get(`${process.env.VUE_APP_BACKEND_URL}/admins/page/1`)
        .then(response => {
          this.admins = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style>
</style>
