/* 
*/


const Profile = require("./profile.js");


// 2.
function home(request, response) {
  if (request.url === "/") {
    response.writeHead(200, {'Content-type': 'text/plain'});
    response.write('Header: \n');
    response.write('Search: \n');    
    response.end('Footer: \n');
  }
}


// 3. 
function user(request, response) {
  let username = request.url.replace('/', '');
  if (username.length > 0) {
    response.writeHead(200, {'Content-type': 'text/plain'});
    response.write('Header: \n');

    const studentProfile = new Profile(username);
    studentProfile.on('end', function(profileJSON) {
      // show profile
      const values = {
       avatarUrl: profileJSON.gravatar_url,
       username: profileJSON.profile_name,
       badges: profileJSON.badges.length,
       javascriptPoints: profileJSON.points.JavaScript
      }
      response.write(`${values.username} has ${values.badges} badges.\n`);    
      response.end('Footer: \n');
    });

    studentProfile.on('error', function(error) {
      // show error
      response.write(error.message + '\n');    
      response.end('Footer: \n');
    });
    
  }
}


module.exports.home = home;
module.exports.user = user;