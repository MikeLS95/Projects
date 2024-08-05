import React, { useState } from 'react'
import { Routes, Route, useParams } from 'react-router-dom'
import CategorySelection from './CategorySelection'
import Home from './Home'
import NewEntry from './NewEntry'
import NavBar from './NavBar'
import ShowEntry from './ShowEntry'

let newEntryId = 1

const App = () => {
  const [entries, setEntries] = useState([])

  const [categories, setCategories] = useState([
    { id: 1, name: "Food" },
    { id: 2, name: "Gaming" },
    { id: 3, name: "Coding" },
    { id: 4, name: "Other" }
  ])

  const addEntry = (cat_id, content) => {
    // console.log(cat_id, content)
    // TODO: Sanitize and validate entry data
    // Create a new entry from the entered data
    const newEntry = { id: newEntryId++, category: cat_id, content: content }
    // Add the new entry to the list of entries
    setEntries([...entries, newEntry])
    return newEntryId - 1
  }

  // Higher-order Component (HOC)
  const ShowEntryWrapper = () => {
    // Get id from useParams
    const { id } = useParams()
    // Get entry with the given id
    const entry = entries.find(e => e.id == id)
    return entry ? <ShowEntry entry={entry} /> : <h3>Entry not found!</h3>
  }

  return (
    <>
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/category" element={<CategorySelection categories={categories} />} />
        <Route path="/entry" >
          <Route path=":id" element={<ShowEntryWrapper />} />
          <Route path="new/:cat_id" element={<NewEntry categories={categories} addEntry={addEntry} />} />
        </Route>
        <Route path="*" element={<h3>404 - Page not found..</h3>} />
      </Routes>
    </>
  )
}

export default App