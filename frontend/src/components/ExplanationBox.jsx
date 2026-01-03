function ExplanationBox({ reasons }) {
  return (
    <ul>
      {reasons.map((r, i) => (
        <li key={i}>{r}</li>
      ))}
    </ul>
  );
}
export default ExplanationBox;
