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
        <ul id="filter-categories">
            <li v-for="category in filter_categories">
                {{ category }}
                <span 
                    class="icon-cross"
                    @click="remove_category_from_filter(category)"
                ></span>
            </li>
        </ul>
    </form>

    

    <ul id="posts">
        <template v-for="post in posts">
            <li class="post">
                <div class="post-title">
                    <router-link :class="`brightness-hover`" :to="{ name:'PostDetail', params: { id: post.id }}">{{ post.title }}</router-link>
                </div>
                <div class="separator"></div>
                <div :class="`post-date`" :data-date="moment(post.created)"></div>
                <div v-if="post.is_draft" :class="`post-draft icon-low-vision`" data-tooltip="draft"></div>

                <div 
                    :class="`category brightness-hover`"
                    v-on:click="this.$router.push({name: 'Blog', query: { category: add_to_categories(post.category) }})"
                >
                    {{ post.category }}
                </div>
            </li>
        </template>
    </ul>

    <ul id="pagination">
        <li 
            @click="() => { if (current_page - 1 > 0) current_page-- }"
            :class="{ 'disabled': current_page - 1 < 1}"
            data-content="previous"
        ></li>

        <template v-for="page in pages">
            <li :class="{ 'active': current_page == page}"
                @click="() => { current_page = page }"
                :data-content="`${page}`"
            ></li>
        </template>

        <li 
            @click="() => { if (current_page + 1 <= total_pages) current_page++ }"
            :class="{ 'disabled': current_page + 1 > total_pages}"
            data-content="next"
        ></li>
    </ul>


</template>
    
<script>
    import "./blog.css";
    import moment from "moment";
    import { get_token } from '@/utils';

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
            'current_page': 'get_posts_by_page',
            '$route.query': function() { 
                this.current_page = 1; 
                this.get_posts_by_page();
            },
        },
        computed: {
            pages() {
                let pages = [];
                let start = 0;
                const max_show = 3

                let count_pages = max_show < this.total_pages ? max_show : this.total_pages

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
            filter_categories() {
                if (this.$route.query.category){
                    if (typeof this.$route.query.category == 'string')
                        return [this.$route.query.category]
                    return this.$route.query.category
                }
                return []
            }
        },
        methods: {
            moment(date) {
                return moment(date, 'DD-MM-YYYY').format('DD.MM.YYYY');
            },
            search_posts(event) {
                clearTimeout(this.timer)
                this.timer = setTimeout(() => {
                    this.get_posts_by_page(1);
                }, 800)
            },
            async get_posts_by_page() {
                if ((this.current_page < 1 || this.current_page > this.total_pages) && this.total_pages)
                    return
                this.is_searching = true;
                const response = await fetch(
                    `http://127.0.0.1:8000/api/posts/?search=${this.post_search}&limit=${this.limit}&offset=${(this.current_page - 1) * this.limit}` +
                    (this.$route.query.category ? `&category=${this.$route.query.category}` : ''), 
                    {
                        method: "get",
                        headers: {
                            Authorization: `Bearer ${get_token()}`,
                        },
                    },
                );
                const content = await response.json();
                this.posts = content['results'];
                this.total_pages = Math.ceil(content['count'] / this.limit);
                this.is_searching = false;
            },
            remove_category_from_filter(category) {
                const query_categories = this.filter_categories.slice();
                query_categories.splice(this.filter_categories.indexOf(category), 1);
                this.$router.replace({name: 'Blog', query: {category: query_categories}});
            },
            add_to_categories(category) {
                const query_categories = this.filter_categories;
                if (query_categories.indexOf(category) === -1)
                    return query_categories.concat(category);
                return query_categories;
            }
        },
        beforeMount() {
            this.get_posts_by_page();
        },
  };

</script>