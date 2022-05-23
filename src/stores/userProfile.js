import { defineStore } from "pinia";

export const useUserProfileStore = defineStore("userProfile", {
  state: () => ({
    token: localStorage.getItem("token") || "",
    user: localStorage.getItem("user") || null,
    isAuthenticated: false,
  }),
  getters: {
    // gettoken :
  },
  actions: {
    init_store() {
      if (localStorage.getItem("token")) {
        this.token = localStorage.getItem("token");
        this.isAuthenticated = true;
      } else {
        this.token = "";
        this.isAuthenticated = false;
      }
    },
    setToken(token) {
      this.token = token;
      this.isAuthenticated = true;
    },
    removeToken() {},
  },
});
