import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';

const Model = ({ model }) => {
  return (
    <Card className=''>
      <Card.Body className='bg-[#00D8FF]'>
        <Card.Title className='text-center'>{model.fields.make}</Card.Title>
        <div className='text-center border-1 bg-white rounded-2xl p-4'>
          <p><strong>Model:</strong> {model.fields.model}</p>
          <div className='flex justify-evenly'>
            <Button className='w-[86px]' variant="primary">Edit</Button>
            <Button className='w-[86px]' variant="danger">Delete</Button>
          </div>
        </div>
      </Card.Body>
    </Card>
  );
}
export default Model