import { defineStore } from "pinia";
import * as userAPI from "../api/userAPI";

export const useUserStore = defineStore("user", {
  state: () => ({
    users: [],
    loading: false,
    error: null,
  }),

  actions: {
    async fetchUsers() {
      const response = await userAPI.fetchAllUsers();
      // console.log(response.data);

      this.users = response.data;
    },

    // async createUser(user) {
    //   try {
    //     const response = await axios.post('http://localhost:5000/users', user)
    //     this.users.push(response.data)
    //   } catch (error) {
    //     this.error = error.response?.data || 'Failed to create user'
    //   }
    // },

    // async updateUser(id, updatedUser) {
    //   try {
    //     const response = await axios.put(`http://localhost:5000/users/${id}`, updatedUser)
    //     const index = this.users.findIndex(u => u.id === id)
    //     if (index !== -1) this.users[index] = response.data.user
    //   } catch (error) {
    //     this.error = error.response?.data || 'Failed to update user'
    //   }
    // },

    // async deleteUser(id) {
    //   try {
    //     await axios.delete(`http://localhost:5000/users/${id}`)
    //     this.users = this.users.filter(u => u.id !== id)
    //   } catch (error) {
    //     this.error = error.response?.data || 'Failed to delete user'
    //   }
    // }
  },
});
