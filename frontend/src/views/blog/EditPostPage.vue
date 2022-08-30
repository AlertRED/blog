<template>
    <form id="create-post">
        <div>
            <label for="post-title">Title</label>
            <input
                id="post-title"
                v-model="title"
            />

        </div>
        
        <div id="post-body">
            <mavon-editor
                ref="me"
                @imgAdd="$imgAdd"
                defaultOpen="preview"
                language="en"
                fontSize="1rem"
                :boxShadow=false
                :tabSize=4
                placeholder=" "
                v-model="body"
            />
        </div>
        
        <div id="post-options">
            <div class="select">
                <label>Category</label>
                <select v-model="category">
                    <option disabled value="">Выбор категории</option>
                    <option v-for="_category in categories">{{ _category.title }}</option>
                </select>
            </div>
            
            <div class="checkbox">
                <input type="checkbox" name="is-draft" value="is-draft" v-model="is_draft">
                <label for="is-draft">Draft</label> 
            </div>
        </div>

        <template v-if="is_edit">
            <a href="#" v-on:click="save_post">Save</a>
        </template>
        <template v-else>
            <a href="#" v-on:click="create_post">Create</a>
        </template>
        
    </form>

    

</template>

<script>
    import "./blog.css";
    import "mavon-editor/dist/css/index.css"
    import { ModelSelect } from 'vue-search-select';
    import { mavonEditor } from 'mavon-editor';
    import { get_token } from '@/utils';


    export default {
        
        data() {
            return {
                title: null,
                body: null,
                is_draft: true,
                category: null,
                categories: [],
            }
        },
        components: {
            ModelSelect,
            mavonEditor,
        },
        computed: {
            is_edit() {
                return Boolean(this.$route.params.id);
            }
        },
        methods: {
            async $imgAdd(pos, $file){
                var formdata = new FormData();
                formdata.append('file', $file);
                const response = await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/post-files/`, 
                    {
                        method: "post",
                        body: formdata,
                        headers: {
                            Authorization: `Bearer ${get_token()}`,
                        },
                    },
                );
                const content = await response.json();
                this.$refs.me.$img2Url(pos, 'http://127.0.0.1:8000' + content.url);
            },
            async create_post(){
                let bodyContent = new FormData();
                bodyContent.append('title', this.title);
                bodyContent.append('body', this.body);
                bodyContent.append('category', this.category);
                bodyContent.append('is_draft', this.is_draft);
                
                const response = await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/posts/`, 
                    {
                        method: "post",
                        body: bodyContent,
                        headers: {
                            Authorization: `Bearer ${get_token()}`,
                        },
                    },
                );
                const content = await response.json();
                if (await response.status == 201){
                    const post_id = content['id'];
                    this.$router.push({name:'PostDetail', params: { id: post_id }});
                }
            },
            async save_post(){
                let bodyContent = new FormData();
                bodyContent.append('title', this.title);
                bodyContent.append('body', this.body);
                bodyContent.append('category', this.category);
                bodyContent.append('is_draft', this.is_draft);

                const response = await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/post/${this.$route.params.id}/`, 
                    {
                        method: "patch",
                        body: bodyContent,
                        headers: {
                            Authorization: `Bearer ${get_token()}`,
                        },
                    },
                );
                if (await response.status == 200)
                    this.$router.push({name:'PostDetail', params: { id: this.$route.params.id }});
            },
            async get_post(id){
                const response = await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/post/${id}/`, 
                    {
                        method: "get",
                        headers: {
                            Authorization: `Bearer ${get_token()}`,
                        },
                    },
                );
                const post = await response.json();
                this.title = post.title;
                this.body = post.body;
                this.is_draft = post.is_draft;
                this.category = post.category;
            },
            async get_categories() {
                const response = await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/categories`, 
                    {
                        method: "get",
                        headers: {
                            Authorization: `Bearer ${get_token()}`,
                        },
                    },
                );
                const content = await response.json();
                this.categories = content['results'];
            },
        },
        beforeMount() {
            if (this.is_edit)
                this.get_post(this.$route.params.id);
            this.get_categories()
        },
  };

</script>

<style type="text/css">
    .markdown-body, .content-input-wrapper, .auto-textarea-input, .v-show-content, .v-note-op {
        background-color: var(--color-background) !important;
    }

    .v-note-wrapper {
        border: none;
    }

    .v-note-wrapper .v-note-op {
        border-bottom: 1px solid var(--color-background) !important;
    }

    .v-note-wrapper .v-note-op .v-left-item .op-icon.selected, .v-note-wrapper .v-note-op .v-right-item .op-icon.selected {
        background: var(--color-background) !important;
    }
</style>
