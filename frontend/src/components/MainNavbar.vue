<template>
    <header>
        <div id="toolbar">
            <ul id="menu">
                <li><router-link :class="`brightness-hover`" :to="{ name:'About'}">About</router-link></li>
                <li><router-link :class="`brightness-hover`" :to="{ name:'Blog'}">Blog</router-link></li>
                <li><router-link :class="`brightness-hover`" :to="{ name:'Categories'}">Categories</router-link></li>
                <li><a :class="`brightness-hover`" :href="'./CV.pdf'" target="_blank">CV <sup>(pdf)</sup></a></li>
            </ul>
            <div 
                id="change-theme"
                @click="() => { theme_name = (theme_name == 'light' ? 'dark' : 'light') }"
            >
                <div :class="{ 'icon-weather-sunny moved': theme_name == 'light', 'icon-moon-o': theme_name == 'dark', }">
                </div>
            </div>
        </div>
    </header>
</template>

<script>
export default { 
    data() {
        return {
            theme_name: localStorage['theme'] || "light",
        }
    },
    mounted() {
        window.addEventListener("storage", this.onStorageUpdate);
        this.setTheme(this.theme_name);
    },
    watch: {
        theme_name(newName) {
            localStorage.theme = newName;
            this.setTheme(this.theme_name);
        }
    },
    methods: {
        onStorageUpdate(event) {
            if (event.key === "theme") {
                this.theme_name = event.newValue;
            }
        },
        setTheme(theme_name){
            const css = document.createElement('style')
            css.type = 'text/css'
            css.appendChild(
                document.createTextNode(
                    `* {
                    -webkit-transition: none !important;
                    -moz-transition: none !important;
                    -o-transition: none !important;
                    -ms-transition: none !important;
                    transition: none !important;
                    }`
                )
            )
            document.head.appendChild(css)  

            document.documentElement.setAttribute('theme', theme_name);

            const _ = window.getComputedStyle(css).opacity
            document.head.removeChild(css)
        }
    },
    beforeDestroy() {
        window.removeEventListener("storage", this.onStorageUpdate);
    },
}
</script>