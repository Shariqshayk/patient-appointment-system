import Home from './components/Home.vue'
import Register from './components/Register.vue'
import {createRouter, createWebHashHistory} from "vue-router"

const routes = [
    {
        name: "Home",
        component: Home,
        path: "/",
    },
    {
        name: "Register",
        component: Register,
        path: "/register"
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;

