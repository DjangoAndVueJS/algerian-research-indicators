<template>
  <aside>
    <nav>
      <router-link class="links" to="/">Home</router-link>
      <router-link class="links" to="/">Home</router-link>
      <h5>Dashboard</h5>
      <h5>Settings</h5>
      <router-link to="/user/profile">Profile</router-link>
    </nav>
  </aside>
</template>
<style lang="scss" scoped>
aside {
  position: fixed;
  top: 0;
  left: 0;
  height: 100%;
  width: 230px;
  transition: 0.3s ease;
  nav {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
    overflow: auto;
    .links {
      text-align: center;
      margin: 12px;
    }
    h5 {
      border-top: 2px solid #000;
      margin: 12px 5px;
      text-align: center;
      color: grey;
    }
  }
}
</style>
<script setup></script>
