<template>
    <div class="nav-admin">
      <span v-if="remainingTime">({{ remainingTime }}분 남음)</span>
      <a href="#" @click.prevent="extendExpirationTime">로그인 연장</a>
        <ul>
            <li><router-link to="/admin">메인 화면</router-link></li>
            <li class="dropdown">
              <a href="#">관리자 관리</a>
              <ul><router-link to="/admin/admin-info">관리자 조회</router-link></ul>
              <ul><router-link to="/admin/admin-create">관리자 생성</router-link></ul>
              <ul><router-link to="/admin/admin-delete">관리자 삭제</router-link></ul>
            </li>
            <li class="dropdown">
                <a href="#">게시물 관리</a>
                <ul><router-link to="/admin/article-info">게시물 조회</router-link></ul>
                <ul><router-link to="/admin/article-create">게시물 생성</router-link></ul>
                <ul><router-link to="/admin/article-delete">게시물 삭제</router-link></ul>
                <ul><router-link to="/admin/article-clame">문의 & 답변</router-link></ul>
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
  data() {
    return {
      remainingTime: null, // 쿠키 만료까지 남은 시간 (분)
      timer: null, // 타이머 객체
    };
  },
  mounted() {
    this.initRemainingTime();
    this.startTimer();
  },
  methods: {
    initRemainingTime() {
      const token = Cookies.get('myToken');
      if (token) {
        const decodedToken = JSON.parse(atob(token.split('.')[1]));
        const expTime = decodedToken.exp * 1000; // 만료 시간 (밀리초 단위)
        const remainingTime = Math.floor((expTime - Date.now()) / (60 * 1000)); // 분 단위로 변환
        this.remainingTime = remainingTime > 0 ? remainingTime : null; // 만료 시간이 지났으면 null로 설정
      }
    },
    startTimer() {
      this.timer = setInterval(() => {
        this.initRemainingTime();
      }, 1000 * 60); // 1분마다 remainingTime 업데이트
    },
    stopTimer() {
      clearInterval(this.timer);
    },
    extendExpirationTime() {
      const token = Cookies.get('myToken');
      if (token) {
        const decodedToken = JSON.parse(atob(token.split('.')[1]));
        const expTime = decodedToken.exp * 1000; // 만료 시간 (밀리초 단위)
        const newExpTime = Date.now() + 30 * 60 * 1000; // 30분 후의 시간 (밀리초 단위)
        if (newExpTime > expTime) {
          decodedToken.exp = Math.floor(newExpTime / 1000);
          const newToken = `${token.split('.')[0]}.${btoa(JSON.stringify(decodedToken))}.${token.split('.')[2]}`;
          Cookies.set('myToken', newToken, { expires: 7, secure: false }); // 7일간 유지
          axios.defaults.headers.common['Authorization'] = `Bearer ${newToken}`; // header에 토큰 추가
          this.initRemainingTime();
        }
      }
    },
    logout() {
      Cookies.remove('myToken');
      delete axios.defaults.headers.common['Authorization']; // header에서 토큰 삭제
      this.stopTimer();
      this.$router.push('/login');
    },
  },
  beforeUnmount() {
    this.stopTimer();
  },
};
</script>

<style scoped>
.nav-admin {
  display: flex;
  flex-direction: column;
  background-color: #f2f2f2;
  width: 200px;
  padding: 10px;
  border-radius: 5px;
}

.nav-admin ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.nav-admin ul li {
  margin-bottom: 5px;
}

.nav-admin ul li a {
  color: black;
  text-decoration: none;
  display: block;
  padding: 5px;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.nav-admin ul li a:hover {
  background-color: #d9d9d9;
}

.nav-admin .dropdown > a {
  font-weight: bold;
}

.nav-admin .dropdown ul {
  display: none;
  margin-left: 10px;
}

.nav-admin .dropdown:hover > ul {
  display: block;
}
</style>