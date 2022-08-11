<template>
  <main-navbar/>
  <div id="content">
    <router-view/>
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
