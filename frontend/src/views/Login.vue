<template>
  <div>
    <h2>Login</h2>
    <!-- <form @submit.prevent="handleLogin">
      <input v-model="username" placeholder="Username" />
      <input v-model="password" type="password" placeholder="Password" />
      <button type="submit">Login</button>
    </form> -->
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    // async handleLogin() {
    //   try {
    //     const res = await axios.post('http://localhost:8000/api/users/login', {
    //       username: this.username,
    //       password: this.password
    //     });
    //     alert('Login successful!');
    //   } catch (err) {
    //     alert('Login failed');
    //   }
    // }
  }
};
</script>
