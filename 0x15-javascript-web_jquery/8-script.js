const apiEndpoint = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.ajax({
  type: 'GET',
  url: apiEndpoint,
  success: (movies) => {
    $.each(movies.results, (index, movie) => {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    });
  }
});
