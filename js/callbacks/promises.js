// const x = 2
// const y = 'string'

// function adder(a, b) {
//     return a + b
// }

// const calc = new Promise((resolve, reject) => {
//     if (typeof x === 'number' && typeof y === 'number') {
//         const answer = adder(x, y)
//         resolve(answer)
//     } else {
//         reject('x and y must be numbers')
//     }
// })

// calc
//     .then(value => console.log(value))
//     .catch(err => console.log(err))

// console.log('This happens without waiting for the promise or the then callback')

function adder(a, b) {
    return a + b
}

function adderPromise(x, y) {
    return new Promise((resolve, reject) => {
        if (typeof x === 'number' && typeof y === 'number') {
            const answer = adder(x, y)
            resolve(answer)
        } else {
            reject('x and y must be numbers')
        }
    })
}

// adderPromise(10, 20)
//     .then(value => {
//         adderPromise(value, 5)
//             .then(value => console.log(value))
//     })
//     .then(value => console.log)
//     .catch(err => console.log(err))

adderPromise(10, 20)
    .then(value => adderPromise(value, 5))
    .then(value => console.log(value))
    .catch(err => console.log(err))

console.log('This happens without waiting for the promise or the then callback')