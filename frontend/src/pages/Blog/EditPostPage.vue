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
                defaultOpen="preview"
                language="en"
                fontSize="1rem"
                :boxShadow=false
                placeholder=" "
                :tabSize=4
                v-model="body"
            />
        </div>
        
        <div id="post-category">
            <label>Category</label>
            <select v-model="category">
                <option disabled value="">Выбор категории</option>
                <option v-for="_category in categories">{{ _category.title }}</option>
            </select>
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
    import { ModelSelect } from 'vue-search-select';
    import { mavonEditor } from 'mavon-editor';
    import "mavon-editor/dist/css/index.css"

    export default {
        
        data() {
            return {
                title: null,
                body: null,
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
            async create_post(){
                let bodyContent = new FormData();
                bodyContent.append('title', this.title);
                bodyContent.append('body', this.body);
                bodyContent.append('category', this.category);
                
                const response = await fetch(
                    `http://127.0.0.1:8000/api/posts/`, 
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
                    this.$router.push({name:'post-detail', params: { id: post_id }});
                }
            },
            async save_post(){
                let bodyContent = new FormData();
                bodyContent.append('title', this.title);
                bodyContent.append('body', this.body);
                bodyContent.append('category', this.category);
                const response = await fetch(
                    `http://127.0.0.1:8000/api/post/${this.$route.params.id}/`, 
                    {
                        method: "patch",
                        body: bodyContent,
                        headers: {
                            Authorization: `Bearer ${get_token()}`,
                        },
                    },
                );
                if (await response.status == 200)
                    this.$router.push({name:'post-detail', params: { id: this.$route.params.id }});
            },
            async get_post(id){
                const response = await fetch(
                    `http://127.0.0.1:8000/api/post/${id}/`, 
                    {
                        method: "get",
                    },
                );
                const post = await response.json();
                this.title = post.title;
                this.body = post.body;
                this.category = post.category;
            },
            async get_categories() {
                const response = await fetch(
                    `http://127.0.0.1:8000/api/categories`, 
                    {
                        method: "get",
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
