const baseUrl = useRuntimeConfig().public.baseURL;

export default {
  BASE_URL: baseUrl,
  POKEMON_ROOT_VIEW: baseUrl + 'api/pokemon',
  POKEMON_DETAIL_VIEW: (pokemon) => `${baseUrl}api/pokemon/${pokemon.id}`,
  LOGGED_IN_USER: baseUrl + 'api/me',
  FAVORITE: baseUrl + 'api/favorite_pokemon',
  UNFAVORITE: baseUrl + 'api/unfavorite_pokemon',
  FAVORITE_POKEMONS: baseUrl + 'api/favorites',
};
