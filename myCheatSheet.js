console.log("-------------Array--------------");
console.log(...[1, 3, 4]);
console.log([1, 3, 4]);

console.log("-------------loops--------------");
xs = ["item1", "item2", "item3"];
for (var i = 0; i < xs.length; i++) {
  console.log(xs[i]);
}
xs.forEach((x, i) => console.log(x));
for (const x of xs) {
  console.log(x);
}

console.log("-------------If else--------------");
let age = 20;
if (age === 18) {
  console.log("It's your birthday !!");
} else if (age > 18) {
  console.log("We can go to a pub together !!");
} else {
  console.log("Sorry...You have to stay at home tonight");
}

console.log("-------------switch--------------");
let fruit = "Papayas";
switch (fruit) {
  case "Oranges":
    console.log("Oranges are $0.59 a pound.");
    break;
  default:
    console.log("Sorry, we are out of " + fruit + ".");
    break;
  case "Mangoes":
  case "Papayas":
    console.log("Mangoes and papayas are $2.79 a pound.");
    // expected output: "Mangoes and papayas are $2.79 a pound."
    break;
}

console.log("-------------Objects--------------");
let person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue",
};
console.log(person.firstName); // John
console.log(person["firstName"]); // John
person.firstName = "Sarah";
console.log(person.firstName); // Sarah
delete person.firstName;
console.log(person);
console.log("-------------function--------------");
console.log("-------------debugger--------------");
// Such command works only when the development tools are open, otherwise the browser ignores it.
debugger;
console.log("-------------RegEx--------------");
let str = "Happy BirthDay";
let patt = /birthday/i; //regular expression, i is a modifier (modifies the search to be case-insensitive).
let result = str.match(patt);
console.log(result); //returns true

if (result) {
  console.log("Yes");
} else {
  console.log("No");
}

let regex = /^.+@.+\..+$/;
console.log(regex.test("johndoe@gmail.com")); //returns true

console.log("-------------RegEx Dict replace vowels--------------");
var word = "AaodsifoHUHOIDHhflsakdj";
var dict = {
  a: 1,
  e: 2,
  i: 3,
  o: 4,
  u: 5,
  A: 1,
  E: 2,
  I: 3,
  O: 4,
  U: 5,
};
var pattern = /[aeiouAEIOU]/g;
solution = word.replace(pattern, (m) => dict[m]);
console.log(solution);

console.log("-------------Short-Circuiting--------------");
var person1 = {
  name: "Jack",
  age: 34,
};
console.log(person1.job || "unemployed");
// 'unemployed'
var person2 = {
  name: "Jack",
  age: 34,
};
console.log(person2.age > 18 && "Driving allowed");
// 'Driving allowed'
