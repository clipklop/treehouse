/* 
*/


const Profile = require("./profile.js"), renderer = require('./renderer.js'), querystring = require('querystring');

const header = {'Content-type': 'text/html'};


// 2.
function home(request, response) {
  if (request.url === "/") {
    if (request.method.toLowerCase() === 'get') {
      response.writeHead(200, header);
      renderer.view('header', {}, response);
      renderer.view('search', {}, response);
      renderer.view('footer', {}, response);
      response.end();
    } else {
      // If url == '/' && POST
      // Get the post data from body
      request.on('data', function(postBody) {
        // Extract the username
        let query = querystring.parse(postBody.toString())
        // Redirect to /:username
        response.writeHead(303, {"Location": `/${query.username}`});
        response.end();

        
      })
    }
  }
}


// 3. 
function user(request, response) {
  let username = request.url.replace('/', '');
  if (username.length > 0) {
    response.writeHead(200, header);
    renderer.view('header', {}, response);

    const studentProfile = new Profile(username);
    studentProfile.on('end', function(profileJSON) {
      // show profile
      const values = {
       avatarUrl: profileJSON.gravatar_url,
       username: profileJSON.profile_name,
       badges: profileJSON.badges.length,
       javascriptPoints: profileJSON.points.JavaScript
      }
      renderer.view('profile', values, response);
      renderer.view('footer', {}, response);
      response.end();
    });

    studentProfile.on('error', function(error) {
      // show error
      renderer.view('error', {errorMessage: error.message}, response);   
      renderer.view('search', {}, response);
      renderer.view('footer', {}, response);
      response.end();
    });
    
  }
}


module.exports.home = home;
module.exports.user = user;