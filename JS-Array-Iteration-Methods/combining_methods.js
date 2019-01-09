/**
 * Combining Array Methods: .map .filter .reduce
 */


// 1. Remove duplicates
const numbers = [1, 1, 2, 3, 4, 3, 5, 5, 6, 7, 3, 8, 9, 10];
const unique = numbers.filter((number, index, array) => index === array.indexOf(number)
);
// console.log(unique); // => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


// 2. Using filter and map
const years = [1989, 2015, 2000, 1999, 2013, 1973, 2012];
let displayYears;
// displayYears should be: ["2015 A.D.", "2013 A.D.", "2012 A.D."]
// Write your code below
displayYears = years.filter((year) => year > 2000 ? year : 0).map((year) => `${year} A.D.`);
// console.log(displayYears)


// 3.
const users = [
  {name: 'Samir', age: 21},
  {name: 'Angela', age: 39},
  {name: 'Beatrice', age: 42}
];
const filteredUsers = users.filter((user) => user.name !== 'Samir' ? user.name : 0);

const stringify = users.map(user => `${user.name} is ${user.age} years old.`);

const objectify = users.reduce((acc, cur) => { 
  acc[cur.name] = cur.age;
  return acc;
}, {});
// console.log(objectify)


// 4.
const authors = [
  { firstName: "Beatrix", lastName: "Potter" },
  { firstName: "Ann", lastName: "Martin" },
  { firstName: "Beverly", lastName: "Cleary" },
  { firstName: "Roald", lastName: "Dahl" },
  { firstName: "Lewis", lastName: "Carroll" }
];
let fullAuthorNames;
// fullAuthorNames should be: ["Beatrix Potter", "Ann Martin", "Beverly Cleary", "Roald Dahl", "Lewis Carroll"]
// Write your code below
fullAuthorNames = authors.map(author => `${author.firstName} ${author.lastName}`);


// 5.
const userNames = ['Samir', 'Angela', 'Beatrice', 'Shaniqua', 'Marvin', 'Sean'];
// Result: [{name: 'Samir'}, {name: 'Shaniqua'}, {name:'Sean'}];
const userStarsWithS = userNames
  .filter(user => user.charAt(0) === 'S')
  .map(name => ({name: name}));


// 6.
const newUsers = [
  {name: 'Samir', age: 27},
  {name: 'Angela', age: 33},
  {name: 'Beatrice', age: 42},
  {name: 'Shaniqua', age: 30},
  {name: 'Marvin', age: 23},
  {name: 'Sean', age: 47}
];
// Result: ['Angela', 'Beatrice', 'Shaniqua', 'Sean'];
const under30 = newUsers.filter(user => user.age >= 30).map(user => user.name);


// 7.
const todos = [
  {
      todo: 'Buy apples',
      done: false
  },
  {
      todo: 'Wash car',
      done: true
  },
  {
      todo: 'Write web app',
      done: false
  },
  {
      todo: 'Read MDN page on JavaScript arrays',
      done: true
  },
  {
      todo: 'Call mom',
      done: false
  }
];
let unfinishedTasks;
// unfinishedTasks should be: ["Buy apples", "Write web app", "Call mom"]
// Write your code below
unfinishedTasks = todos.filter(todo => !todo.done).map(todo => todo.todo);


// 8.
const products = [
  { name: 'hard drive', price: 59.99 },
  { name: 'lighbulbs', price: 2.59 },
  { name: 'paper towels', price: 6.99 },
  { name: 'flatscreen monitor', price: 159.99 },
  { name: 'cable ties', price: 19.99 },
  { name: 'lolypop', price: 9.99 },
  { name: 'ballpoint pens', price: 4.49 }
];
// Result: { name: 'paper towels', price: 6.99 }
const highestUnder10 = products
  .filter(product => product.price <= 10)
  .reduce((acc, cur) => acc.price < cur.price ? cur : acc)


// 9.
const sumOver10 = products
  .filter(product => product.price >= 10)
  .reduce((acc, cur) => acc + cur.price, 0).toFixed(2)


// 10.
const purchaseItems = [
  {
      name: 'apples',
      dept: 'groceries',
      price: 2.49
  },
  {
      name: 'bread',
      dept: 'groceries',
      price: 2.99
  },
  {
      name: 'batteries',
      dept: 'electronics',
      price: 5.80
  },
  {
      name: 'eggs',
      dept: 'groceries',
      price: 3.99
  },
  {
      name: 't-shirts',
      dept: 'apparel',
      price: 9.99
  }
];
let groceryTotal;
// groceryTotal should be: 9.47
// Write your code below
groceryTotal = purchaseItems
  .filter(item => item.dept === 'groceries')
  .reduce((acc, cur) => acc + cur.price, 0)


// 11.
const movies = [
  ['The Day the Earth Stood Still', 'Superman', 'Ghostbusters'],
  ['Finding Dory'],
  ['Jaws', 'On the Waterfront']
]
// Result: ['The Day the Earth Stood Still', 'Superman', 'Ghostbusters', 'Finding Dory', 'Jaws', 'On the Waterfront']
const flatMovies = movies.reduce((arr, cur) => [...arr, ...cur], []);


// 12.
const objectUsers = [
  {
    name: 'Samir',
    age: 27,
    favoriteBooks:[
      {title: 'The Iliad'},
      {title: 'The Brothers Karamazov'}
    ]
  },
  {
    name: 'Angela',
    age: 33,
    favoriteBooks:[
      {title: 'Tenth of December'},
      {title: 'Cloud Atlas'},
      {title: 'One Hundred Years of Solitude'}
    ]
  },
  {
    name: 'Beatrice',
    age: 42,
    favoriteBooks:[
      {title: 'Candide'}
    ]
  }
];
// Result: ['The Iliad', 'The Brothers Karamazov', 'Tenth of December', 'Cloud Atlas', 'One Hundred Years of Solitude', 'Candide'];
const books = objectUsers.map(user => user.favoriteBooks.map(book => book.title))
  .reduce((acc, cur) => [...acc, ...cur], [])
console.log(books)