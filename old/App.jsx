import React, { useState } from "react";
import sheets from "../knowledge_sheets.json";

function App() {
  const [currentSheet, setCurrentSheet] = useState(null);

  const showRandomSheet = () => {
    const randomIndex = Math.floor(Math.random() * sheets.length);
    setCurrentSheet(sheets[randomIndex]);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-4">
      <h1 className="text-3xl font-bold mb-6">Weekly Knowledge</h1>
      <button
        onClick={showRandomSheet}
        className="px-6 py-3 mb-6 bg-blue-600 text-white rounded shadow hover:bg-blue-700 transition"
      >
        Show a Knowledge Sheet
      </button>

      {currentSheet && (
        <div className="max-w-2xl bg-white p-6 rounded shadow">
          <p className="text-sm text-gray-500 mb-2">
            {currentSheet.date} — {currentSheet.location}, {currentSheet.country}
          </p>
          <h2 className="text-2xl font-semibold mb-4">{currentSheet.title}</h2>
          <p className="whitespace-pre-line">{currentSheet.text}</p>
        </div>
      )}
    </div>
  );
}

export default App;
