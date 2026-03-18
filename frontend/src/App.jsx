import { useState } from "react";
import Upload from "./components/Upload";
import Query from "./components/Query";

function App() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  return (
    <div style={{ height: "100vh", display: "flex", flexDirection: "column" }}>
      <h1 style={{ padding: "10px", borderBottom: "1px solid #ccc" }}>
        RAG Chat
      </h1>

      <Upload />

      {/* Chat Area */}
      <div
        style={{
          flex: 1,
          overflowY: "auto",
          padding: "20px",
          display: "flex",
          flexDirection: "column",
        }}
      >
        {messages.map((msg, index) => (
          <div key={index} style={{ marginBottom: "15px" }}>
            {/* USER */}
            <div
              style={{
                display: "flex",
                justifyContent: "flex-end",
              }}
            >
              <div
                style={{
                  background: "#007bff",
                  color: "white",
                  padding: "10px 15px",
                  borderRadius: "15px",
                  maxWidth: "60%",
                }}
              >
                {msg.question}
              </div>
            </div>

            {/* AI */}
            <div
              style={{
                display: "flex",
                justifyContent: "flex-start",
                marginTop: "5px",
              }}
            >
              <div
                style={{
                  background: "#e5e5ea",
                  padding: "10px 15px",
                  borderRadius: "15px",
                  maxWidth: "60%",
                  whiteSpace: "pre-line",
                }}
              >
                {msg.answer}
              </div>
            </div>
          </div>
        ))}

        {/* 🔄 Loading Indicator */}
        {loading && (
          <div style={{ display: "flex", justifyContent: "flex-start" }}>
            <div
              style={{
                background: "#e5e5ea",
                padding: "10px 15px",
                borderRadius: "15px",
              }}
            >
              ⏳ Thinking...
            </div>
          </div>
        )}
      </div>

      <Query setMessages={setMessages} setLoading={setLoading} />
    </div>
  );
}

export default App;