import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { createPinia } from "pinia";
import axios from "axios";
import VueAxios from "vue-axios";

const app = createApp(App);
app.use(router);
app.use(createPinia());
app.use(VueAxios, axios);
router.isReady().then(() => {
  app.mount("#app");
});
