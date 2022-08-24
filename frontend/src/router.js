import { createRouter } from 'vue-router';
import { is_auth } from '@/utils';
import { createWebHistory } from 'vue-router'


const routes = [
  { 
    path: '/auth',
    name: 'Auth',
    component: () => import('./pages/Auth/AuthPage.vue'),
  },
  { 
    path: '/about',
    name: 'About',
    component: () => import('./pages/About/AboutPage.vue'),
    alias: '/',
  },
  { 
    path: '/blog',
    name: 'Blog',
    component: () => import('./pages/Blog/BlogPage.vue'),
  },
  { 
    path: '/create-post',
    name: 'CreatePost',
    component: () => import('./pages/Blog/EditPostPage.vue'),
    meta: { requiresAuth: true },
  },
  { 
    path: '/edit-post/:id',
    name: 'EditPost',
    component: () => import('./pages/Blog/EditPostPage.vue'),
  },
  { 
    path: '/categories',
    name: 'Categories',
    component: () => import('./pages/Category/CategoriesPage.vue'),
  },
  { 
    path: '/post-detail/:id',
    name: 'PostDetail',
    component: () => import('./pages/Blog/PostDetailPage.vue'),
  }
]

const history = createWebHistory();
const router = createRouter({ history, routes })

router.beforeEach((to, from) => {
  if (to.meta.requiresAuth && !is_auth()) {
    return {name: 'Auth'}
  }
})

export default router;

