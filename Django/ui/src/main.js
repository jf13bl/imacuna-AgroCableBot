import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import '../src/assets/vendor/swiper/swiper-bundle.min.css'
import '../src/assets/vendor/bootstrap/css/bootstrap.min.css'

import axios from 'axios'
import store from './store'


// import { BootstrapIconsPlugin } from "bootstrap-icons-vue";

import '../src/resources/css/Bootstrap-Calendar.css' 
import '../src/resources/css/integrantes.css' 
import '../src/resources/css/imacuna_style.css' 
import '../src/resources/css/tareasProgramados.css' 
import '../src/resources/css/listcultivo.css' 
import 'bootstrap'; 
import 'bootstrap/dist/js/bootstrap.bundle.min.js'; // Importa el JavaScript de Bootstrap
import 'swiper/css';
import 'swiper/css/pagination';

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'



axios.defaults.baseURL = 'http://0.0.0.0:8000'


const app = createApp(App);
app.use(ElementPlus)
app.use(router).use(store);
// app.use(BootstrapIconsPlugin);


app.mount('#app');