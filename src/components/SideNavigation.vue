<template>
  <nav>
    <router-link class="links" to="/">Home</router-link> |
    <router-link class="links" to="/about">About</router-link>
    <button ref="toggle" @click="ToggleTheme">Switch mode</button>
  </nav>
</template>
<style lang="scss" scoped>
nav {
  display: flex;
  background: red;
  .links:hover {
    background: black;
    color: white;
  }
}
</style>
<script>
export default {
  methods: {
    // ToggleTheme() {
    //   let root = document.documentElement;
    //   if (root.style.getPropertyValue("--light-dark-mode") === "#000") {
    //     root.style.setProperty("--light-dark-mode", "#fff");
    //   } else {
    //     root.style.setProperty("--light-dark-mode", "#000");
    //   }
    //   // if(this.$refs.toggle.style.)
    // },
  },
};
</script>
