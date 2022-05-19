<template>
  <header>
    <TheNavigation />
  </header>
  <div class="conten">
    <main>
      <section id="hero">
        <h1 class="tagline">
          The
          <span class="aka">First</span>
          <br />
          Collaborative website for
          <br />
          <span class="aka">algerian Researcher</span>
        </h1>
        <p class="description"></p>
        <p class="actions">
          <button @click="SignUp">Sign Up</button>
        </p>
      </section>
      <section id="features"></section>
      <section id="howItWorks"></section>
      <section id="developersTeamMember"></section>
    </main>
  </div>
</template>
<script>
import router from "@/router";
import TheNavigation from "@/components/TheNavigation.vue";
export default {
  setup() {},
  components: { TheNavigation },
  methods: {
    SignUp() {
      return router.push("/user");
    },
  },
};
</script>
<style lang="scss" scoped>
.conten {
  font-family: InterExtraBold;
  font-size: 30px;
  // max-width: 960px;
  font-weight: 1000;
}
</style>
