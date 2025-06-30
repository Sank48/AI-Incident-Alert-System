import React from "react";
import Button from "./buttons";
import { toast } from "sonner";
import "./ErrorSimulations.css";

const ERROR_TYPES = {
  DB_ERROR: "Failed to connect to database",
  AUTH_FAILURE: "Unauthorized access attempt",
  SERVICE_DOWN: "Downstream service not responding",
  TIMEOUT: "Request timeout",
  NULL_POINTER: "Null reference exception",
  RATE_LIMIT: "Rate limit exceeded",
  DISK_FULL: "Disk out of space",
  MEMORY_LEAK: "Memory usage too high",
  CONFIG_MISSING: "Missing config",
  DEPLOY_ERROR: "Deployment failure",
  INTERNAL_ERROR: "Generic 500 error",
  INVALID_INPUT: "Invalid input provided",
};

const API_BASE = "https://54kf3qzgb3.execute-api.ap-south-1.amazonaws.com/prod";

export default function ErrorSimulator() {
  const simulateError = async (type) => {
    try {
      const res = await fetch(`${API_BASE}/simulate`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ type }),
      });

      if (res.ok) {
        toast.success(`${type} simulated`);
      } else {
        toast.success(`${type} simulated`);
      }
    } catch (err) {
      console.error("this is error-> ", err);
      toast.success(`${type} simulated`);
    }
  };

  return (
    <div className="p-4 space-y-4">
      <h2 className="text-xl font-semibold">Simulate Errors</h2>
      <div className="flex flex-wrap gap-2">
        {Object.entries(ERROR_TYPES).map(([type, label]) => (
          <Button key={type} onClick={() => simulateError(type)}>
            {type.replaceAll("_", " ")}
          </Button>
        ))}
      </div>
    </div>
  );
}
