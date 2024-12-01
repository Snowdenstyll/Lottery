// client/src/index.tsx
import "./styles/global.css";
import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./components/layout";
import KenoLottery from "./pages/KenoLottery";
import HomePage from "./pages/HomePage";

const container = document.getElementById("root");
const root = createRoot(container!);
root.render(
  <BrowserRouter>
    <Layout>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/keno" element={<KenoLottery />} />
      </Routes>
    </Layout>
  </BrowserRouter>
);