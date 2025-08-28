const Model = ({ model }) => {
  return (
    <>
      <p>{model.fields.make} {model.fields.model}</p>
    </>
  );
}
export default Model