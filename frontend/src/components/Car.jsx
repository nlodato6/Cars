const Car = ({ car }) => {
  return (
    <>
      <h1>Car model: {car.fields.car_model}</h1>
      <p>Manufacture Year: {car.fields.manufacture_year}</p>
      <p>Mileage: {car.fields.mileage}</p>
      <p>Doors: {car.fields.number_of_doors}</p>
      <p>Owners: {car.fields.number_of_owners}</p>
      <p>Registration #: {car.fields.registration_number}</p>
    </>
  );
}
export default Car