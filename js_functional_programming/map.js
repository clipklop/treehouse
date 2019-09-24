/**
 * Map method
**/


// 1
const strings = ['1','2','3','4','5','6']
const numbers = strings.map(number => parseInt(number, 10))


// 2
const fruits = ['apple', 'pear', 'cherry'];
let capitalizedFruits = fruits.map(fruit => fruit.toUpperCase());


// 3
const prices = [5, 4.23, 6.4, 8.09, 3.20];
const parsedPrices = prices.map(price => `$${parseFloat(price).toFixed(2)}`);
// Result: [ '$5.00', '$4.23', '$6.40', '$8.09', '$3.20' ]


// 4
const daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
let abbreviatedDays;
// abbreviatedDays should be: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
// Write your code below
abbreviatedDays = daysOfWeek.map(day => day.slice(0,3))
console.log(abbreviatedDays)