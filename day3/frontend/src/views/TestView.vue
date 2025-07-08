<template>
    <div class="test-page">
        <h1>Test Page</h1>
        <p>This is a test page to demonstrate Vue.js functionality.</p>
        <p>Feel free to modify this page as needed.</p>
        <div class="testPageField">
            <label for="testPageTextField">Data: </label>
            <input type="text" placeholder="Enter something here..." id="testPageTextField" v-model="this.testData"/>
            <button v-on:click="this.printData()">print it in the console</button>
        </div>
        <br>
        var: {{ this.testData }}
    </div>
</template>

<script>
export default {
    name: 'TestView',
    data() {
        return {
            testData: '',
        };
    },
    methods: {
        printData() {
            console.log(this.testData);
        },
    },
};
</script>

<style>

</style>