import { useState, useEffect } from 'react';
import { getAds } from '../api/authApi';
import Ad from '../components/Ad';

export default function ListAds() {

  const [ads, setAds] = useState([])

  const createAdsList = () => {
    return ads.map((ad, i) => <Ad key={i} ad={ad} />)
  }

  useEffect(() => {
    async function performGetAds() {
      const ads = await getAds()
      setAds(ads)
    }
    performGetAds()
  }, [])

  return (
    createAdsList()
  )
}