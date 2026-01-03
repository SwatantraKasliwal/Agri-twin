function MetricCard({ label, value, unit }) {
  return (
    <div className="card">
      <h4>{label}</h4>
      <p>
        {value} {unit}
      </p>
    </div>
  );
}

export default MetricCard;
