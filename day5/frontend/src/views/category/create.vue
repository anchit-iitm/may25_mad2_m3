<template>
    <div class="create-category">
        <h1>Create New Category</h1>
        <form>
            <div class="form-group">
                <label for="categoryName">Category Name:</label>
                <input type="text" id="categoryName" v-model="category.name" required />
            </div>
            <br>
            <div class="form-group">
                <label for="categoryDescription">Description:</label>
                <textarea id="categoryDescription" v-model="category.description"></textarea>
            </div>
        </form>
        <button v-on:click="this.addCategory()">Create Category</button>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    name: 'CreateCategory',
    data() {
        return {
            category: {
                name: '',
                description: ''
            },
            token:'',
            role: ''
        };
    },
    created() {
        this.token = localStorage.getItem('authToken');
        if (!this.token) {
            alert("You must be logged in to create a category.");
            this.$router.push({ name: 'login' });
        }
        this.role = localStorage.getItem('user-role');
        if (this.role !== 'admin') {
            alert("You do not have permission to create a category.");
            this.$router.push({ name: 'home' });
        }
    },
    methods: {
        addCategory() {
            axios.post(
                'http://localhost:5000/api/category', 
                this.category,
                {
                    headers: {
                        Authorization: this.token
                    }
                })
                .then(response => {
                    if (response.status === 201) {
                        alert("Category created successfully!");
                        this.$router.push({ name: 'home' });
                    }
                })
                .catch(error => {
                    alert("Error creating category: " + error.response.data.message || error.message);
                });
        }
    }
};
</script>