<template>
    <div class="login-page">
        <h1>Login Page</h1>
        <div class="login-form">
            <div class="email-field">
                <label for="user-email">Email: </label>
                <input type="email" id="user-email" placeholder="write the registered email" v-model="this.email" required>
            </div>
            <br>
            <div class="password-field">
                <label for="user-password">Password: </label>
                <input type="password" id="user-password" placeholder="password" v-model="this.password" required>
            </div>
            <br>
            <button v-on:click="this.loginfn()">login</button> | <button v-on:click="this.$router.push({name: 'register'})">register</button>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
export default{
    name: 'LoginView',
    data() {
        return{
            email: '',
            password: ''
        };
    },
    methods: {
        loginfn(){
            axios
                .post(
                    'http://localhost:5000/login',
                    {
                        email: this.email,
                        password: this.password
                    }
                )
                .then(response => {
                    if (response.status === 200){
                    localStorage.setItem('authToken', response.data.authToken)
                    localStorage.setItem('user-email', response.data.user_email)
                    localStorage.setItem('user-role', response.data.user_role)
                    localStorage.setItem('user-id', response.data.user_id)
                    if (response.data.user_role === 'admin'){
                        this.$router.push({name: 'home'})
                        }
                    else{
                        this.$router.push({name: 'about'})
                    }
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