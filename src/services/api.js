//  create axios(api) instances

import axios from "axios";

export default {
  appApi(url = "http://localhost:8092/api/v1/") {
    return axios.create({
      baseURL: url,
    });
  },
};
