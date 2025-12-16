//object
let user = {
  name: "John",
  age: 25,
  isAdmin: true
};
console.log(user)//{ name: 'John', age: 25, isAdmin: true }
//set
let numbers = new Set([1, 2, 2, 3]);
numbers.add(4);
console.log(numbers)//Set(4) { 1, 2, 3, 4 }
//map
let map = new Map();
map.set("name", "Alice");
map.set(1, "One");
console.log(map)
//stack
let stack = [];
stack.push(10);
stack.push(5)
// stack.pop();
console.log(stack)
// =================
const visited = new WeakSet();

let page = { url: "/home" };
visited.add(page);

console.log(visited.has(page)); // true

page = null; // eligible for garbage collection

let numbers1 = new Set([]);
numbers1.add(1);
numbers1.add(2);
numbers1.add(3);
console.log(numbers1)

