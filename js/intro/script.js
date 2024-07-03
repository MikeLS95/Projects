// const maxTemp = 28
// console.log(maxTemp)
// maxTemp = 30
// console.log(maxTemp)

// -------------------------------------------------------

// x = 'Sarah'

// {
//     console.log(x)
//     console.log(42)
//     let y = 15
// }

// console.log(y)

// -------------------------------------------------------

// let str = 'Hello World!'

// // console.log(str.indexOf('l'))
// console.log(str.slice(2, 5))

// let str = 'Hello World!'
// let name = 'Matt'

// x = str.replaceAll('o', '---')
// console.log(str)

// // Python: print(f'Hello, {name}!')
// console.log(`Hello, ${name}!`)

// -------------------------------------------------------

// function add(x, y) { return x + y }
// const add = (x, y) => x + y
// const square = (x) => x ** 2

// // console.log(typeof add)
// // console.log(add(10, 34))
// console.log(square(10))

// const number = [12, 50, 44, 32, 2]
// const result = number.map(square)
// console.log(result)

// -------------------------------------------------------

// const people = ['Matt', 'John', 'Mary', 'Kate']

// // const first = people[0]
// // const second = people[1]
// const [first, second, ...foo] = people

// console.log(first, second, foo)

// -------------------------------------------------------

// const bobBirds = ['Robin', 'Crow']
// const sallyBirds = ['Bluejay', 'Cardinal']

// //Python: bob_birds + sally_birds
// // const allBirds = bobBirds.concat(sallyBirds)
// const allBirds = [...bobBirds, ...sallyBirds, 'Kookaburra']

// console.log(allBirds)

// -------------------------------------------------------

const me = {name: 'Mike', age: 28, favouriteColour: 'green'}
const address = {city: 'Brisbane', state: 'QLD'}

const person = {...me, ...address, postcode: '4301', city: 'Sunshine Coast'}

console.log(person)