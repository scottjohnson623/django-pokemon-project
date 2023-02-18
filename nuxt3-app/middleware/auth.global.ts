import { useAuthStore } from '~~/stores/auth';

export default defineNuxtRouteMiddleware((to, from) => {
  const store = useAuthStore();

  store.refreshUser();
});
