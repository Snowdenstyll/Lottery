import React, { useEffect } from "react";

function index() {
  const [message, setMessage] = React.useState("Loading");

  useEffect(() => {
    fetch("http://127.0.0.1:8000")
      .then((res) => res.json())
      .then((data) => setMessage(data.message));

  }, []);

  return <div> {message}</div>
}

export default index;