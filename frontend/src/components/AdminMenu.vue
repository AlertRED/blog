<template>
    <div v-if="is_auth()" id="admin-menu" @clicked="onClickChild">
        <ul>
        <li><router-link :to="{ name:'CreatePost'}">Create post</router-link></li>
        <template v-if="$route.matched.some(({ name }) => name === 'PostDetail')">
            <li><router-link :to="{ name:'EditPost', params: {id: this.$route.params.id}}">Edit post</router-link></li>
            <li><a class="brightness-hover" @click="delete_post()">Delete post</a></li>
        </template>
        </ul>
        <hr/>
        menu
    </div>
</template>

<script>
    import { is_auth } from '@/utils';

    export default {
        props: {
            delete_post: Function,
        },
        methods: {
            is_auth(){
                return is_auth();
            },
        },
    }
</script>
