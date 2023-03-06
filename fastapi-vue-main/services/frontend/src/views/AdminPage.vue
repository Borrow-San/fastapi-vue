<template>
  <div class="loginPage">
    <h3>adminID 님, 안녕하세요.</h3>
    <table>
      <tbody>
        <tr>
          <NavAdminVue/>
          <td>
            <router-view/>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import NavAdminVue from '@/components/common/NavAdmin.vue'

export default {
  name: 'loginPage',
  components: {
    NavAdminVue
  }
}
</script>

<style>
  h3{
    text-align: left;
  }
  table {
    text-align: left;
    border-collapse: collapse;
    border: 0;
  }
  td {
    border: 4px solid #aaa;
    background-clip: padding-box;
    width: 80vw;
    height: 80vw;
    scroll-snap-align: start;
  }
</style>
