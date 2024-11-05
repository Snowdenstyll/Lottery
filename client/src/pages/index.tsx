import React, { useEffect } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Lottery from "./lottery/index"; // Adjust the path as needed

function Index() {
  const [message, setMessage] = React.useState("Loading");

  useEffect(() => {
    fetch("http://127.0.0.1:5000")
      .then((res) => res.json())
      .then((data) => setMessage(data.message));
  }, []);

  return <div><p>{message}</p></div>;
}

const container = document.getElementById('root');
const root = createRoot(container!);
root.render(
  <Router>
    <Routes>
      <Route path="/" element={<Index />} />
      <Route path="/lottery" element={<Lottery />} />
    </Routes>
  </Router>
);

export default Index;