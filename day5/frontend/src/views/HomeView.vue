<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/>  -->
     <div class="no-category" v-if="!this.categories || this.categories.length === 0">
      <p>No categories available</p>
      <button v-on:click="this.$router.push({name: 'category-create'})">Add the first Category</button>
     </div>
     <table v-if="this.categories">
      <thead>
        <th>id</th>
        <th>name</th>
        <th>description</th>
        <th>status</th>
        <th>created_by</th>
        <th>updated_by</th>
        <th>created_at</th>
        <th>updated_at</th>
        <th>delete</th>
        <th>actions</th>
      </thead>
      <tbody>
        <tr v-for="category in categories">
          <td>{{ category.id }}</td>
          <td>{{ category.name }}</td>
          <td>{{ category.description }}</td>
          <td>{{ category.status }}</td>
          <td>{{ category.created_by }}</td>
          <td>{{ category.updated_by }}</td>
          <td>{{ category.created_at }}</td>
          <td>{{ category.updated_at }}</td>
          <td>{{ category.delete }}</td>
          <td>
            <button v-on:click="this.$router.push({name: 'category-update', params: {id: category.id}})">Edit</button> | 
            <button v-on:click="this.categoryDelete(category.id, category.delete)"><span v-if="category.delete === false">Delete</span><span v-else>Restore</span></button>
          </td>
        </tr>
      </tbody>
     </table>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios';

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  },
  data(){
    return{
      token: '',
      role: '',
      categories: ''
    }
  },
  created(){
    this.token = localStorage.getItem('authToken')
    if (this.token === '' || this.token === null){
      localStorage.clear()
      this.$router.push({name: 'login'})
    }
    this.role = localStorage.getItem('user-role')
    if (this.role !== 'admin'){
      alert('Accessing a restrcited page is not allowed')
      localStorage.clear()
      this.$router.push({name: 'login'})
    }
    this.get_category_data()
  },
  methods: {
    get_category_data(){
      axios
          .get(
            'http://localhost:5000/api/category',
            {
              headers: {
                Authorization: this.token
              }
            }
          )
          .then(response => {
            this.categories = response.data.category_data;            
          })
          .catch(error => {
            console.log(error.response.data);
            
          })
    },
    categoryDelete(id, deleteStatus) {
      const message_1 = 'Are you sure you want to delete this category?';
      const message_2 = 'Are you sure you want to restore this category?';
      if (confirm(deleteStatus === false ? message_1 : message_2)) {
        axios.delete(
          `http://localhost:5000/api/category/${id}`,
          {
            headers: {
              Authorization: this.token
            }
          }
        )
        .then(response => {
          if (response.status === 201) {
            alert(response.data.message + ' with id: ' + response.data.id);
            this.get_category_data(); // Refresh the category list
          }
        })
        .catch(error => {
          alert("Failed to delete the category.");
        });
      }
    }
  }
}
</script>
