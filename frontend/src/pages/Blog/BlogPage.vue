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
                <div class="post-title"><router-link :to="{ name:'post-detail', params: { id: post.id }}">{{ post.title }}</router-link></div>
                <div class="separator"></div>
                <div :class="`post-date`" :data-date="moment(post.created, 'DD-MM-YYYY').format('DD.MM.YYYY')"></div>
                <div class="tags">
                    <template v-for="tag in post.tags"> 
                        <div class="tag" v-on:click="this.$router.push({name: 'blog', query: { tag: tag }})">{{ tag }}</div>
                    </template>
                </div>
            </li>
        </template>
    </ul>

    <ul id="pagination">
        <li 
            @click="get_posts_by_page(current_page - 1)"
            :class="{ 'disabled': current_page - 1 < 1}"
            data-content="previous"
        ></li>

        <template v-for="page in pages">
            <li :class="{ 'active': current_page == page}"
                @click="get_posts_by_page(page)"
                :data-content="`${page}`"
            ></li>
        </template>

        <li 
            @click="get_posts_by_page(current_page + 1)"
            :class="{ 'disabled': current_page + 1 > total_pages}"
            data-content="next"
        ></li>
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

                limit: 8,
                current_page: 1,
                total_pages: null,
            }
        },
        watch: {
            '$route.params': 'get_posts_by_page',
        },
        computed:{
            pages() {
                let pages = [];
                let start = 0;

                let count_pages = 3 < this.total_pages ? 3 : this.total_pages

                if (this.current_page == 1)
                    start = this.current_page
                else if (this.current_page == this.total_pages)
                    start = this.total_pages - (count_pages - 1)
                else
                    start = this.current_page - Math.floor(count_pages / 2);

                for(let i = start; i < start + count_pages; i++ ) {
                    pages.push(i);
                }
                return pages;
            },
        },
        methods: {
            moment() {
                return moment();
            },
            search_posts(event) {
                clearTimeout(this.timer)
                this.timer = setTimeout(() => {
                    this.get_posts_by_page(1);
                }, 800)
            },
            async get_posts_by_page(page, tag = null) {
                if ((page < 1 || page > this.total_pages) && this.total_pages)
                    return
                this.is_searching = true;
                const response = await fetch(
                    `http://127.0.0.1:8000/api/posts/?search=${this.post_search}&limit=${this.limit}&offset=${(page - 1) * this.limit}` +
                    (this.$route.query.tag ? `&tag=${this.$route.query.tag}` : ''), 
                    {
                        method: "get",
                    },
                );
                const content = await response.json();
                this.posts = content['results'];
                this.current_page = page;
                this.total_pages = Math.ceil(content['count'] / this.limit);
                this.is_searching = false;
            },
        },
        beforeMount() {
            this.get_posts_by_page(this.current_page);
        },
  };

</script>