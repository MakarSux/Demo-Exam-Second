import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import CreateOrderView from '../views/CreateOrderView.vue'
import AuthView from '../views/AuthView.vue'
import RegisterView from '../views/RegisterView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: AuthView,
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView
    },
    {
      path: '/createOrder',
      name: 'createOrder',
      component: CreateOrderView,
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView,
    },
  ]
})

export default router
