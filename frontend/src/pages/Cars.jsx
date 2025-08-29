

import ListCars from "./ListCars";
import Container from 'react-bootstrap/Container';

function Cars() {
  return (
    <Container fluid className='mt-8'>
      <h2 className="text-center">Cars</h2>
      <div className='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 grid-rows-[auto] gap-8 p-4'>
        <ListCars />
      </div>
    </Container>
  )
}

export default Cars;