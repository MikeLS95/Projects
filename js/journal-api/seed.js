import mongoose from 'mongoose'
import { Entry, Category } from "./db.js"

const categories = [
    { name: 'Food' },
    { name: 'Gaming'},
    { name: 'Coding'},
    { name: 'Other'}
]

const entries = [
    { id: 1, category: 'Food', content: 'Pizza is yummy!' },
    { id: 2, category: 'Coding', content: 'Coding is fun!' },
    { id: 3, category: 'Gaming', content: 'War. War never changes.' }
]

await Category.deleteMany()
console.log('Deleted Categories')
await Category.insertMany(categories)
console.log('Added Categories')

await Entry.deleteMany()
console.log('Deleted Entries')
await Entry.insertMany(entries)
console.log('Added Entries')

mongoose.disconnect()