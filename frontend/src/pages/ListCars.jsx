import { useState, useEffect } from 'react';
import { getCars } from '../api/authApi';
import Car from '../components/Car';

export default function ListCars() {

  const [cars, setCars] = useState([])

  const createCarsList = () => {
    return cars.map((car, i) => <Car key={i} car={car} />)
  }

  useEffect(() => {
    async function performGetCars() {
      const cars = await getCars()
      console.log('cars: ', cars)
      setCars(cars)
    }
    performGetCars()
  }, [])

  return (
    createCarsList()
  )
}