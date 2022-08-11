import { createApp } from "vue";
import { createWebHistory } from 'vue-router'
import App from "./App.vue";
import createRouter from "./router";

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

import "./assets/main.css";

const router = createRouter(createWebHistory());
const app = createApp(App);
app.use(router);
app.mount('#app');
