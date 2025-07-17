<template>
    <div class="update-category">
        <h1>update a Category</h1>
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
        <button v-on:click="this.editCategory()">Update Category</button>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    name: 'UpdateCategory',
    data() {
        return {
            category: {
                name: '',
                description: ''
            },
            token:'',
            role: '',
            categoryId: ''
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
        this.categoryId = this.$route.params.id;
        if (this.categoryId){
            this.get_category()
        }
        else{
            alert('error fetching the catgory details')
        }
    },
    methods: {
        get_category(){
            axios.get(`http://localhost:5000/api/category/${this.categoryId}`, {
                headers: {
                    Authorization: this.token
                }
            })
            .then(response => {
                this.category = response.data.category_data;
            })
            .catch(error => {
                alert("Error fetching category data: " + error.response.data.message || error.message);
            });
        },
        editCategory() {
            axios.put(
                `http://localhost:5000/api/category/${this.categoryId}`, 
                this.category,
                {
                    headers: {
                        Authorization: this.token
                    }
                })
                .then(response => {
                    if (response.status === 201) {
                        alert("Category updated successfully!");
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