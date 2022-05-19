<template>
  <SideNavigation />
  <router-view name="userProfile" />
</template>

<script>
import SideNavigation from "@/components/SideNavigation.vue";
export default {
  name: "HomeView",
  components: { SideNavigation },
};
</script>
<style lang="scss" scoped>
.content {
  position: relative;
  left: 230px;
  width: calc(100vw - 230px);
  border-right: 2px solid #000;
  height: 100%;
  padding: 12px;
  font-size: 2vw;
  overflow: scroll;
}
</style>
