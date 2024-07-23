import express from 'express'
import mongoose from 'mongoose'
import dotenv from 'dotenv'

dotenv.config()

const categories = ['Food', 'Gaming', 'Coding', 'Other']

const entries = [
    { id: 1, category: 'Food', content: 'Pizza is yummy!' },
    { id: 2, category: 'Coding', content: 'Coding is fun!' },
    { id: 3, category: 'Gaming', content: 'War. War never changes.' }
]

mongoose.connect(process.env.DB_URI)
    .then(m => console.log(m.connection.readyState == 1 ? 'Mongoose connected' : 'Mongoose failed to connect'))
    .catch(err => console.error(err))

const Entry = mongoose.model('Entry', {
    category: {type: String, required: true},
    content: {type: String, required: true}

})

const app = express()

// Middleware
app.use(express.json())

// Flask
// @app.route('/')
// def home():
//     return {'info': 'Journal API'}
app.get('/', (request, response) => response.send({ info: 'Journal API!!' }))

app.get('/categories', (req, res) => res.send(categories))

app.get('/entries', (req, res) => res.send(entries))

app.get('/entries/:id', (req, res) => {
    const entry = entries.filter(e => e.id == req.params)
    if (matchingEntries.length == 1) {
        res.send(matchingEntries[0])
    } else {
        res.status(404).send({ error: 'Not found' })
    }
})

// Create new entry
app.post('/entries', async (req, res) => {
    try {
        // get the body of the request
        // console.log(req.body)
        // TODO: Validate the data
        // Create a new entry object
        // Push the entry to the array
        // entries.push(req.body) // Matt said "you never do this"
        const newEntry = await Entry.create(req.body)
        // Respond to the client with the new entry and 201 code
        res.status(201).send(newEntry)
    }
    catch (err) {
        res.status(400).send({ error: err.message })
    }
})

app.listen(4001, err => {
    if (err) {
        console.error(err)
    } else {
        console.log('Server running')
    }
})

