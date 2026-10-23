# Wayvora AI — Travel Studio

A premium-minimalist travel-planning prototype with destination selection, day-by-day sample itineraries, illustrative INR budget estimates, replanning, and a standalone MCP server.

## Run locally on Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app:app --reload
```

Open http://127.0.0.1:8000. Health check: http://127.0.0.1:8000/api/health. API docs: http://127.0.0.1:8000/docs.

If PowerShell blocks environment activation, run `.venv\Scripts\python.exe -m pip install -r requirements.txt` and `.venv\Scripts\python.exe -m uvicorn app:app --reload`.

## Deploy to Render

This repository includes `render.yaml`. Create a new **Blueprint** in Render and connect this GitHub repository, or create a **Web Service** manually with:

- Runtime: Python 3
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn app:app --host 0.0.0.0 --port $PORT`
- Health check path: `/api/health`

## MCP tools

Run `python mcp_server.py` in a separate terminal. The standalone MCP server exposes `search_destination_places`, `calculate_travel_budget`, `build_travel_itinerary`, and `adapt_travel_itinerary`.

## API endpoints

- `GET /api/health` — health check
- `GET /api/destinations` — supported sample destinations
- `GET /api/places?destination=Jaipur` — sample attractions
- `POST /api/plan` — create an itinerary draft
- `POST /api/replan` — replan with updated preferences
- `GET /docs` — interactive API documentation

## Prototype limitations

Attractions and budget figures are local sample data / illustrative estimates, not live quotes. The planner does not verify live opening hours, transport routes, weather, hotel availability, or booking prices. The web UI currently calls Python functions directly; the separate MCP server is available for MCP clients, but the web UI is not yet an LLM-powered autonomous agent. No bookings or payments are made.
