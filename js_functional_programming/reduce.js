/**
 * Reduce method
**/


// 1
const prices = [6.75, 3.10, 4.00, 8.12]; // Total: 21.97
const total = prices.reduce((sum, price) => sum + price, 0);


// 2
const names = ['Gary', 'Pasan', 'Gabe', 'Treasure', 'Gengis', 'Gladys', 'Tony'];
// Result: 4
const startsWithG = names.reduce((acc, cur) =>
  acc + (cur.startsWith('G') ? 1 : 0), 0
);


// 3
const phoneNumbers = ["(503) 123-4567", "(646) 123-4567", "(503) 987-6543", "(503) 234-5678", "(212) 123-4567", "(416) 123-4567"];
let numberOf503;
// numberOf503 should be: 3
// Write your code below
numberOf503 = phoneNumbers.reduce((acc, cur) => acc + (cur.slice(1, 4) === '503' ? 1 : 0), 0);
console.log(numberOf503)