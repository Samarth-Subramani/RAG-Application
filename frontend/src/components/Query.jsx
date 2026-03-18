import { useState } from "react";
import { queryRAG } from "../services/api";

export default function Query({ setMessages, setLoading }) {
  const [query, setQuery] = useState("");

  const handleQuery = async () => {
    if (!query.trim()) return;

    const userQuery = query;
    setQuery("");

    setLoading(true); // 👈 start loading

    const res = await queryRAG(userQuery);

    setMessages((prev) => [
      ...prev,
      {
        question: userQuery,
        answer: res?.data?.answer || "No response",
      },
    ]);

    setLoading(false); // 👈 stop loading
  };

  return (
    <div
      style={{
        display: "flex",
        padding: "10px",
        borderTop: "1px solid #ccc",
      }}
    >
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask something..."
        style={{
          flex: 1,
          padding: "10px",
          borderRadius: "10px",
          border: "1px solid #ccc",
        }}
      />
      <button
        onClick={handleQuery}
        style={{
          marginLeft: "10px",
          padding: "10px 15px",
        }}
      >
        Send
      </button>
    </div>
  );
}