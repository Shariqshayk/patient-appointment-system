import Home from './components/Home.vue'
import Register from './components/Register.vue'
import PatientLogin from './components/PatientLogin.vue'
import DoctorLogin from './components/DoctorLogin.vue'
import PatientDashboard from './components/PatientDashboard.vue'
import DoctorDashboard from './components/DoctorDashboard.vue'
import AppointmentBooking from './components/AppointmentBooking.vue'
import DoctorModal from './components/DoctorModal.vue'
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
    },
    {
        name: "PatientDashboard",
        component:PatientDashboard,
        path: "/patientdashboard"
    },
    {
        name: "DoctorDashboard",
        component:DoctorDashboard,
        path: "/doctordashboard"
    },
    {
        name: "AppointmentBooking",
        component: AppointmentBooking,
        path: "/appointmentbooking"
    },
    {
        name: "DoctorModal",
        component: DoctorModal,
        path: "/doctormodal"
    }
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;

