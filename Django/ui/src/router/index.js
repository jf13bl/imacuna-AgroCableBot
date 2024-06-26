import { createRouter, createWebHistory } from 'vue-router'

import Inicio from '../views/InicioView.vue'
import LoginView from '../components/loginView.vue'
import monitoreo from '../views/Agrocablebot/monitoreoView.vue'
import control from '../views/Agrocablebot/controlView.vue'
import calendario from '../views/Agrocablebot/calendarioView.vue'
import estadisticas from '../views/Agrocablebot/estadisticasView.vue'
import soporte from '../views/Agrocablebot/soporteView.vue'
import mqtt from '../views/Agrocablebot/Mqtt_View.vue'

const routes = [
  {path: '/', name: 'inicio', component: Inicio },
  {path: '/loginview', name: 'loginview', component: LoginView},

  // rutas AgroCableBOt
  {path: '/monitoreo', name: 'monitoreo', component: monitoreo },
  {path: '/control', name: 'control', component: control },
  {path: '/calendario', name: 'calendario', component: calendario },
  {path: '/estadisticas', name: 'estadisticas', component: estadisticas },
  {path: '/soporte', name: 'soporte', component: soporte },
  {path: '/mqtt', name: 'mqtt', component: mqtt },

  ]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

const protecdRoutes= [
  'Admin',
  'monitoreo',
  'control',
  'calendario',
  'estadisticas',
  'soporte',
  'mqtt',
]

router.beforeEach((to, from, next) => {
  const isProtected = protecdRoutes.includes(to.name);
  if(isProtected && !localStorage.getItem('token')){
    next({
      path:'/',
      query: {redirect: to.fullpath}
    })
  }else{
    if (!isProtected && localStorage.getItem('token') && (to.name == 'loginview' || to.name == 'Signup')){
      next({
        path: '/monitoreo'
      })
    }else{
      next();
    }
  }
})

export default router
