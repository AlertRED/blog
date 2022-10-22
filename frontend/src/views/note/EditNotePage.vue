<template>
    <form id="create-note">
        <div>
            <label for="note-title">Title</label>
            <input
                id="note-title"
                v-model="title"
            />

        </div>
        
        <div id="note-body">
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
        
        <div id="note-options">
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
            <a href="#" v-on:click="save_note">Save</a>
        </template>
        <template v-else>
            <a href="#" v-on:click="create_note">Create</a>
        </template>
        
    </form>

    

</template>

<script>
    import "./note.css";
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
                    `${import.meta.env.VITE_BASE_API_URL}/note-files/`, 
                    {
                        method: "note",
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
            async create_note(){
                let fromBody = new FormData();
                fromBody.append('title', this.title);
                fromBody.append('body', this.body);
                fromBody.append('category', this.category);
                fromBody.append('is_draft', this.is_draft);
                
                const response = await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/notes/`, 
                    {
                        method: "note",
                        body: fromBody,
                        headers: {
                            Authorization: get_bearer(),
                        },
                    },
                ).then(response => parse_response(response));

                if (response.status === 201)
                    this.$router.push({name:'NoteDetail', params: { id: response.body.id }});
                else
                    throw_body(response.body)
            },
            async save_note(){
                let fromBody = new FormData();
                fromBody.append('title', this.title);
                fromBody.append('body', this.body);
                fromBody.append('category', this.category);
                fromBody.append('is_draft', this.is_draft);

                const response = await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/note/${this.$route.params.id}/`, 
                    {
                        method: "put",
                        body: fromBody,
                        headers: {
                            Authorization: get_bearer(),
                        },
                    },
                ).then(response => parse_response(response));

                if (response.status === 200)
                    this.$router.push({name:'NoteDetail', params: { id: this.$route.params.id }});
                else
                    throw_body(response.body)
            },
            async get_note(id){
                const response = await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/note/${id}/`, 
                    {
                        method: "get",
                        headers: {
                            Authorization: get_bearer(),
                        },
                    },
                ).then(response => parse_response(response));

                if (response.status === 200){
                    const note = response.body;
                    this.title = note.title;
                    this.body = note.body;
                    this.is_draft = note.is_draft;
                    this.category = note.category;
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
                this.get_note(this.$route.params.id);
            this.get_categories()
        },
  };

</script>

<style type="text/css">
    .markdown-body, .content-input-wrapper, .auto-textarea-input, .v-show-content, .v-note-op {
        background-color: var(--color-background) !important;
    }

    .v-note-wrapper {
        border: none !important;
    }

    .v-note-op {
        border-bottom: 1px solid var(--color-background) !important;
    }

    .v-note-wrapper .v-note-panel .v-note-edit.divarea-wrapper.scroll-style::-webkit-scrollbar{
        background-color: var(--color-unnoticeble) !important;
    }
</style>
