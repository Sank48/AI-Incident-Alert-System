// Component to fetch and display incidents based on filter criteria
import React, { useEffect, useState } from "react";
import Button from "./buttons";
import { Card, CardContent } from "./card";
import { Badge } from "./badge";
import { toast } from "sonner";

const API_URL =
  "https://54kf3qzgb3.execute-api.ap-south-1.amazonaws.com/prod/incidents";

export default function IncidentList() {
  const [incidents, setIncidents] = useState([]);
  const [loading, setLoading] = useState(false);
  const [filterType, setFilterType] = useState("all");
  const [expandedId, setExpandedId] = useState(null);

  const fetchIncidents = async (param, value = null) => {
    setLoading(true);
    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(
          param === "all" ? { param: "all" } : { param, [param]: value }
        ),
      });
      const data = await res.json();
      setIncidents(data);
    } catch (error) {
      toast.error("Failed to fetch incidents");
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchIncidents("all");
  }, []);

  const toggleExpand = (id) => {
    console.log("id: ", id);
    setExpandedId(expandedId === id ? null : id);
  };

  return (
    <div className="p-6 space-y-4">
      <h2 className="text-xl font-semibold">Incident List</h2>

      <div className="flex gap-2 flex-wrap">
        <Button
          onClick={() => {
            setFilterType("all");
            fetchIncidents("all");
          }}
        >
          All
        </Button>
        <Button
          onClick={() => {
            setFilterType("severity");
            fetchIncidents("severity", "Critical");
          }}
        >
          Severity: Critical
        </Button>
        <Button
          onClick={() => {
            setFilterType("severity");
            fetchIncidents("severity", "High");
          }}
        >
          Severity: High
        </Button>
        <Button
          onClick={() => {
            setFilterType("status");
            fetchIncidents("status", "OPEN");
          }}
        >
          Status: OPEN
        </Button>
        <Button
          onClick={() => {
            setFilterType("status");
            fetchIncidents("status", "RESOLVED");
          }}
        >
          Status: RESOLVED
        </Button>
      </div>

      {loading ? (
        <p>Loading...</p>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {incidents.length > 0 ? (
            incidents.map((incident) => {
              const isExpanded = expandedId === incident.eventId;
              return (
                <Card key={incident.eventid} className="border">
                  <div
                    className={`p-4 space-y-2 cursor-pointer ${
                      isExpanded ? "col-span-2 lg:col-span-3" : ""
                    }`}
                    key={incident.eventid}
                    onClick={() => toggleExpand(incident.eventId)}
                  >
                    <CardContent className="space-y-2">
                      <div className="flex justify-between items-center">
                        <Badge variant="outline">{incident.severity}</Badge>
                        <span className="text-sm text-muted-foreground">
                          {new Date(incident.timestamp * 1000).toLocaleString()}
                        </span>
                      </div>
                      <div>
                        <h3 className="font-semibold">{incident.summary}</h3>
                        <p className="text-sm">💡 {incident.suggestions}</p>
                      </div>
                      <p className="text-xs text-muted-foreground">
                        <strong>Status: </strong>
                        {incident.status}
                      </p>
                      {isExpanded && (
                        <div className="text-xs space-y-1 text-muted-foreground">
                          <p>
                            <strong>Event ID:</strong> {incident.eventId}
                          </p>
                          <p>
                            <strong>Log source: </strong> {incident.source}
                          </p>
                        </div>
                      )}
                    </CardContent>
                  </div>
                </Card>
              );
            })
          ) : (
            <p>No Results.</p>
          )}
        </div>
      )}
    </div>
  );
}
