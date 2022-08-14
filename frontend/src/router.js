import { createRouter } from 'vue-router';


const routes = [
  { 
    path: '/auth',
    name: 'auth',
    component: () => import('./pages/Auth/AuthPage.vue'),
  },
  { 
    path: '/about',
    name: 'about-me',
    component: () => import('./pages/About/AboutPage.vue'),
    alias: '/',
  },
  { 
    path: '/blog',
    name: 'blog',
    component: () => import('./pages/Blog/BlogPage.vue'),
  },
  { 
    path: '/create-post',
    name: 'create-post',
    component: () => import('./pages/Blog/EditPostPage.vue'),
  },
  { 
    path: '/edit-post/:id',
    name: 'edit-post',
    component: () => import('./pages/Blog/EditPostPage.vue'),
  },
  { 
    path: '/tags',
    name: 'tags',
    component: () => import('./pages/Tags/TagsPage.vue'),
  },
  { 
    path: '/post-detail/:id',
    name: 'post-detail',
    component: () => import('./pages/Blog/PostDetailPage.vue'),
  }
]

export default function(history) {
  return createRouter({
    history,
    routes
  })
}