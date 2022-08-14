<template>
    <div id="post-detail">
        <div id="post-title">{{ post?.title }}</div>
            <div class="post-tools">
                <router-link
                    :to="{ name:'edit-post', params: {id: this.$route.params.id}}"
                    class="disable-decoration"
                    @click=""
                >
                    <span class="icon-pencil"></span>
                </router-link>
                
                <a 
                    class="disable-decoration"
                    @click="delete_post"
                >
                    <span class="icon-bin"></span>
                </a>
            </div>
        <ul id="post-tags">
            <li v-for="tag in post?.tags" :key="index">
                <router-link :to="{ name:'blog', params: { tag: tag }}">
                    {{ tag }}
                </router-link>
            </li>
        </ul>
        <div id="post-body">{{ post?.body }}</div>
    </div>
</template>
    
<script>
    export default {
        
        data() {
            return {
                post: null,
            }
        },
        methods: {
            async get_post() {
                const response = await fetch(
                    `http://127.0.0.1:8000/api/post/${this.$route.params.id}/`, 
                    {
                        method: "get",
                    },
                );
                this.post = await response.json();
            },
            async delete_post() {
                const response = await fetch(
                    `http://127.0.0.1:8000/api/post/${this.$route.params.id}/`, 
                    {
                        method: "delete",
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem('token')}`,
                        },
                    },
                );
                const status = await response.status;
                if (status == 204)
                    this.$router.push({name: 'blog'});
            },
        },
        beforeMount() {
            this.get_post();
        },
  };
</script>


<style>
#editor {
  margin: auto;
  width: 80%;
}
</style>
