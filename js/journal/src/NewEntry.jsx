import React, { useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'

const NewEntry = ({ categories, addEntry }) => {
    const [content, setContent] = useState('')

    const nav = useNavigate()
    const { cat_id } = useParams()
    const cat = categories.find((c) => c.id == cat_id)

    const submitHandler = e => {
        e.preventDefault()
        // Add the new entry to the list of entries
        const id = addEntry(cat.id, content)
        // Return success message or redirect to entry
        nav(`/entry/${id}`)
    }

    return cat ? (
            <div class="container is-fluid">
                <h2 class="my-2 is-size-5">New Entry in category | {cat.name}</h2>
                <form onSubmit={submitHandler}>
                    <div class="field">
                        <div class="control">
                            <textarea value ={content} onChange={e => setContent(e.target.value)} class="textarea" placeholder="Type your entry here"></textarea>
                        </div>
                    </div>
                    <div class="control">
                        <button class="button is-primary">Create Entry</button>
                    </div>
                </form>
            </div>
    ) : (
        <h3>Invalid category ID!</h3>
    )
}

export default NewEntry