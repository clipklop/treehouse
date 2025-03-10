/*
*/

// 4.


const fs = require('fs');


function mergeValues(values, content) {
  // Cycle over the keys
  for (let key in values) {
    // Replace all {{ key }} with the value from the value object
    content = content.replace(`{{ ${key} }}`, values[key])
  }
  
  // Return merged content
  return content;
}

function view(templateName, values, response) {
  // Read from the template file
  let fileContents = fs.readFileSync(`./views/${templateName}.html`, {encoding: "utf8"});
  
  // Insert values in to the content
  fileContents = mergeValues(values, fileContents);

  // Write out to the response  
  response.write(fileContents)
}


module.exports.view = view;