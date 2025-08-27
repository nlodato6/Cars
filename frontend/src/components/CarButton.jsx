import { CardText } from 'react-bootstrap';
import Button from 'react-bootstrap/Button';

function CarButton() {
  return (
    <div className="d-grid gap-2">
      <Button variant="primary" size="lg">
        Add Car
      </Button>
       <Button variant="primary" size="lg">
        Delete Car
      </Button>
    </div>
  );
}

export default CarButton;