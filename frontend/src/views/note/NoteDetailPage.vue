<template>
    <div id="note-detail">
        <div id="note-title">{{ note?.title }}</div>
        <div id="note-category">
            <router-link 
                :class="`brightness-hover`" 
                :to="{ name:'Notes', query: { category: note?.category }}"
            >
                ~ {{ note?.category }} ~
            </router-link>
        </div>
        <div :class="`markdown-body`" v-html="markdown_body"></div>
    </div>
</template>
    
<script>
    import "./note.css";
    import "mavon-editor/dist/css/index.css";
    import "../../assets/markdown-add-on.css";
    import { mavonEditor } from 'mavon-editor';
    import { parse_response, throw_body, get_bearer, is_auth } from '@/utils';

    export default {
        data() {
            return {
                note: null,
            } 
        },
        computed: {
            markdown_body() {
                const markdownIt = mavonEditor.getMarkdownIt();
                return markdownIt.render(this.note?.body || '');
            }
        },
        methods: {
            is_auth(){
                return is_auth();
            },
            async get_note() {
                const response = await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/note/${this.$route.params.id}/`, 
                    {
                        method: "get",
                        headers: {
                            Authorization: get_bearer(),
                        },
                    },
                ).then(response => parse_response(response));

                if (response.status === 200)
                    this.note = await response.body
                else
                    this.$router.push({name: 'NotFound'});
            },
            async delete_note() {
                const response = await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/note/${this.$route.params.id}/`, 
                    {
                        method: "delete",
                        headers: {
                            Authorization: get_bearer(),
                        },
                    },
                ).then(response => parse_response(response));

                if (response.status === 204)
                    this.$router.push({name: 'Notes'})
                else
                    throw_body(response.body)
            },
        },
        beforeMount() {
            this.get_note();
            this.$emit('loadDeleteNote', this.delete_note);
        },
  };
</script>


<style>
#editor {
  margin: auto;
  width: 80%;
}
</style>
