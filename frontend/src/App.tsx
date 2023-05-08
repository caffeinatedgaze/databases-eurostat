import React from "react";
import logo from "./logo.svg";
import "./App.css";
import { Routes, Route } from "react-router-dom";
import Home from "./containers/Home";
import SearchResult from "./components/SearchResult";

function App() {
  return (
    <div className="App bg-gray-600 min-h-full h-full w-full absolute  ">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="search-result" element={<SearchResult />} />
      </Routes>
    </div>
  );
}

export default App;
