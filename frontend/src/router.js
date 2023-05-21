import { createRouter } from 'vue-router';
import { check_is_auth } from '@/utils';
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
    component: () => import('./views/note/NotesPage.vue'),
  },
  { 
    path: '/create-note',
    name: 'CreateNote',
    component: () => import('./views/note/EditNotePage.vue'),
    meta: { requiresAuth: true },
  },
  { 
    path: '/edit-note/:id',
    name: 'EditNote',
    component: () => import('./views/note/EditNotePage.vue'),
  },
  { 
    path: '/categories',
    name: 'Categories',
    component: () => import('./views/category/CategoriesPage.vue'),
  },
  { 
    path: '/note-detail/:id',
    name: 'NoteDetail',
    component: () => import('./views/note/NoteDetailPage.vue'),
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
  if (to.meta.requiresAuth && !check_is_auth()) {
    return {name: 'Auth'}
  }
})

export default router;

