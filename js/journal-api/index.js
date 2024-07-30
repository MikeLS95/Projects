import express from 'express'
import mongoose from 'mongoose'
import { Category } from './db.js'
import entryRoutes from './routes/entry_routes.js'

const app = express()

// Middleware
app.use(express.json())

// Flask
// @app.route('/')
// def home():
//     return {'info': 'Journal API'}
app.get('/', (request, response) => response.send({ info: 'Journal API!!' }))

// TODO: Move /categories route to a routes module
// TODO: Complete categories CRUD
// TODO: ADVANCED: Add a route GET /categories/:cat_id/entries that returns all entries in the given category

// Retrieve all categories
app.get('/categories', async (req, res) => res.send(await Category.find()))

app.use(entryRoutes)

// Start Server
app.listen(4001, err => {
    if (err) {
        console.error(err)
    } else {
        console.log('Server running')
    }
})

