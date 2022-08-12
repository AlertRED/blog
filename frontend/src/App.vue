<template>
  <main-navbar/>
  <div id="content">
    <router-view/>
  </div>
  <div id="admin-menu">
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

  export default {
    name: "App",
    components: {
      MainNavbar,
    },
  };
</script>

<style>
</style>
