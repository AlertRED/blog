<template>
    <ul id="tags">
      <template v-for="tag in tags">
        <li><a href="#">{{ tag.title }}</a></li>
      </template>
    </ul>
</template>
    
<script>
    export default {

        data() {
            return {
                tags: [],
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
        },
        beforeMount() {
            this.get_tags();
        },
  };

</script>