<template>
  <h1>profiles</h1>
  <div class="profiles">
    {{ profiles }}
  </div>

  <button @click="createLocation">add Location</button>
</template>
<script>
import axios from "axios";
import { ref } from "vue";
import locationApi from "@/services/locationApi";
export default {
  setup() {
    const profiles = ref("");
    const loadProfiles = async () => {
      try {
        const res = await locationApi.getLocation();
        profiles.value = res.data;
        console.log(profiles.value);
      } catch (err) {
        console.log(err);
      }
    };
    loadProfiles();
    // axios.get("http://localhost:8000/api/v1/location-list")
    // .then((res) => {
    //   // reseponse
    //   console.log(res.data[2].state_name);
    //   profiles.value = res.data[2].state_name;
    // })
    // .catch(err=>{
    // handleerr
    // });

    const createLocation = () => {
      axios
        .post(
          "http://127.0.0.1:8000/api/v1/location-create/",
          JSON.stringify({
            id: 12,
            state_name: "tiaret",
          })
        )
        .then((res) => {
          console.log(res.data);
        });
    };
    return {
      profiles,
      createLocation,
    };
  },
};
</script>
