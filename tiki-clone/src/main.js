import { createApp } from "vue";
import App from "./App.vue";
import './style.css'
import { createVuestic } from "vuestic-ui";
import "vuestic-ui/css";

createApp(App).use(createVuestic()).mount("#app");
