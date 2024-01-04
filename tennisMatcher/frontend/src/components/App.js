import HomePage from "./HomePage";
import React from "react";
import ReactDOM from "react-dom/client";

const App = () => {
  return (
    <HomePage />
  );
};

const root = ReactDOM.createRoot(document.getElementById("app"));
root.render(<App />);
