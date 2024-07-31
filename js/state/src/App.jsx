import React, { useState } from 'react'
import BitcoinIndex from "./BitcoinIndex"
import CurrencySelector from "./CurrencySelector"

const App = () => {
  const [currency, setCurrency] = useState("AUD")

  const updateCurrency = (code) => {
    // Validation of code
    setCurrency(code)
  }

  return (
    <>
      <h1>Bitcoin Index</h1>
      <BitcoinIndex currency={currency} />
      <CurrencySelector setCurrency={updateCurrency} />
    </>
  )
}

export default App