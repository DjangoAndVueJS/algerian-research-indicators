import appApi from "./api.js";

export default {
  getLocation() {
    return appApi.get("/location-list");
  },
};
