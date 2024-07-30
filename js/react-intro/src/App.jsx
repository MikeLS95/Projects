import './App.css'
import { Greeting } from './Greeting.jsx'

function App() {
  return (
    <>
      <h1>Hello</h1>
      <Greeting name="Mike" age={28} />
      <Greeting name="Ben"/>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt voluptas libero magni itaque ullam, voluptate dolorum natus pariatur nemo cum exercitationem a, reiciendis quo blanditiis minima odio cumque, mollitia possimus!</p>
      <Greeting />
    </>
  )
}

export default App
