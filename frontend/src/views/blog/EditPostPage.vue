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
    import "mavon-editor/dist/css/index.css";
    import "../../assets/markdown-add-on.css";
    import { ModelSelect } from 'vue-search-select';
    import { mavonEditor } from 'mavon-editor';
    import { parse_response, throw_body, get_bearer } from '@/utils';


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
                            Authorization: get_bearer(),
                        },
                    },
                ).then(response => parse_response(response));

                if (response.status === 201)
                    this.$refs.me.$img2Url(pos, import.meta.env.VITE_BASE_API_URL + response.body.url);
                else
                    throw_body(response.body)
            },
            async create_post(){
                let fromBody = new FormData();
                fromBody.append('title', this.title);
                fromBody.append('body', this.body);
                fromBody.append('category', this.category);
                fromBody.append('is_draft', this.is_draft);
                
                const response = await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/posts/`, 
                    {
                        method: "post",
                        body: fromBody,
                        headers: {
                            Authorization: get_bearer(),
                        },
                    },
                ).then(response => parse_response(response));

                if (response.status === 201)
                    this.$router.push({name:'PostDetail', params: { id: response.body.id }});
                else
                    throw_body(response.body)
            },
            async save_post(){
                let fromBody = new FormData();
                fromBody.append('title', this.title);
                fromBody.append('body', this.body);
                fromBody.append('category', this.category);
                fromBody.append('is_draft', this.is_draft);

                const response = await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/post/${this.$route.params.id}/`, 
                    {
                        method: "put",
                        body: fromBody,
                        headers: {
                            Authorization: get_bearer(),
                        },
                    },
                ).then(response => parse_response(response));

                if (response.status === 200)
                    this.$router.push({name:'PostDetail', params: { id: this.$route.params.id }});
                else
                    throw_body(response.body)
            },
            async get_post(id){
                const response = await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/post/${id}/`, 
                    {
                        method: "get",
                        headers: {
                            Authorization: get_bearer(),
                        },
                    },
                ).then(response => parse_response(response));

                if (response.status === 200){
                    const post = response.body;
                    this.title = post.title;
                    this.body = post.body;
                    this.is_draft = post.is_draft;
                    this.category = post.category;
                } else
                    throw_body(response.body)
            },
            async get_categories() {
                const response = await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/categories`, 
                    {
                        method: "get",
                        headers: {
                            Authorization: get_bearer(),
                        },
                    },
                ).then(response => parse_response(response));

                if (response.status === 200)
                    this.categories = response.body.results
                else
                    throw_body(response.body)
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
