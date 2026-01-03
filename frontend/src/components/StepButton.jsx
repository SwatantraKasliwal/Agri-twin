function StepButton({ onClick }) {
  return (
    <button className="step-btn" onClick={onClick}>
      Run Next Step
    </button>
  );
}

export default StepButton;
