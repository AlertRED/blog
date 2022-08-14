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
        <a href="#" v-on:click="create_post">Create</a>
        <button type="submit">Create</button>
    </form>

    

</template>
    
<script>

    export default {
        
        data() {
            return {
                title: null,
                body: null,
            }
        },
        methods: {
            async create_post(){

                let bodyContent = new FormData();
                bodyContent.append('title', this.title);
                bodyContent.append('body', this.body);

                const response = await fetch(
                    `http://127.0.0.1:8000/api/posts/`, 
                    {
                        method: "post",
                        body: bodyContent,
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem('token')}`,
                        },
                    },
                );
                const content = await response.json();
                const post_id = content['id'];
                this.$router.push({name:'post-detail', params: { id: post_id }});
            },
        },
  };

</script>


<style>
#editor {
  margin: auto;
  width: 80%;
}
</style>
