
const Ad = ({ ad }) => {
  return (
    <>
      <h2>{ad.car}</h2>
      <p>{ad.advertisement_date}</p>
      <p>{ad.seller_account}</p>
    </>
  );
}
export default Ad