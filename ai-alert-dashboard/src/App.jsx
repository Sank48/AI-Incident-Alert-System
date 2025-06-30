import { useState } from "react";
// import Button from "./components/buttons";
import ErrorSimulator from "./components/ErrorSimulations";
import IncidentList from "./components/IncidentList";
import { Toaster } from "sonner";
import "./App.css";

function App() {
  return (
    <>
      <Toaster position="top-center" />
      <div className=" p-2 tex-center w-fit mx-auto text-2xl font-bold">
        Incident Dashboard
      </div>
      <ErrorSimulator />
      <IncidentList />
    </>
  );
}

export default App;
