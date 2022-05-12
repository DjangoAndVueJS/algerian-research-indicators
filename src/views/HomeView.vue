<template>
  <div class="homeView">
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
        <p class="actions"></p>
      </section>
      <section id="features"></section>
      <section id="howItWorks"></section>
      <section id="developersTeamMember"></section>
    </main>
    <div class="footer"></div>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: "HomeView",
  components: {},
};
</script>

<style lang="scss" scoped>
.homeView {
  font-family: InterExtraBold;
  font-size: 30px;
  // max-width: 960px;
  font-weight: 1000;
}
</style>
