<template>
    <div id="login">
        <label for="username">Login</label>
        <input type="text" name="username" v-model="input.username"/>

        <label for="password">Password</label>
        <input type="password" name="password" v-model="input.password"/>

        <button type="button" v-on:click="login()">Login</button>
    </div>
</template>


<script>

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
            if(this.input.username != "" && this.input.password != "") {
                
                let bodyContent = new FormData();
                bodyContent.append("username", this.input.username);
                bodyContent.append("password", this.input.password);

                const response = await fetch(
                    `http://127.0.0.1:8000/api/auth/login/`,
                    {
                        method: "post",
                        body: bodyContent,
                    },
                );
                const content = await response.json();
                if (response.status == 200) {
                    const storage = localStorage;
                    const expiredTime = Date.now() + content['lifetime'] * 1000;
                    storage.setItem('lifetime', content['lifetime']);
                    storage.setItem('expiredTime', expiredTime);
                    storage.setItem('token', content['token']);
                    this.$router.push({name: 'blog'});
                }
            }
        },
    },
  };
</script>