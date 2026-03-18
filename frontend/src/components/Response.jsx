export default function Response({ data }) {
  if (!data) return null;

  return (
    <div style={{ marginTop: "20px" }}>
      <h2>Answer</h2>
      <p style={{ whiteSpace: "pre-line" }}>
        {data?.data?.answer || "No response"}
      </p>
    </div>
  );
}