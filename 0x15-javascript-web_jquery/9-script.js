$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  type: 'GET',
  dataType: 'json', // added data type
  success: function (res) {
    $('DIV#hello').text(res.hello);
  }
});
