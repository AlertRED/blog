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
    path: '/tags',
    name: 'tags',
    component: () => import('./pages/Tags/TagsPage.vue'),
  },
]

export default function(history) {
  return createRouter({
    history,
    routes
  })
}