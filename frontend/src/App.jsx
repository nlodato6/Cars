"use client"
import './App.css'
import { Router, Route, Routes } from 'react-router-dom'
import NavbarNav from './components/NavbarNav'
import Home from './pages/Home'
import Ads from './pages/Ads'
import Cars from './pages/Cars'
import Models from './pages/Models'
import Users from './pages/Users'
import Profiles from './pages/Profiles'
import { ErrorBoundary } from "react-error-boundary";

function App() {

  return (
    <>
      <ErrorBoundary fallback={<div>Something went wrong</div>}>
        <NavbarNav />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/ads" element={<Ads />} />
          <Route path="/cars" element={<Cars />} />
          <Route path="/models" element={<Models />} />
          <Route path="/users" element={<Users />} />
          <Route path="/profiles" element={<Profiles />} />
        </Routes>
      </ErrorBoundary>
    </>
  )
}

export default App;
