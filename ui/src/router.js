import Vue from 'vue'
import Router from 'vue-router'

const routerMapping = [
    {path: '/', component: 'Home'},
    {path: '/about', component: 'About'}
]

const routes = routerMapping.map(route => {
    return {
        ...route,
        component: () => import(`./views/${route.component}.vue`)
    }
})

Vue.use(Router)

export default new Router({routes})
