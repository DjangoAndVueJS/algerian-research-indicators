<template>
  <aside class="sidebar">
    <nav class="nav-apps">
      <router-link class="links" :to="{ name: 'Dashboard' }">
        <i class="bx bxs-dashboard"></i>
        <span class="router-tags tooltip">Dashboard</span>
      </router-link>
      <h5>Pages</h5>
      <router-link class="links" :to="{ name: 'TeamMember' }">
        <i class="bx bx-group"></i>
        <span class="router-tags tooltip">Team</span>
      </router-link>
      <h5>Settings</h5>

      <router-link class="links" :to="{ name: 'UserProfile' }">
        <i class="bx bx-group"></i>
        <span class="router-tags tooltip">Profile</span>
      </router-link>
    </nav>
  </aside>
</template>
<style lang="scss">
@import "@/assets/styles/_global.scss";
</style>
<script setup>
import toggleMenu from "@/views/Clients/UserHomeView.vue";
</script>
