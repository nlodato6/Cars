import { useState, useEffect } from 'react';
import { getModels } from '../api/authApi';
import Model from '../components/Model';

export default function ListModels() {

  const [models, setModels] = useState([])

  const createModelsList = () => {
    return models.map((model, i) => <Model key={i} model={model} />)
  }

  useEffect(() => {
    async function performGetModels() {
      const models = await getModels()
      setModels(models)
    }
    performGetModels()
  }, [])

  return (
    createModelsList()
  )
}