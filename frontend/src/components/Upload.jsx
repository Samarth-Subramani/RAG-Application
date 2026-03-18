import { useState } from "react";
import { uploadFile } from "../services/api";

export default function Upload() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");

  const handleUpload = async () => {
    if (!file) return;

    setStatus("Uploading...");
    try {
      const res = await uploadFile(file);
      setStatus("Upload successful!");
    } catch (err) {
      setStatus("Upload failed");
    }
  };

  return (
    <div>
      <h2>Upload PDF</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload</button>
      <p>{status}</p>
    </div>
  );
}