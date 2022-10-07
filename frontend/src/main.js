import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import "./assets/main.css";
import "./assets/icomoon.css";

router.beforeEach(function () {
    window.scrollTo(0, 0);
})

const app = createApp(App);
app.use(router);
app.mount('#app');
