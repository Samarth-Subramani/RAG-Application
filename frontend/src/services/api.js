const BASE_URL = "http://localhost:8000"; // FastAPI

export async function uploadFile(file) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${BASE_URL}/files/upload?ingest=true`, {
    method: "POST",
    body: formData,
  });

  return res.json();
}

export async function queryRAG(query, top_k = 5) {
  const res = await fetch(`${BASE_URL}/query/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ query, top_k }),
  });

  return res.json();
}