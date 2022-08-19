<template>
    <form id="edit-category">
        <template v-if="category_edit && new_category_tittle">
            <input v-model="new_category_tittle" placeholder="Edit category"/>
            <a href="#" v-on:click="save_category">Save</a>
        </template>
        <template v-else>
            <input  v-model="new_category_tittle" placeholder="Create category"/>
            <a href="#" v-on:click="create_category">Create</a>
        </template>
        
    </form>
    
    <ul id="categories">
      <template v-for="category in categories">
        <li>
            <router-link :to="{ name:'blog', query: { category: category.title }}">{{ category.title }}</router-link>
            <div class="options">
                <span @click="() => { this.category_edit = category; new_category_tittle = category.title; }" class="icon-pencil"></span>
                <span @click="delete_category(category.id)" class="icon-bin"></span>
            </div>
        </li>
      </template>
    </ul>
</template>
    
<script>
    export default {

        data() {
            return {
                categories: [],
                new_category_tittle: null,
                category_edit: null,
            }
        },
        methods: {
            moment() {
                return moment();
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
            async create_category() {
                let bodyContent = new FormData();
                bodyContent.append('title', this.new_category_tittle);
                        
                const response = await fetch(
                    `http://127.0.0.1:8000/api/categories/`, 
                    {
                        method: "post",
                        body: bodyContent,
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem('token')}`,
                        },
                    },
                );
                if (response.status == 201){
                    this.get_categories();
                    this.new_category_tittle = null;
                }
            },
            async delete_category(id) {
                const response = await fetch(
                    `http://127.0.0.1:8000/api/category/${id}`, 
                    {
                        method: "delete",
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem('token')}`,
                        },
                    },
                );
                if (response.status == 204)
                    this.get_categories();                
            },
            async save_category() {
                let bodyContent = new FormData();
                bodyContent.append('title', this.new_category_tittle);

                const response = await fetch(
                    `http://127.0.0.1:8000/api/category/${this.category_edit.id}/`, 
                    {
                        method: "put",
                        body: bodyContent,
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem('token')}`,
                        },
                    },
                );
                if (response.status == 200){
                    this.get_categories();
                    this.category_edit = null;
                    this.new_category_tittle = null;
                }
            },
        },
        beforeMount() {
            this.get_categories();
        },
  };

</script>