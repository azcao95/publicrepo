import React from "react";
import "./App.css";
import SPCalc from "./SPCalc";

import data from "./history.json";

function App() {
  return (
    <div>
      <header>
        <h1>{"Cumulative S&P Tool"}</h1>
      </header>
      <body>
        <SPCalc data={data} />
      </body>
    </div>
  );
}

export default App;
