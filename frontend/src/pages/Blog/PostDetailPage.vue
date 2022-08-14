<template>
    <div id="post-detail">
        <div id="post-title">{{ post.title }}</div>
            <div class="post-tools">
                <a>Изменить</a>
                <a>Удалить</a>
            </div>
        <ul id="post-tags">
            <li v-for="tag in post.tags" :key="index">
                <router-link :to="{ name:'post-detail', params: { id: post.id }}">
                    {{ tag }}
                </router-link>
            </li>
        </ul>
        <div id="post-body">{{ post.body }}</div>
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
