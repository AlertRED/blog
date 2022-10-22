<template>
    <form 
        id="note-search"
        v-on:submit.prevent="onSubmit"
    >
        <input 
            v-on:keyup="search_notes"
            :disabled="is_searching"
            v-model="note_search"
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

    

    <ul id="notes">
        <template v-for="note in notes">
            <li class="note">
                <div class="note-title">
                    <router-link :class="`brightness-hover`" :to="{ name:'NoteDetail', params: { id: note.id }}">{{ note.title }}</router-link>
                </div>
                <div class="separator"></div>
                <div :class="`note-date`" :data-date="moment(note.created)"></div>
                <div v-if="note.is_draft" :class="`note-draft icon-low-vision`" data-tooltip="draft"></div>

                <div 
                    :class="`category brightness-hover`"
                    v-on:click="this.$router.push({name: 'Notes', query: { category: add_to_categories(note.category) }})"
                >
                    {{ note.category }}
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
    import "./note.css";
    import moment from "moment";
    import { parse_response, throw_body, get_bearer } from '@/utils';

    export default {
        data() {
            return {
                notes: [],
                note_search: "",
                is_searching: false,
                limit: 8,
                current_page: 1,
                total_pages: null,
            }
        },
        watch: {
            'current_page': 'get_notes_by_page',
            '$route.query': function() { 
                this.current_page = 1; 
                this.get_notes_by_page();
            },
        },
        computed: {
            pages() {
                let pages = [];
                let start = 0;
                const max_show = 3;

                let count_pages = max_show < this.total_pages ? max_show : this.total_pages;

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
            search_notes(event) {
                clearTimeout(this.timer)
                this.timer = setTimeout(() => {
                    this.get_notes_by_page(1);
                }, 800)
            },
            async get_notes_by_page() {
                if ((this.current_page < 1 || this.current_page > this.total_pages) && this.total_pages)
                    return
                this.is_searching = true;
                const response = await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/notes/?search=${this.note_search}&limit=${this.limit}&offset=${(this.current_page - 1) * this.limit}` +
                    (this.$route.query.category ? `&category=${this.$route.query.category}` : ''), 
                    {
                        method: "get",
                        headers: {
                            Authorization: get_bearer(),
                        },
                    },
                ).then(response => parse_response(response));

                if (response.status === 200){
                    this.notes = response.body.results;
                    this.total_pages = Math.ceil(response.body.count / this.limit);
                    this.is_searching = false;
                } else
                    throw_body(response.body)
                
            },
            remove_category_from_filter(category) {
                const query_categories = this.filter_categories.slice();
                query_categories.splice(this.filter_categories.indexOf(category), 1);
                this.$router.replace({name: 'Notes', query: {category: query_categories}});
            },
            add_to_categories(category) {
                const query_categories = this.filter_categories;
                if (query_categories.indexOf(category) === -1)
                    return query_categories.concat(category);
                return query_categories;
            }
        },
        beforeMount() {
            this.get_notes_by_page();
        },
  };

</script>