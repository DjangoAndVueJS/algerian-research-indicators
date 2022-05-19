<template>
  <router-view />
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
body {
  overflow-x: hidden;
  &::-webkit-scrollbar {
    height: 8px;
    width: 4px;
  }

  &::-webkit-scrollbar:hover {
    background-color: #e9e9e9;
    border: none;
  }

  &::-webkit-scrollbar-thumb {
    border: none;
    transition: background-color 0.2s ease;
  }

  &::-webkit-scrollbar-thumb:hover {
    background-color: #798892;
  }

  &:hover {
    &::-webkit-scrollbar-thumb {
      background-color: rgba(0, 0, 0, 0.1);
    }
  }
}
</style>
