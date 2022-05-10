<template>
  <nav>
    <router-link class="links" to="/">Home</router-link> |
    <router-link class="links" to="/about">About</router-link>
  </nav>
</template>
<style lang="sass" scoped>
nav
  display: flex;
  background: red;
  .links:hover
      background: black
      color: white
</style>
