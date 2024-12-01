// client/src/index.tsx
import "./styles/global.css";
import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./components/layout";
import Index from "./pages/KenoLottery";

const container = document.getElementById("root");
const root = createRoot(container!);
root.render(
  <BrowserRouter>
    <Layout>
      <Routes>
        <Route path="/" element={<Index />} />
      </Routes>
    </Layout>
  </BrowserRouter>
);

export default Index;