<template>
    <div id="login">
        <h1>Login</h1>
        <input type="text" name="username" v-model="input.username" placeholder="Username" />
        <input type="password" name="password" v-model="input.password" placeholder="Password" />
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
                localStorage.token = await content['token'];
            }
        }

        // login: async function () {
        //     const { username, password } = this
            
        //     const response = await fetch(
        //             `http://127.0.0.1:8000/api/auth/login/`, 
        //             {
        //                 method: "post",
        //                 body: {
        //                     username: username,
        //                     password: password,
        //                 },
        //                 headers:{ 
        //                     'Content-Type': 'multipart/form-data',
        //                 }
        //             },
        //         );
        //     console.log(await response.json())
        // }
    }
  };
</script>