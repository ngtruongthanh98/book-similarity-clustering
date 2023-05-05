import { createRouter, createWebHistory } from 'vue-router'

import Home from '../views/Homepage/index.vue'
import TikiBookstore from '../views/TikiBookstore/index.vue'

const routes = [
    {
        path: '/',
        name: "home",
        component: Home
    },
    {
        path: '/nha-sach-tiki',
        name: 'tiki-bookstore',
        component: TikiBookstore
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes
})

export default router
