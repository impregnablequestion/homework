const names = ["Fred", "Maria", "Isaac", "Daisy", "Sam"];
// console.log(names);

const [fred, maria, ...remainingNames] = names;
// console.log(remainingNames);

const person = {
    name: "Joni",
    age: 76
}

// const joni = person.name
// const age = person.age

// console.log(joni);
// console.log(age);

const { name, age } = person;

console.log(name);
console.log(age)
