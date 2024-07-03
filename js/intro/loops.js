// Python
// count = 4
// while count > 0:
//     print(count)
//     count -= 1

// let count = 4
// while (count > 0) {
//     console.log(count--)
// }

// -------------------------------------------------------

// Python 
// for i in range(10):
//     print(i)

// 3-part for loop
// initializer: runs once, before the first iteration
// condition: will be tested before every iteration
// post-iteration: will be evaluated after every iteration

// for (initializer; condition post-iteration) {}

// for (let i=0; i < 10; ++i) {
//     console.log(i)
// }

// -------------------------------------------------------

// Fibonacci
// const fib = [1]
// for (let prev=1, next=1; next <= 1000; tmp=next, next=prev+next, prev=tmp) {
//     fib.push(next)
// }

// console.log(fib)

// -------------------------------------------------------

const favFoods = ['pizza', 'pasta', 'tacos']

// Python
// for food in favFoods:
//     print(food)

// for (let food of favFoods) {
//     console.log(food)
// }
favFoods.forEach((food, index) => {
    console.log(`${index+1}. ${food}`)
})

favFoods.forEach(food => console.log(food))