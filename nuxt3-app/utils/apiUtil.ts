import Cookies from 'js-cookie';

export const makeApiCall = (url, method = 'GET', body = null) => {
  const csrfToken = Cookies.get('csrftoken');
  return $fetch(url, {
    method,
    credentials: 'include',
    body,
    headers: {
      'X-CSRFToken': csrfToken,
    },
  });
};
