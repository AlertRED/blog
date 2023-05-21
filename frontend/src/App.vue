<template>
  <main-navbar/>
  <div id="content">
    <router-view @loadDeleteNote="loadDeleteNote" @loadIsAuth="loadIsAuth"/>
  </div>
  <admin-menu :delete_note="delete_note" :is_auth="is_auth"/> 
</template>

<script>
  import MainNavbar from './components/MainNavbar.vue';
  import AdminMenu from './components/AdminMenu.vue';
  import { check_is_auth } from '@/utils';

  export default {

    name: "App",
    components: {
      MainNavbar,
      AdminMenu,
    },
    data() {
      return {
        delete_note: null,
        is_auth: check_is_auth(),
      }
    },
    methods: {
      loadDeleteNote(delete_note) {
          this.delete_note = delete_note;
      },
      loadIsAuth(is_auth) {
          this.is_auth = is_auth;
      }
    }
  }
</script>
