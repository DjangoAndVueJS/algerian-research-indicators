import api from "./api.js";

export default {
  getLocation() {
    return api().get("/location-list");
  },
};
