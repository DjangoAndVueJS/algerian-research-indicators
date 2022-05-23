<template>
  <TheNavigation />
  <div class="forms-container" :class="`${is_not_user ? 'is_not_user' : 'is_user'}`">
    <SignUpViewVue />
    <!-- <LogInViewVue /> -->
  </div>
</template>
<script setup>
import TheNavigationVue from "@/components/TheNavigation.vue";
import { ref } from "vue";
import SignUpViewVue from "./SignUpView.vue";
import LogInViewVue from "./LogInView.vue";
const is_not_user = ref(true);

function toggleUser() {
  is_not_user.value = !is_not_user.value;
}
</script>
