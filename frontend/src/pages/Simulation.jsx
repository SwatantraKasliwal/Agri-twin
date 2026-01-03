import { useState } from "react";
import { getNextStep } from "../api/backend";
import ActionCard from "../components/ActionCard";
import StepButton from "../components/StepButton";

function Simulation() {
  const [data, setData] = useState(null);

  const runSimulation = () => {
    setData(getNextStep());
  };

  return (
    <div className="page">
      <h2>Decision Simulation</h2>

      <StepButton onClick={runSimulation} />

      {data && <ActionCard irrigation={data.irrigation_mm} />}
    </div>
  );
}

export default Simulation;
