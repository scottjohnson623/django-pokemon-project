import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({ user: null }),
  actions: {
    refreshUser() {
      $fetch('http://localhost:8000/api/me', { credentials: 'include' }).then(
        (user) => {
          if (user) {
            this.user = user
          } else {
            this.user = null
          }
        }
      )
    },
  },
})
