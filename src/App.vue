<template>
  <header>
    <TheNavigation />
  </header>
  <div class="appContent">
    <router-view />
  </div>
</template>
<script>
import TheNavigation from "@/components/TheNavigation.vue";

export default {
  setup() {},
  components: { TheNavigation },
  methods: {},
};
</script>
<style lang="scss">
#app {
  min-height: 100vh;
}
header {
  width: 100%;
  position: fixed;
}
.appContent {
  padding-top: 55px;
}
</style>
