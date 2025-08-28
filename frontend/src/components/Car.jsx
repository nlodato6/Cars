import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';

const Car = ({ car }) => {
  return (
    <Card>
      <Card.Body className='bg-[#00D8FF]'>
        <Card.Title className='text-center'>Model: {car.fields.car_model}</Card.Title>
        <div className='border-1 bg-white rounded-2xl p-4'>
          <p><strong>Manufacture Year:</strong> {car.fields.manufacture_year}</p>
          <p><strong>Mileage:</strong> {car.fields.mileage}</p>
          <p><strong>Doors:</strong> {car.fields.number_of_doors}</p>
          <p><strong>Owners:</strong> {car.fields.number_of_owners}</p>
          <p><strong>Registration #:</strong> {car.fields.registration_number}</p>
          <div className='flex justify-evenly'>
            <Button className='w-[86px]' variant="primary">Edit</Button>
            <Button className='w-[86px]' variant="danger">Delete</Button>
          </div>
        </div>
      </Card.Body>
    </Card>
  );
}
export default Car