import { createApp } from "vue";
import App from "./App.vue";
import './style.css'
import { createVuestic } from "vuestic-ui";
import "vuestic-ui/css";
import axios from 'axios'
import VueAxios from 'vue-axios'

import router from './router'

const app = createApp(App)
app.use(createVuestic())
app.use(router)
app.use(VueAxios, axios)

app.mount('#app')
