import { createRouter } from 'vue-router';


const routes = [
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
    component: () => import('./pages/Blog/CreatePostPage.vue'),
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