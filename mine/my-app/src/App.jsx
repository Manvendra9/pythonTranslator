import React from "react";
import CodeTranslator from "./CodeTranslator"; // ✅ Ensure this file exists

export default function App() {
  return (
    <div style={{ background: "white", color: "black", padding: "20px", textAlign: "center" }}>
      <h1>🚀 Python Code Translator</h1>
      <CodeTranslator />
    </div>
  );
}
