import MetricCard from "../components/MetricCard";

function Dashboard() {
  return (
    <div className="page">
      <h2>Current Farm State</h2>

      <div className="grid">
        <MetricCard label="Soil Moisture" value="62" unit="%" />
        <MetricCard label="Heat Stress" value="28" unit="%" />
        <MetricCard label="Rainfall" value="10" unit="mm" />
        <MetricCard label="Crop Stage" value="Vegetative" unit="" />
      </div>
    </div>
  );
}

export default Dashboard;
