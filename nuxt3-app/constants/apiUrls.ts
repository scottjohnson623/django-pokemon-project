const baseUrl = useRuntimeConfig().public.baseURL

export default {
  POKEMON_ROOT_VIEW: baseUrl + 'api/pokemon',
  POKEMON_DETAIL_VIEW: (pokemon) => `${baseUrl}api/pokemon/${pokemon.id}`,
  LOGGED_IN_USER: 'api/me',
  FAVORITE: 'api/favorite_pokemon',
  UNFAVORITE: 'api/unfavorite_pokemon',
}
