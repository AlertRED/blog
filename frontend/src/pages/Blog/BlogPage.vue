<template>
    <form 
        id="post-search"
        v-on:submit.prevent="onSubmit"
    >
        <input 
            v-on:keyup="search_posts"
            :disabled="is_searching"
            v-model="post_search"
            type="text"
            placeholder="Search"
        >
    </form>

    <ul id="posts">
        <template v-for="post in posts">
            <li class="post">
                <div class="post-title"><a href="#">{{ post.title }}</a></div>
                <div class="separator"></div>
                <div :class="`post-date`" :data-date="moment(post.created, 'DD-MM-YYYY').format('DD.MM.YYYY')"></div>
                <div class="tags">
                    <template v-for="tag in post.tags">
                        <div class="tag" v-on:click="get_posts_by_tag(tag)">{{ tag }}</div>
                    </template>
                </div>
            </li>
        </template>
    </ul>

    <ul id="pagination">
        <li 
            @click="get_posts_previous(previous_link)"
            :class="{ 'disabled' : previous_link === null}"
            data-content="previous"
        >
        </li>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>...</li>
        <li>7</li>
        <li 
            @click="get_posts_next(next_link)"
            :class="{ 'disabled': next_link === null}"
            data-content="next"
        >
        </li>
    </ul>



</template>
    
<script>
    import moment from "moment";

    export default {
        
        data() {
            return {
                posts: [],
                post_search: "",
                is_searching: false,
                next_link: null,
                previous_link: null,
                pagination_limit: 2,
                pagination_offset: 0,
            }
        },
        methods: {
            moment() {
                return moment();
            },
            search_posts(event) {
                clearTimeout(this.timer)
                this.timer = setTimeout(() => {
                    this.get_posts();
                }, 800)
            },
            async get_posts() {
                this.is_searching = true;                
                const response = await fetch(
                    `http://127.0.0.1:8000/api/posts/?search=${this.post_search}&limit=${this.pagination_limit}&offset=${this.pagination_offset}`, 
                    {
                        method: "get",
                    },
                );
                const content = await response.json();
                this.posts = content['results'];
                this.next_link = content['links']['next'];
                this.previous_link = content['links']['previous'];
                this.is_searching = false;
            },
            async get_posts_next(url) {
                this.is_searching = true;                
                const response = await fetch(
                    `${url}`, 
                    {
                        method: "get",
                    },
                );
                const content = await response.json();
                this.posts = content['results'];
                this.next_link = content['links']['next'];
                this.previous_link = content['links']['previous'];
                this.is_searching = false;
                // debugger;
            },
            async get_posts_previous(url) {
                this.is_searching = true;                
                const response = await fetch(
                    `${url}`, 
                    {
                        method: "get",
                    },
                );
                const content = await response.json();
                this.posts = content['results'];
                this.next_link = content['links']['next'];
                this.previous_link = content['links']['previous'];
                this.is_searching = false;
            },
            async get_posts_by_tag(tag) {
                this.is_searching = true;                
                const response = await fetch(
                    `http://127.0.0.1:8000/api/posts?tag=${tag}`, 
                    {
                        method: "get",
                    },
                );
                const content = await response.json();
                this.posts = content['results'];
                this.next_link = content['links']['next'];
                this.previous_link = content['links']['previous'];
                this.is_searching = false;
            },
        },
        beforeMount() {
            this.get_posts();
        },
  };

</script>