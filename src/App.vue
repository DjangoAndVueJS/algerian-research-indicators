<template>
  <router-view />
</template>
<script>
export default {
  setup() { },
  components: {},
  methods: {},
};
</script>
<style lang="scss">
:root {
  --primary: #4ade80;
  --primary-alt: #22c55e;
  --grey: #64748b;
  --dark: #1e293b;
  --dark-alt: #334155;
  --light: #f1f5f9;
  --sidebar-width: 300px;
}

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
