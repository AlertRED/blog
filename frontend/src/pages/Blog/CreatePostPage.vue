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
                const response = await fetch(
                    `http://127.0.0.1:8000/api/posts/`, 
                    {
                        method: "post",
                        body: {
                            title: this.title,
                            body: this.body,
                        }
                    },
                );
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
