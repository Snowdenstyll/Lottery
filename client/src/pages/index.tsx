import React, { useEffect } from "react";
import ReactDOM from "react-dom";
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

export default Index;