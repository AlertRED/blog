<template>
    <div id="login">
        <label for="username">Login</label>
        <input type="text" name="username" v-model="input.username" />

        <label for="password">Password</label>
        <input type="password" name="password" v-model="input.password" />

        <button type="button" v-on:click="login()">Login</button>
    </div>
</template>


<script>

import "./auth.css";
import { parse_response, throw_body, get_bearer } from '@/utils';

export default {
    data() {
        return {
            input: {
                username: "",
                password: ""
            }
        }
    },
    methods: {
        async login() {
            if (this.input.username != "" && this.input.password != "") {

                let fromBody = new FormData();
                fromBody.append("username", this.input.username);
                fromBody.append("password", this.input.password);

                const response = await fetch(
                    `${import.meta.env.VITE_BASE_API_URL}/auth/login/`,
                    {
                        method: "post",
                        body: fromBody,
                        headers: {
                            Authorization: get_bearer(),
                        },
                    },
                ).then(response => parse_response(response));

                if (response.status === 200){
                    const expiredTime = Date.now() + response.body.lifetime * 1000;
                    localStorage.setItem('expiredTime', expiredTime);
                    localStorage.setItem('lifetime', response.body.lifetime);
                    localStorage.setItem('token', response.body.token);
                    this.$router.push({ name: 'Blog' });
                } else
                    throw_body(response.body)
            }
        },
    },
};
</script>