<template>
  <main-navbar/>
  <div id="content">
    <router-view @loadDeleteNote="loadDeleteNote"/>
  </div>
  <admin-menu :delete_note="delete_note"/> 
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
        delete_note: null,
      }
    },
    methods: {
      loadDeleteNote(delete_note) {
          this.delete_note = delete_note;
      }
    }
  }
</script>
