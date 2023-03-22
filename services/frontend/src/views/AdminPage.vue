<template>
  <div class="adminPage">
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
    name: 'AdminPage',
    components: {
      NavAdminVue
    }
  }
</script>


<style>
</style>