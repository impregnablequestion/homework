// EPISODE 1

// const scenario = {
//         murderer: 'Miss Scarlet',
//         room: 'Library',
//         weapon: 'Rope'
//     };
    
//     const declareMurderer = function() {
//         return `The murderer is ${scenario.murderer}.`;
//     }
    
//     const verdict = declareMurderer();
//     console.log(verdict);

/*
Running this code should produce the string "The murderer is Miss Scarlet."
The object scenario has been defined with the key "murderer" corresponding to the value 'Miss Scarlet',
When the function expression "declareMurderer"  is run to obtain the verdict it will then produce a string with
that value in it, which the console then prints
*/

// EPISODE 2

// const murderer = 'Professor Plum';

// const changeMurderer = function() {
//   murderer = 'Mrs. Peacock';
// }

// const declareMurderer = function() {
//   return `The murderer is ${murderer}.`;
// }

// changeMurderer();
// const verdict = declareMurderer();
// console.log(verdict);

/*
Running this code should produce an error, as we have defined the variable as a constant initially and so
when we call the function 'changeMurderer' that will fail as it cannot reassign the value to 'Mrs. Peacock'
*/

// EPISODE 3

// let murderer = 'Professor Plum';

// const declareMurderer = function() {
//   let murderer = 'Mrs. Peacock';
//   return `The murderer is ${murderer}.`;
// }

// const firstVerdict = declareMurderer();
// console.log('First Verdict: ', firstVerdict);

// const secondVerdict = `The murderer is ${murderer}.`;
// console.log('Second Verdict: ', secondVerdict);

/*
In this example, the console will print different statements for firstVerdict and secondVerdict.
firstVerdict will print "The murderer is Mrs. Peacock", and secondVerdict will print "The murder is Professor Plum".
This is because we can use the let verdict to redeclare a variable value within a specific block of code. So within the function
declare Murderer the murder is 'Mrs Peaccok, and hence the first verdict which is a result of that function will declare that.

However the second verdict is simply defined as a string containing the variable murderer, which we defined outside of that function as 'Professor Plum'
*/

// EPISODE 4

// let suspectOne = 'Miss Scarlet';
// let suspectTwo = 'Professor Plum';
// let suspectThree = 'Mrs. Peacock';

// const declareAllSuspects = function() {
//   let suspectThree = 'Colonel Mustard';
//   return `The suspects are ${suspectOne}, ${suspectTwo}, ${suspectThree}.`;
// }

// const suspects = declareAllSuspects();
// console.log(suspects);
// console.log(`Suspect three is ${suspectThree}.`);

/*
When the console prints 'suspects' in this examle, which is defined as the function 'declareAllSuspects', it will print
'The suspects are Miss Scarlet, Professor Plum, and Colonel Mustard'. The first two suspects will have been defined outside of the function
but the third has been redefined inside of the function, which is perfectly acceptable when we use 'let' to define variables.
When the console prints after that, it will print 'Suspect three is Mrs Peacock', because that variable has only been redefined within the 
scope of the 'declareAllSuspects' function
*/

// EPISODE 5

// const scenario = {
//     murderer: 'Miss Scarlet',
//     room: 'Kitchen',
//     weapon: 'Candle Stick'
//   };
  
//   const changeWeapon = function(newWeapon) {
//     scenario.weapon = newWeapon;
//   }
  
//   const declareWeapon = function() {
//     return `The weapon is the ${scenario.weapon}.`;
//   }
  
//   changeWeapon('Revolver');
//   const verdict = declareWeapon();
//   console.log(verdict);

/*
When we print the verdict at the end here, it should print 'The weapon is the Revolver'.
This is because we can redefine the value for the key of a constant object without any issue.
So to change scenarios 'weapon' to another key or remove it would throw up an error, but we can change the weapon from 
candlestick to revolver with no issues using the changeweapon function.
*/

// EPISODE 6

// let murderer = 'Colonel Mustard';

// const changeMurderer = function() {
//     murderer = 'Mr. Green';

//     const plotTwist = function() {
//         murderer = 'Mrs. White';
//     }

//     plotTwist();
// }

// const declareMurderer = function () {
//     return `The murderer is ${murderer}.`;
// }

// changeMurderer();
// const verdict = declareMurderer();
// console.log(verdict);

/*
My guess is that doing this would 
— override the declaration of the variable initially and that declareMurderer after calling changeMurderer would
print 'The murderer is Mrs White', and that when you do this within a function you redefine the variable without redeclaring it
*/

// EPISODE 7

// let murderer = 'Professor Plum';

// const changeMurderer = function() {
//     murderer = 'Mr. Green';

//     const plotTwist = function() {
//         let murderer = 'Colonel Mustard';

//         const unexpectedOutcome = function() {
//         murderer = 'Miss Scarlet';
//         }

//         unexpectedOutcome();
//     }

//     plotTwist();
// }

// const declareMurderer = function() {
//     return `The murderer is ${murderer}.`;
// }

// changeMurderer();
// const verdict = declareMurderer();
// console.log(verdict);

/*
In this example I think the console would either print that Mr. Green was the murderer, because in the plot twist we are only locally updating the variable,
but in the root level of the change murderer function it is updating the variable globally

*/

// EPISODE 8

// const scenario = {
//     murderer: 'Mrs. Peacock',
//     room: 'Conservatory',
//     weapon: 'Lead Pipe'
//   };
  
//   const changeScenario = function() {
//     scenario.murderer = 'Mrs. Peacock';
//     scenario.room = 'Dining Room';
  
//     const plotTwist = function(room) {
//       if (scenario.room === room) {
//         scenario.murderer = 'Colonel Mustard';
//       }
  
//       const unexpectedOutcome = function(murderer) {    
//         if (scenario.murderer === murderer) {
//           scenario.weapon = 'Candle Stick';
//         }
//       }
  
//       unexpectedOutcome('Colonel Mustard');
//     }
  
//     plotTwist('Dining Room');
//   }
  
//   const declareWeapon = function() {
//     return `The weapon is ${scenario.weapon}.`
//   }
  
//   changeScenario();
//   const verdict = declareWeapon();
//   console.log(verdict);

/*
ugh haha

unexpected outcome: 

if murderer === 'Colonel Mustard'
the weapon === 'Candle Stick'

plot twist:

if room = 'Dining room"
the murderer === 'Colonel Mustard"

change scenario:

so calling change scenario
change room to dining room, murderer to mrs peacock

define plot twist:
call plot twist (dining room):
murderer is Colonel Mustard

define unexpected outcome
call unexpected outcome('colonel mustard')
weapon is candlestick

Okay so if you call change scenario and then declare weapon, the weapon should be updated to Candlestick
but this is a stupid set of nested functions.
*/

// EPISODE 9

let murderer = 'Professor Plum';

if (murderer === 'Professor Plum') {
  let murderer = 'Mrs. Peacock';
}

const declareMurderer = function() {
  return `The murderer is ${murderer}.`;
}

const verdict = declareMurderer();
console.log(verdict);

/*
the verdict will be 'The murderer is 'Professor Plum'—
the let murder = Mrs. Peacock is only the case within that if block, so when we declare the murderer it will just be what was declared previously
*/


