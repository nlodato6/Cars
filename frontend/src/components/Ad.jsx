import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';

const Ad = ({ ad }) => {
  return (
    <Card className=''>
      <Card.Body className='bg-[#00D8FF]'>
        <Card.Title className='text-center'>{ad.advertisement_date}</Card.Title>
        <div className='border-1 bg-white rounded-2xl p-4'>
          <p><strong>Car id:</strong> {ad.car}</p>
          <p><strong>Date:</strong> {ad.advertisement_date}</p>
          <p><strong>Seller id:</strong> {ad.seller_account}</p>
          <div className='flex justify-evenly'>
            <Button className='w-[86px]' variant="primary">Edit</Button>
            <Button className='w-[86px]' variant="danger">Delete</Button>
          </div>
        </div>
      </Card.Body>
    </Card>
  );
}
export default Ad