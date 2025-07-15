<template>
    <div class="register-page">
        <h1>Register Page</h1>
        <div class="register-form">
            <div class="email-field">
                <label for="user-email">Email: </label>
                <input type="email" id="user-email" placeholder="write the registered email" v-model="this.email" required>
            </div>
            <br>
            <div class="username-field">
                <label for="user-name">Username: </label>
                <input type="text" id="user-name" placeholder="write the username" v-model="this.username" required>
            </div>
            <br>
            <div class="password-field">
                <label for="user-password">Password: </label>
                <input type="password" id="user-password" placeholder="password" v-model="this.password" required>
            </div>
            <br>
            <button v-on:click="this.registerfn()">register</button> | <button v-on:click="this.$router.push({name: 'login'})">login</button>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
export default{
    name: 'RegisterView',
    data() {
        return{
            email: '',
            password: '',
            username: ''
        };
    },
    methods: {
        registerfn(){
            axios
                .post(
                    'http://localhost:5000/register',
                    {
                        email: this.email,
                        password: this.password,
                        username: this.username
                    }
                )
                .then(response => {
                    if (response.status === 201){
                    this.$router.push({name: 'login'})
                    }
                    else{
                        alert(response.data.message)
                    }
                })
                .catch(error => {
                    console.log('error', error)
                    console.log('error-response', error)
                })
            
        }
    }
}
</script>