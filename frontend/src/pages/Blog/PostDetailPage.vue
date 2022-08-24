<template>
    <div id="post-detail">
        <div id="post-title">{{ post?.title }}</div>
            <div v-if="is_auth()" class="post-tools">
                <router-link
                    :to="{ name:'edit-post', params: {id: this.$route.params.id}}"
                    class="disable-decoration"
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
        <ul id="post-categories">
            <li v-for="category in post?.categories" :key="index">
                <router-link :to="{ name:'Blog', params: { category: category }}">
                    {{ category }}
                </router-link>
            </li>
        </ul>
        <div class="markdown-body" v-html="markdown_body"></div>
    </div>
</template>
    
<script>
    import { mavonEditor } from 'mavon-editor';
    import { get_token, is_auth } from '@/utils';
    import "mavon-editor/dist/css/index.css"

    export default {
        data() {
            return {
                post: null,
            }
        },
        computed: {
            markdown_body() {
                const markdownIt = mavonEditor.getMarkdownIt();
                return markdownIt.render(this.post?.body || '');
            }
        },
        methods: {
            is_auth(){
                return is_auth();
            },
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
                            Authorization: `Bearer ${get_token()}`,
                        },
                    },
                );
                const status = await response.status;
                if (status == 204)
                    this.$router.push({name: 'Blog'});
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
