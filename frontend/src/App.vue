<template>
  <main-navbar/>
  <div id="content">
    <router-view @loadDeletePost="loadDeletePost"/>
  </div>
  <admin-menu :delete_post="delete_post"/> 
</template>

<script>
  import MainNavbar from './components/MainNavbar.vue';
  import AdminMenu from './components/AdminMenu.vue';

  export default {
    name: "App",
    components: {
      MainNavbar,
      AdminMenu,
    },
    data() {
      return {
        delete_post: null,
      }
    },
    methods: {
      loadDeletePost(delete_post) {
          this.delete_post = delete_post;
      }
    }
  }
</script>
