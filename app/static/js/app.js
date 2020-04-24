
import Vue from 'vue'
import App from './App.vue'
import router from './vue-router'

Vue.config.productionTip = false


new Vue({
    el: '#app',
    data: {},
    template: 'App',
    router,
    render: h => h(App)

}).$mount('#app')

