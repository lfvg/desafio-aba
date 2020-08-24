import Vue from 'vue';
import Router from 'vue-router';
import ListUser from '@/components/ListUser';
import UserForm from '@/components/UserForm';

Vue.use(Router);

const routes = [
    {
        name: 'home',
        path: '/',
        component: ListUser,
    },
    {
        name: 'edit',
        path: '/user/:id(\\d*)',
        component: UserForm,
        props: true
    }
];

const router = new Router({routes});

export default router;