import { createRouter, createWebHistory } from 'vue-router'

import Home from '../views/Homepage/index.vue'

const routes = [
    {
        path: '/',
        name: "home",
        component: Home
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes
})

export default router
