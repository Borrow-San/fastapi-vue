<template>
    <div class="nav-admin">
        <ul>
            <li><router-link to="/admin">메인 화면</router-link></li>
            <li class="dropdown">
              <a href="#">관리자 관리</a>
              <ul><router-link to="/admin/admin-info">관리자 조회</router-link></ul>
              <ul><router-link to="/admin/create">관리자 생성</router-link></ul>
              <ul><router-link to="/admin/delete">관리자 삭제</router-link></ul>
            </li>
            <li><router-link to="/admin/user-info">회원 관리</router-link></li>
            <li><router-link to="/admin/rents">파손 기록</router-link></li>
            <li><router-link to="/admin/claims">상담 접수</router-link></li>
            <li><router-link to="/admin/stands">보관함 관리</router-link></li>
            <li><router-link to="/admin/demands">수요예측 현황</router-link></li>
            <li><router-link to="/admin/notice">공지사항 관리</router-link></li>
        </ul>
        <ul>
            <li><a href="#" @click.prevent="logout">로그아웃</a></li>
        </ul>
    </div>
</template>

<script>
import Cookies from 'js-cookie';
import axios from 'axios';

export default {
  name: 'nav-admin',
  methods: {
    logout() {
      Cookies.remove('myToken');
      delete axios.defaults.headers.common['Authorization']; // header에서 토큰 삭제
      this.$router.push('/login');
    }
  }
}
</script>

<style>
.nav-admin {
  display: flex;
  flex-direction: column;
}

.nav-admin ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav-admin li {
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

.nav-admin li:last-child {
  border-bottom: none;
}

.nav-admin .dropdown ul {
  display: none;
}

.nav-admin .dropdown:hover ul {
  display: block;
}

.nav-admin a {
  text-decoration: none;
  color: #333;
}

.nav-admin a:hover {
  color: #666;
}
</style>