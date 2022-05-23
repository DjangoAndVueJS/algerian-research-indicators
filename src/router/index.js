import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("@/views/LandingPageView"),
  },
  {
    path: "/auth",
    name: "auth",
    component: () => import("@/views/Authentication/AuthUsers.vue"),
  },

  {
    path: "/sponsor",
    name: "profiles",
    component: () => import("@/views/SponsorView"),
  },
  {
    path: "/user",
    name: "user",
    component: () => import("@/views/Clients/UserHomeView.vue"),
    children: [
      {
        path: "profile",
        name: "UserProfile",
        component: () => import("@/views/Clients/ResearcherProfileView.vue"),
      },
      {
        path: "dashboard",
        name: "Dashboard",
        component: () => import("@/views/Clients/UserDash.vue"),
      },
      {
        path: "team",
        name: "TeamMember",
        component: () => import("@/views/Clients/TeamMemberView.vue"),
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
  linkActiveClass: "active",
});

export default router;
