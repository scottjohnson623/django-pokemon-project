import { defineStore } from 'pinia';
import { makeApiCall } from '~~/utils/apiUtil';

export const useAuthStore = defineStore('auth', {
  state: () => ({ user: null }),
  actions: {
    refreshUser() {
      makeApiCall('http://localhost:8000/api/me')
        .then((user) => {
          if (user) {
            this.user = user;
          } else {
            this.user = null;
          }
        })
        .catch((e) => console.error(e));
    },
  },
});
