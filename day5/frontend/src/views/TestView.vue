<template>
    <div class="test-page">
        <h1>Test Page<span v-if="this.responseData"> - {{ this.responseData }}</span></h1>
        <p>This is a test page to demonstrate Vue.js<span v-if="this.responseData"> and flask</span> functionality.</p>
        <p>Feel free to modify this page as needed.</p>
        <div class="testPageField">
            <label for="testPageTextField">Data: </label>
            <input type="text" placeholder="Enter something here..." id="testPageTextField" v-model="this.testData"/>
            <button v-on:click="this.printData()">print it in the console</button>
        </div>
        <br>
        var: {{ this.testData }} {{ this.responseData }} <br><br>
        <!-- <button v-on:click="this.doSomething()">do something</button> -->
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'TestView',
    data() {
        return {
            testData: '',
            responseData: null,
        };
    },
    created(){
        console.log('test view created');
        this.doSomething();
    },
    methods: {
        printData() {
            console.log(this.testData);
        },
        doSomething() {
            console.log("doSomething() called");
            axios
                .get('http://localhost:5000/')
                .then(response => {
                    // console.log("response http code: ", response.status);
                    // console.log("response: ", response);
                    this.responseData = response.data;
                })
                .catch(error => {
                    console.log("error http code: ", error.status);
                    console.log("error: ", error);
                })
        }
    },
};
</script>

<style>

</style>