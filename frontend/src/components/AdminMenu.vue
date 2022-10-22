<template>
    <div v-if="is_auth()" id="admin-menu" @clicked="onClickChild">
        <ul>
        <li><router-link :to="{ name:'CreateNote'}">Create note</router-link></li>
        <template v-if="$route.matched.some(({ name }) => name === 'NoteDetail')">
            <li><router-link :to="{ name:'EditNote', params: {id: this.$route.params.id}}">Edit note</router-link></li>
            <li><a class="brightness-hover" @click="delete_note()">Delete note</a></li>
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
            delete_note: Function,
        },
        methods: {
            is_auth(){
                return is_auth();
            },
        },
    }
</script>
