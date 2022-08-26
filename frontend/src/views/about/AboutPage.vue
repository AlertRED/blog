<template>
    <div id="about-me">
        <h3>About me</h3>
        <div>
            My name is Alexander, I am a Python web application developer mainly.
            I am also in love with science and learning.
            I have a bachelor's degree from the Don State Technical University and a master's degree from the Harbin
            Institute of Technology.
            Also I want to get my PhD in China in the future, preferably.
        </div>
    </div>
    <div id="skills">
        <h3>Main skills</h3>
        <ul>
            <li>Python</li>
            <li>Django</li>
            <li>Flask</li>
            <li>Vue</li>
        </ul>
    </div>
    <div id="accounts">
        <h3>Social accounts & Contacts</h3>
        <ul>
            <li @click="go_telegram">
                <span class="icon-paper-plane icon-contact"></span>
                <span class="social-name">Telegram</span>
                <span class="social-contact">@saboteur_man</span>
            </li>
            <li @click="go_github">
                <span class="icon-github-alt icon-contact"></span>
                <span class="social-name">GitHub</span>
                <span class="social-contact">AlertRed</span>
            </li>
            <li>
                <span class="icon-weixin icon-contact"></span>
                <span class="social-name">WeChat</span>
                <span class="social-contact">merovingiann</span>
            </li>
            <li @click="go_email">
                <span class="icon-envelope-o icon-contact"></span>
                <span class="social-name">E-mail</span>
                <span class="social-contact">drammtv@gmail.com</span>
            </li>
        </ul>
    </div>

</template>
    
<script>
import "./about.css";

export default {
    methods: {
        go_telegram() {
            window.open('https://t.me/saboteur_man', '_blank');
        },
        go_github() {
            window.open('https://github.com/AlertRED', '_blank');
        },
        go_email() {
            window.open('mailto:drammtv@gmail.com', '_blank');
        },
    },
}
</script>