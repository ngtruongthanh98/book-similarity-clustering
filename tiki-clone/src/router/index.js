import { createRouter, createWebHistory } from 'vue-router'

import Home from '../views/Homepage/index.vue'

const routes = [
    {
        path: '/',
        component: Home
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes
})

export default router
