import mongoose from 'mongoose'
import dotenv from 'dotenv'

dotenv.config()

mongoose.connect(process.env.DB_URI)
    .then(m => console.log(m.connection.readyState == 1 ? 'Mongoose connected' : 'Mongoose failed to connect'))
    .catch(err => console.error(err))

const Entry = mongoose.model('Entry', {
    category: {type: String, required: true},
    content: {type: String, required: true}
})

const Category = mongoose.model('Category', {
    name: { type: String, required: true }
})

export { Entry, Category }
