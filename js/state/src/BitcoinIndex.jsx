import React, { useEffect, useState } from 'react'

const BitcoinIndex = () => {
  const [price, setPrice] = useState(0)

  // will be triggered every update
  useEffect(() => console.log('effect triggered'))

  // will be triggered if any of the dependencies change
  useEffect(() => {
    console.log('Fetching...')
    fetch('https://api.coindesk.com/v1/bpi/currentprice/AUD.json')
      .then(res => res.json())
      .then(data => setPrice(data.bpi.AUD.rate))
  }, [])




  return <h2>Current Price (AUD): {price}</h2>
}

export default BitcoinIndex