$.ajax({
        url: "https://swapi.co/api/films/?format=json",
        type: 'GET',
        success: function(res) {
          for (const movie of res.results) {
            $('UL#list_movies').append(`<li>${movie.title}</li>`);
          }
        }
});