import Home from './components/Home.vue'
import Register from './components/Register.vue'
import PatientLogin from './components/PatientLogin.vue'
import DoctorLogin from './components/DoctorLogin.vue'
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
    {
        name: "PatientLogin",
        component: PatientLogin,
        path: "/patientlogin"
    },
    {
        name: "DoctorLogin",
        component: DoctorLogin,
        path: "/doctorlogin"
    }
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;

