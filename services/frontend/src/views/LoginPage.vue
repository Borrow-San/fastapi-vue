<template>
  <div class="loginPage">
    <router-link to="/"><img :src="imgUrl +'/bslogo.PNG'" style="width:80%;"></router-link><br>
    아이디: <input class="id"/><br>
    비밀번호: <input class="password"/><br>
    <router-link to="/admin">아이디/비밀번호 찾기</router-link>
    <router-link to="/admin">로그인</router-link>
  </div>
</template>

<script>
export default {
  name: 'loginPage',
  data(){
    return {
      imgUrl: "https://bucket-lqr64n.s3.ap-northeast-2.amazonaws.com"
    }
  }
}
</script>

<style>
</style>