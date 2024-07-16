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

function getJoke(cb) {
    const req = new XMLHttpRequest()
    req.open('GET', 'https://icanhazdadjoke.com/')
    req.setRequestHeader('Accept', 'application/json')
    req.responseType ='json'
    req.addEventListener('load', e => cb(e.target.response.joke))
    req.send()
}

getJoke(joke => console.log(joke))

console.log('Waiting for joke...')