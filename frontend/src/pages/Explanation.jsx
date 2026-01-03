import ExplanationBox from "../components/ExplanationBox";
import { getNextStep } from "../api/backend";

function Explanation() {
  const data = getNextStep();

  return (
    <div className="page">
      <h2>Why This Decision?</h2>
      <ExplanationBox reasons={data.explanation} />
    </div>
  );
}

export default Explanation;
