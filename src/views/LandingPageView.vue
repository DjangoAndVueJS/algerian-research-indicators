<template>
  <header>
    <TheNavigation />
  </header>
  <h1 class="text-3xl font-bold underline">hrllo</h1>
  <div class="content">
    <main>
      <section id="hero">
        <!-- <h1 class="tagline">
          The
          <span class="aka">First</span>
          <br />
          Collaborative website for
          <br />
          <span class="aka">algerian Researcher</span>
        </h1> -->
        <main class="mt-10 mx-auto max-w-7xl px-4 sm:mt-12 sm:px-6 md:mt-16 lg:mt-20 lg:px-8 xl:mt-28">
          <div class="sm:text-center lg:text-left">
            <h1 class="text-4xl tracking-tight font-extrabold text-gray-900 sm:text-5xl md:text-6xl">
              <span class="block xl:inline">The First Online</span>
              <br>
              <span class="block text-indigo-600 xl:inline"> callobaration platform</span>
            </h1>
            <div class="mt-5 sm:mt-8 sm:flex sm:justify-center lg:justify-start">
              <div class="rounded-md shadow">
                <button @click="signUp"
                  class="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 md:py-4 md:text-lg md:px-10">
                  Get started </button>
              </div>
            </div>
          </div>
        </main>
        <p class="description"></p>
        <!-- <p class="actions">
           <button >Get Started</button> 
        </p> -->
      </section>
      <section id="features">features of the site</section>
      <section id="howItWorks">definitions of site</section>
      <section id="developersTeamMember">developers team</section>
      <h1 class="text-3xl underline">
        Hello world!
      </h1>

    </main>
  </div>
</template>
<script>
import router from "@/router";
import TheNavigation from "@/components/TheNavigation.vue";
export default {
  setup() { },
  components: { TheNavigation },
  methods: {
    signUp() {
      return router.push("/auth");
    },
    logIn() {
      return router.push("/login");
    },
  },
};
</script>
<style lang="scss" scoped>
.content {
  font-family: InterExtraBold;
  font-size: 30px;
  // max-width: 960px;
  font-weight: 1000;
}
</style>
