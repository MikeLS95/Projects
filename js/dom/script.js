// const el = document.querySelectorAll('li')

// console.log(el)

// const newDiv = document.createElement('div')
// newDiv.innerHTML = '<p>Lorem ipsum dolor sit amet</p>'
// document.querySelector('body').appendChild(newDiv) // .insertBefore(newDiv, document.querySelector('ul'))

// document.body.innerHTML += '<div><p>Lorem ipsum dolor sit amet</p></div>'

const items = [
    'Adding to the DOM',
    'Querying the DOM',
    'Changing the DOM',
    'Event Listeners'
]

const ul = document.querySelector('ul')

// Populate the ul with an li representing each item
// let html = ''
// for (let item of items)  {
//     html += `<li>${item}</li>`
//     // const newLi = document.createElement('li')
//     // ul.appendChild(newLi)
//     // newLi.innerText = item
// }
// ul.innerHTML = html

// const lis = items.map(item => `<li>${item}</li>`)

// ul.innerHTML = lis.join('')

document.querySelector('ul').innerHTML = items.map(item => `<li>${item}</li>`).join('')