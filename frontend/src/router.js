import { createRouter } from 'vue-router';
import { is_auth } from '@/utils';
import { createWebHistory } from 'vue-router'


const routes = [
  { 
    path: '/auth',
    name: 'Auth',
    component: () => import('./views/auth/AuthPage.vue'),
  },
  { 
    path: '/about',
    name: 'About',
    component: () => import('./views/about/AboutPage.vue'),
    alias: '/',
  },
  { 
    path: '/notes',
    name: 'Notes',
    component: () => import('./views/notes/NotePage.vue'),
  },
  { 
    path: '/create-post',
    name: 'CreatePost',
    component: () => import('./views/blog/EditPostPage.vue'),
    meta: { requiresAuth: true },
  },
  { 
    path: '/edit-post/:id',
    name: 'EditPost',
    component: () => import('./views/blog/EditPostPage.vue'),
  },
  { 
    path: '/categories',
    name: 'Categories',
    component: () => import('./views/category/CategoriesPage.vue'),
  },
  { 
    path: '/post-detail/:id',
    name: 'PostDetail',
    component: () => import('./views/blog/PostDetailPage.vue'),
  },
  { 
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('./components/404.vue'),
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

