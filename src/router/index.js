import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("@/views/LandingPageView"),
  },
  {
    path: "/sponsor",
    name: "profiles",
    component: () => import("@/views/SponsorView"),
  },
  {
    path: "/user",
    name: "user",
    component: () => import("@/views/Clients/HomeView.vue"),
    children: [
      {
        path: "profile",
        name: "userProfile",
        component: () => import("@/views/Clients/ResearcherProfileView"),
      },
    ],
  },
  {
    path: "/profile",
    name: "userProfile",
    component: () => import("@/views/Clients/ResearcherProfileView"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
