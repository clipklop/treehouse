
// const grades = [4,73,67,38,33];

// function gradingStudents(grades) {
//   /*
//    * Write your code here.
//    */
//   let temp = [];
//   for (let i = 0; i < grades.length; i++) {
//     if ( (((grades[i] - grades[i]%5) + 5) - grades[i]) < 3 && grades[i] >= 38) {
//       temp.push((grades[i] - grades[i]%5) + 5);
//     } else {
//       temp.push(grades[i])
//     } 
//   }
//   return temp;
// }

// gradingStudents(grades)


const alphabet = 'abcdefghijklmnopqrstuvwxyz', string = 'middle-Outz';

function caesarCipher(s, k) {
  // Complete this function
  let tempStr = s.split(''), splitedAlphabet = alphabet.split(''), list = [];

  for (let i = 0; i < tempStr.length; i++) {
    if (tempStr.includes(splitedAlphabet[i])) {
      list.push(splitedAlphabet[i])
    }// else {
    //   list.push(tempStr[i])
    // }
  }
  console.log(list)
}

caesarCipher(string, 2)