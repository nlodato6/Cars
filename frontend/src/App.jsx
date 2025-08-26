import './App.css'
import { Route, Routes } from 'react-router-dom'
import Navbar2 from './components/Navbar2'
import Home from './pages/Home'
import Ads from './pages/Ads'
import Cars from './pages/Cars'
import Models from './pages/Models'
import Users from './pages/Users'
import Profiles from './pages/Profiles'

function App() {

  return (
    <div>
      <Navbar2 />
      <div className='flex justify-center mt-8'>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/ads" element={<Ads />} />
          <Route path="/cars" element={<Cars />} />
          <Route path="/models" element={<Models />} />
          <Route path="/users" element={<Users />} />
          <Route path="/profiles" element={<Profiles />} />
        </Routes>
      </div>
    </div>
  )
}

export default App
