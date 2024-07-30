import React from 'react'

export const Greeting = ({ name, age = 'unknown' }) => {
    return (
        <>
            <p>FR: Bonjour{name ? ', ' : ''}{name}!</p>
            <p>ES: Hola!</p>
            <p>EN: You are {age} years old!</p>
        </>
    )
}
