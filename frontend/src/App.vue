<template>
  <main-navbar/>
  <div id="content">
    <router-view/>
  </div>
  <div v-if="is_auth" id="admin-menu">
    <ul>
      <li><router-link :to="{ name:'create-post'}">Create post</router-link></li>      
      <li><router-link :to="{ name:'create-post'}">Draft</router-link></li>
    </ul>
    <hr/>
    menu
  </div>
</template>

<script>
  import MainNavbar from './components/MainNavbar.vue';

  import { is_auth } from '@/utils';

  export default {
    name: "App",
    components: {
      MainNavbar,
    },
    methods: {
      is_auth(){
          return is_auth();
      },
    },
  };
</script>

<style>
</style>
