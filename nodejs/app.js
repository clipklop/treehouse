/*
  # Problem: We need a simple way to look at a user's
             badge count and JS point from a web browser.
  # Solution: Use Node.js to perform the profile 
  # Plan: 
    1. Create a web server

    2. Handle HTTP route get / and POST / i.e. Home
      if url == '/' && GET:
        show search
      if else url == '/' && POST:
        redirect to /:username
      
    3. Handle HTTP route GET /:username
      if url == '/...'
        get JSON from Treehouse
          on 'end'
            show profile
          on 'error'
            show error
    
    4. Function that handles the reading of files and
    merge in value
      read from file and get a string
        merge values in to strings
*/


// 1.
const http = require('http'), server = '127.0.0.1', port = 1337;

http.createServer(function (request, response) {
  homeRoute(request, response)
}).listen(port, server);

function homeRoute(request, response) {
  if (request.url === "/") {
    response.writeHead(200, {'Content-type': 'text/plain'});
    response.write('Header: \n');
    response.write('Search: \n');
    response.write('Footer: \n');    
    response.end('')
  }
}

console.log('Server runnig at http://' +server+ ':' +port)