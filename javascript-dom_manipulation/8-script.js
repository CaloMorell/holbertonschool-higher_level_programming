$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (query) {
  $('#hello').text(query.hello);
});
