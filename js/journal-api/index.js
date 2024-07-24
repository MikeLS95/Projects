import express from 'express'
// import mongoose from 'mongoose'
import { Entry, Category } from './db.js'

const app = express()

// Middleware
app.use(express.json())

// Flask
// @app.route('/')
// def home():
//     return {'info': 'Journal API'}
app.get('/', (request, response) => response.send({ info: 'Journal API!!' }))

app.get('/categories', async (req, res) => res.send(await Category.find()))

// Retrieve all entries
app.get('/entries', async (req, res) => res.send(await Entry.find()))

// Retrieve one entry
app.get('/entries/:id', async (req, res) => {
    try {
        const entry = await Entry.findById(req.params.id) 
        if (entry) {
            res.send(entry)
        } else {
            res.status(404).send({ error: 'Entry not found' })
        }
    }
    catch (err) {
        res.status(400).send({ error: err.message})
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


// Update and entry
app.put('/entries/:id', async (req, res) => {
    try {
        const entry = await Entry.findByIdAndUpdate(req.params.id, req.body, { returnDocument: 'after' }) 
        if (entry) {
            res.send(entry)
        } else {
            res.status(404).send({ error: 'Entry not found' })
        }
    }
    catch (err) {
        res.status(400).send({ error: err.message})
    }
})

// Delete and entry
app.delete('/entries/:id', async (req, res) => {
    try {
        const entry = await Entry.findByIdAndDelete(req.params.id) 
        if (entry) {
            res.sendStatus(200)
        } else {
            res.status(404).send({ error: 'Entry not found' })
        }
    }
    catch (err) {
        res.status(400).send({ error: err.message})
    }
})

// Start Server
app.listen(4001, err => {
    if (err) {
        console.error(err)
    } else {
        console.log('Server running')
    }
})

