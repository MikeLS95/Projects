// function adder(x, y, callback) {
//     setTimeout(() => { callback (x + y) }, 1000)
// }

// adder(5, 10, answer => console.log(`Answer: ${answer}`))

// console.log('Done')

// const req = new XMLHttpRequest()

// req.addEventListener('load', e => console.log(e.target))

// req.open('GET', 'https://icanhazdadjoke.com/')
// req.setRequestHeader('Accept', 'application/json')
// req.responseType ='json'
// req.send()

// console.log('Request Sent!')

// ----------------------------------------------------------------

// function getJoke(cb) {
//     const req = new XMLHttpRequest()
//     req.open('GET', 'https://icanhazdadjoke.com/')
//     req.setRequestHeader('Accept', 'application/json')
//     req.responseType ='json'
//     req.addEventListener('load', e => cb(e.target.response.joke))
//     req.send()
// }

function getJoke() {
    return new Promise((resolve, reject) => {
        const req = new XMLHttpRequest()
        req.open('GET', 'https://icanhazdadjoke.com/')
        req.setRequestHeader('Accept', 'application/json')
        req.responseType ='json'
        req.addEventListener('load', e => {
            if (e.target.response.joke) {
                resolve(e.target.response.joke)
            } else {
                reject('Invalid response')
            }
        })
        req.send()
    })
}

function fetchJoke() {
    fetch('https://icanhazdadjoke.com/', {
        headers: {
            'Accept': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data => console.log(data))
}

fetchJoke()

// const jokePromises = []

// // Get 3 jokes
// for (let i = 0; i < 3; i++) {
//     jokePromises.push(getJoke())
// }

// getJoke()
//     .then(joke => {
//         jokes.push(joke)
//         return getJoke()
//     })
//     .then(joke => {
//         jokes.push(joke)
//         return getJoke()
//     })
//     .then(joke => {
//         jokes.push(joke)
//         return getJoke()
//     })


console.log('Waiting for joke...')
// console.log(jokePromises)

// // Wait for all promises in the array to resolve,
// // then call our .then callback
// Promise.all(jokePromises).then()