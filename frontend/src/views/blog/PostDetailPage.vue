<template>
    <div id="post-detail">
        <div id="post-title">{{ post?.title }}</div>
            <div v-if="is_auth()" class="post-tools">
                <router-link
                    :to="{ name:'EditPost', params: {id: this.$route.params.id}}"
                    class="brightness-hover"
                >
                    <span class="icon-pencil"></span>
                </router-link>
                <a 
                    class="brightness-hover"
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
    import "./blog.css";
    import "mavon-editor/dist/css/index.css"

    import { mavonEditor } from 'mavon-editor';
    import { get_bearer, is_auth } from '@/utils';

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
                    `${import.meta.env.VITE_BASE_API_URL}/post/${this.$route.params.id}/`, 
                    {
                        method: "get",
                        headers: {
                            Authorization: get_bearer(),
                        },
                    },
                );
                if (response.status == 200)
                    this.post = await response.json();
                else
                    this.$router.push({name: 'NotFound  '});
            },
            async delete_post() {
                const response = await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/post/${this.$route.params.id}/`, 
                    {
                        method: "delete",
                        headers: {
                            Authorization: get_bearer(),
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
