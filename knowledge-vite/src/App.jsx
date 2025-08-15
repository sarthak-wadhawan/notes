import React, { useState } from "react";
import sheets from "./knowledge_sheets.json";
import "./App.css";
import { Analytics } from '@vercel/analytics/react'

function App() {
  const [currentSheet, setCurrentSheet] = useState(null);
  const [showLanding, setShowLanding] = useState(true);

  const showRandomSheet = () => {
    const randomIndex = Math.floor(Math.random() * sheets.length);
    setCurrentSheet(sheets[randomIndex]);
    setShowLanding(false);
  };

  const returnToLanding = () => {
    setCurrentSheet(null);
    setShowLanding(true);
  };

  return (
    <>
    <Analytics />
    <div className="app-container">
      {showLanding ? (
        <div className="landing-container">
          <h1>Pages from an intimate note to the Sincere Seeker</h1>
          <div className="quote-card" onClick={showRandomSheet}>
            <div className="quote-image-container">
              <img 
                src="https://i.pinimg.com/736x/e4/4a/53/e44a53a6727d8889d3eb70fc1a41b1d3.jpg" 
                alt="Sri Sri Ravi Shankar" 
                className="quote-image"
              />
              <div className="quote-border"></div>
            </div>
            <button
              onClick={showRandomSheet}
              className="knowledge-button"
            >
              Show a Knowledge Sheet
            </button>
          </div>
          <div className="iframe-container">
            <iframe
              src={showLanding ? "https://members.us.artofliving.org/us-en/ask-gurudev": ""}
              title="Ask Gurudev"
              className="responsive-iframe"
              loading="lazy"
              onLoad={(e) => e.target.classList.add('loaded')}
            />
          </div>
        </div>
      ) : (
        <>
          <button 
            onClick={returnToLanding}
            className="back-button"
          >
            ← Back to Home Page
          </button>
          
          {currentSheet && (
            <div className="knowledge-card">
              {/* Header Section */}
              <div className="card-header">
                <h1 className="card-main-title">Knowledge by Sri Sri</h1>
                <div className="card-subheader">
                  <span className="card-subtitle">Knowledge Sheet from {currentSheet.country}</span>
                  <span className="card-date">
                    {currentSheet.date} — {currentSheet.location}, {currentSheet.country}
                  </span>
                </div>
              </div>
              
              {/* Content Section */}
              <div className="card-content">
                <h2 className="card-title">{currentSheet.title}</h2>
                
                {currentSheet.news_flash && (
                  <div className="news-flash">
                    <p>{currentSheet.news_flash}</p>
                  </div>
                )}
                
                <p className="card-text">{currentSheet.text}</p>
              </div>
              
              {/* Footer */}
              <div className="card-footer">
                © The Art of Living Foundation
              </div>
            </div>
          )}
        </>
      )}
    </div>
    </>
  );
}

export default App;