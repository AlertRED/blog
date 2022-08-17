<template>
    <form id="edit-tag">
        <template v-if="tag_edit && new_tag_tittle">
            <input v-model="new_tag_tittle" placeholder="Edit tag"/>
            <a href="#" v-on:click="save_tag">Save</a>
        </template>
        <template v-else>
            <input  v-model="new_tag_tittle" placeholder="Create tag"/>
            <a href="#" v-on:click="create_tag">Create</a>
        </template>
        
    </form>
    
    <ul id="tags">
      <template v-for="tag in tags">
        <li>
            <router-link :to="{ name:'blog', query: { tag: tag.title }}">{{ tag.title }}</router-link>
            <div class="options">
                <span @click="() => { this.tag_edit = tag; new_tag_tittle = tag.title; }" class="icon-pencil"></span>
                <span @click="delete_tag(tag.id)" class="icon-bin"></span>
            </div>
        </li>
      </template>
    </ul>
</template>
    
<script>
    export default {

        data() {
            return {
                tags: [],
                new_tag_tittle: null,
                tag_edit: null,
            }
        },
        methods: {
            moment() {
                return moment();
            },
            async get_tags() {
                const response = await fetch(
                    `http://127.0.0.1:8000/api/tags`, 
                    {
                        method: "get",
                    },
                );
                const content = await response.json();
                this.tags = content['results'];
            },
            async create_tag() {
                let bodyContent = new FormData();
                bodyContent.append('title', this.new_tag_tittle);
                        
                const response = await fetch(
                    `http://127.0.0.1:8000/api/tags/`, 
                    {
                        method: "post",
                        body: bodyContent,
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem('token')}`,
                        },
                    },
                );
                if (response.status == 201){
                    this.get_tags();
                    this.new_tag_tittle = null;
                }
            },
            async delete_tag(id) {
                const response = await fetch(
                    `http://127.0.0.1:8000/api/tag/${id}`, 
                    {
                        method: "delete",
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem('token')}`,
                        },
                    },
                );
                if (response.status == 204)
                    this.get_tags();                
            },
            async save_tag() {
                let bodyContent = new FormData();
                bodyContent.append('title', this.new_tag_tittle);

                const response = await fetch(
                    `http://127.0.0.1:8000/api/tag/${this.tag_edit.id}/`, 
                    {
                        method: "put",
                        body: bodyContent,
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem('token')}`,
                        },
                    },
                );
                if (response.status == 200){
                    this.get_tags();
                    this.tag_edit = null;
                    this.new_tag_tittle = null;
                }
            },
        },
        beforeMount() {
            this.get_tags();
        },
  };

</script>