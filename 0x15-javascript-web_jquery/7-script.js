$.ajax({
        url: "https://swapi.co/api/people/5/?format=json",
        type: 'GET',
        dataType: 'json', // added data type
        success: function(res) {
          $('DIV#character').text(res.name);
        }
});