import ListModels from './ListModels';
import Container from 'react-bootstrap/Container';

export default function Models() {

  return (
    <Container fluid className="mt-8">
      <h2 className="text-center">Models List</h2>
      <div className='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 grid-rows-[auto] gap-8 p-4'>
        <ListModels />
      </div>
    </Container>
  )
}