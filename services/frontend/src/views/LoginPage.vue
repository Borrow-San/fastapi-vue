<template>
  <div class="loginPage">
    <router-link to="/">Logo</router-link><br>
    아이디: <input class="id"/><br>
    비밀번호: <input class="password"/><br>
    <router-link to="/admin">아이디/비밀번호 찾기</router-link>
    &nbsp;&nbsp;&nbsp;
    <router-link to="/admin">로그인</router-link>
  </div>
</template>

<script>
export default {
  name: 'loginPage'
}
</script>

<style>
</style>
