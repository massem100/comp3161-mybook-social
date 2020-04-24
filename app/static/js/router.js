import Router from 'vue-router';
import signup from './components/signup-page.vue';
import login from './components/login-page.vue';
import dashboard from './components/dashboard.vue';


Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        // { path: "/Home", component: Home },
        // Put other routes here
        { path: "/login", component: login },

        { path: "/", component: login },

        { path: "/signup", component: signup },

        { path: "/dashboard", component: dashboard },
        // This is a catch all route in case none of the above matches
        { path: "*", component: NotFound }
    ],
});