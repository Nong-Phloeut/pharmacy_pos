import { createRouter, createWebHistory } from "vue-router";

import DashboardView from "../views/DashboardView.vue";
import PharmacistsView from "../views/PharmacistsView.vue";
import AdminsView from "../views/AdminsView.vue";
import MedicationsView from "../views/MedicationsView.vue";
import DailySalesReport from "../views/DailySalesReport.vue";
import ExpiredItemsReport from "../views/ExpiredItemsReport.vue";
import LoginView from '../views/Login.vue'

const routes = [
  {
    path: "/login",
    name: "Login",
    component: LoginView,
  },
  {
    path: "/",
    component: () => import("../views/Layout.vue"),
    children: [
      { path: "", redirect: "/dashboard" },
      { path: "dashboard", name: "Dashboard", component: DashboardView },
      {
        path: "users/pharmacists",
        name: "Pharmacists",
        component: PharmacistsView,
      },
      { path: "users/admins", name: "Admins", component: AdminsView },
      {
        path: "inventory/medications",
        name: "Medications",
        component: MedicationsView,
      },
      {
        path: "reports/daily-sales",
        name: "DailySales",
        component: DailySalesReport,
      },
      {
        path: "reports/expired-items",
        name: "ExpiredItems",
        component: ExpiredItemsReport,
      },
    ],
  },
  {
    path: "/",
    redirect: "/dashboard",
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// router.beforeEach((to, from, next) => {
//   const isAuthenticated = !!localStorage.getItem('token') // or any auth check logic

//   if (to.path !== '/login' && !isAuthenticated) {
//     next('/login')
//   } else {
//     next()
//   }
// })

export default router;
