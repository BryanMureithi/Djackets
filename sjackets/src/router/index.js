import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";
import LogIn from "../views/Login.vue";
import SignUp from "../views/Signup.vue";
import ProductView from "../views/Products.vue";
import ProductDetail from "../views/Product.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomePage,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/:category_slug/:product_slug/",
    name: "ProductDetail",
    component: ProductDetail,
  },
  {
    path: "/products",
    name: "ProductView",
    component: ProductView,
  },
  {
    path: "/login",
    name: "login",
    component: LogIn,
  },
  {
    path: "/signup",
    name: "signup",
    component: SignUp,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
