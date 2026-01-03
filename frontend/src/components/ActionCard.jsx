function ActionCard({ irrigation }) {
  return (
    <div className="action-card">
      <h2>{irrigation} mm/day</h2>
      <p>Recommended Irrigation</p>
    </div>
  );
}
export default ActionCard;
