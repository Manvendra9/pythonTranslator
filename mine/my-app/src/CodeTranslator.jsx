import React, { useState } from "react";
import "./styles.css"; // ✅ Ensure CSS is linked

export default function CodeTranslator() {
  const [code, setCode] = useState("");
  const [language, setLanguage] = useState("javascript");
  const [translatedCode, setTranslatedCode] = useState("");

  // 🔹 Expanded Language List
  const languages = [
    "javascript", "c", "c++", "java", "ruby", "go",
    "php", "swift", "rust", "kotlin", "typescript"
  ];

  const handleTranslate = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/translate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code, language }),
      });

      if (!response.ok) {
        throw new Error("Translation failed.");
      }

      const data = await response.json();
      setTranslatedCode(data.translatedCode);
    } catch (error) {
      setTranslatedCode("Error: Could not translate code.");
    }
  };

  return (
    <div className="container">
      <h1>🚀 Python Code Translator</h1>

      <textarea placeholder="Enter Python code..." value={code} onChange={(e) => setCode(e.target.value)} />

      <select value={language} onChange={(e) => setLanguage(e.target.value)}>
        {languages.map((lang) => (
          <option key={lang} value={lang}>{lang.toUpperCase()}</option>
        ))}
      </select>

      <button onClick={handleTranslate}>Translate</button>

      {translatedCode && (
        <div className="translated-box">
          <h2>📜 Translated Code:</h2>
          <textarea value={translatedCode} readOnly />
        </div>
      )}
    </div>
  );
}
