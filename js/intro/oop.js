// Python
// class Person:
//     def __init__(self, name, age):
//         self.name = name
//         self.age = age
//
// person = Person('Mike', 28)

// const person = {
//     name: 'Mike',
//     age: 28,
// }

// function Person(name, age) {
//     this.name = name
//     this.age = age

//     this.greet = () => {
//         console.log(`${this.name} is ${this.age} years old!`)
//     }
// }

// class Person {
//     constructor(name, age) {
//         this.name = name
//         this.age = age
//     }

//     greet() {
//         console.log(`${this.name} is ${this.age} years old!`)
//     }
// }

// // Main
// const person = new Person('Mike', 28)
// person.age = 29
// person.greet()
// console.log(person.age)

class Rectangle {
    #width
    #height

    constructor(width, height) {
        this.#width = width
        this.#height = height
    }

    get width() { return this.#width }

    set width(value) {
        if (typeof value === 'number') {
            this.#width = value
        } else {
            // Raise exception
            console.error('Invalid value - must be a number')
        }
    }

    get area() {
        return this.#width * this.#height
    }
}

class Square extends Rectangle {
    #width
    #height

    constructor(size=5) {
        super(size, size)
    }
}

const rect = new Square(10)
console.log(rect.area)