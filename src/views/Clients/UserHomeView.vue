<template>
  <div class="userHome" :class="`${is_open ? 'is_open' : ''}`">
    <i @click="toggleMenu" class="toggle-menu bx bx-right-arrow-alt"></i>
    <SideNavigation />
    <div class="content">
      <router-view />
    </div>
  </div>
</template>

<script setup>
import SideNavigation from "@/components/SideNavigation.vue";
import { ref } from "vue";
const is_open = ref(false);
const toggleMenu = () => {
  is_open.value = !is_open.value;
};
</script>
<style lang="scss">
.content {
  position: relative;
  left: 70px;
  height: 100vh;
  width: 100%;

  padding: 12px;
  font-size: 2vw;
  overflow: scroll;
  transition: all 0.4s ease;
}
</style>
