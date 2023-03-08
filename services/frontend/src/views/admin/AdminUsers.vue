<template>
  <div class="admin_users">
    <h1>회원 조회</h1>
    <table>
      <tr>
        <td v-for="result in results" :key="result.id">
        {{ result }}
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      results: [],
    };
  },
  mounted() {
    axios
      .get('/admins/show')
      .then(response => {
        this.results = response.data;
      })
      .catch(error => {
        console.log(error);
      });
  },
};
</script>

<style>
</style>
