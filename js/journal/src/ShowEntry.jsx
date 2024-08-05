import React from 'react'

const ShowEntry = ({ entry }) => {
    return (
        <>
            <p>Posted in {entry.category}</p>
            <h2 class="my-5 is-size-5">{entry.content}</h2>
        </>
    )
}

export default ShowEntry