import React, { useEffect, useState } from 'react'

const BitcoinIndex = ({ currency }) => {
  const [price, setPrice] = useState(0)

  // All useEffects will be triggered on mount

  //
  //

  //
  //

  // will be triggered if any of the dependencies change
  useEffect(() => {
    console.log('Fetching...')
    fetch(`https://api.coindesk.com/v1/bpi/currentprice/${currency}.json`)
      .then(res => res.json())
      .then(data => setPrice(data.bpi[currency].rate))
  }, [currency])

  return <h2>Current Price ({currency}): {price}</h2>
}

export default BitcoinIndex