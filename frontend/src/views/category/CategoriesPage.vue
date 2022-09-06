<template>
    <form v-if="is_auth()" id="edit-category">
        <template v-if="category_edit && new_category_tittle">
            <input v-model="new_category_tittle" placeholder="Edit category"/>
            <a href="#" v-on:click="save_category">Save</a>
        </template>
        <template v-else>
            <input  v-model="new_category_tittle" placeholder="Create category"/>
            <a href="#" v-on:click="create_category" class="button">Create</a>
        </template>
    </form>
    
    <ul id="categories">
      <template v-for="category in categories">
        <li>
            <router-link class="brightness-hover" :to="{ name:'Blog', query: { category: category.title }}">{{ category.title }}</router-link>
            <div v-if="is_auth()" class="options">
                <span @click="() => { this.category_edit = category; new_category_tittle = category.title; }" class="icon-pencil"></span>
                <span @click="delete_category(category.id)" class="icon-bin"></span>
            </div>
        </li>
      </template>
    </ul>
</template>
    
<script>
    import "./category.css";
    import { parse_response, throw_body, get_bearer, is_auth } from '@/utils';

    export default {
        data() {
            return {
                categories: [],
                new_category_tittle: null,
                category_edit: null,
            }
        },
        methods: {
            is_auth(){
                return is_auth();
            },
            async get_categories() {
                await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/categories`, 
                    {
                        method: "get",
                        headers: {
                            Authorization: get_bearer(),
                        },
                    },
                )
                .then(response => response.json())
                .then(data => (this.categories = data['results']));
            },
            async create_category() {
                let fromBody = new FormData();
                fromBody.append('title', this.new_category_tittle);
                        
                const response = await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/categories/`, 
                    {
                        method: "post",
                        body: fromBody,
                        headers: {
                            Authorization: get_bearer(),
                        },
                    },
                ).then(response => parse_response(response));

                if (response.status === 201){
                    this.get_categories();
                    this.new_category_tittle = null;
                } else
                    throw_body(response.body)
            },
            async delete_category(id) {
                const response = await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/category/${id}`, 
                    {
                        method: "delete",
                        headers: {
                            Authorization: get_bearer(),
                        },
                    },
                ).then(response => parse_response(response));
                
                if (response.status === 204)
                    this.get_categories()
                else
                    throw_body(response.body)             
            },
            async save_category() {
                let fromBody = new FormData();
                fromBody.append('title', this.new_category_tittle);

                const response = await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/category/${this.category_edit.id}/`, 
                    {
                        method: "put",
                        body: fromBody,
                        headers: {
                            Authorization: get_bearer(),
                        },
                    },
                ).then(response => parse_response(response));

                if (response.status === 200){
                    this.get_categories();
                    this.category_edit = null;
                    this.new_category_tittle = null;
                } else
                    throw_body(response.body)          
            },
        },
        beforeMount() {
            this.get_categories();
        },
  };

</script>