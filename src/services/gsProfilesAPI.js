//  g-s-profiles --> google scholar profiles api

import googleScholarApi from "./api";

export default {
  getProfiles() {
    return googleScholarApi.get(
      "?engine=google_scholar_profiles&mauthors=Mike&api_key=efa8d7e7a7fda118b855de81e82288b21f5c99811905b85a22e9dfc84ebbae4d"
    );
  },
};
