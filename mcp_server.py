"""Standalone MCP server for Wayvora AI."""
from mcp.server.fastmcp import FastMCP
from travel_tools import find_places, estimate_trip_budget, create_itinerary, replan_trip

mcp = FastMCP("Wayvora AI Travel Tools")

@mcp.tool()
def search_destination_places(destination: str, interests: list[str] | None = None, limit: int = 8) -> dict:
    """Find sample attractions by destination and interests."""
    return find_places(destination, interests, limit)

@mcp.tool()
def calculate_travel_budget(destination: str, days: int, travelers: int, budget_inr: int, travel_style: str = "balanced") -> dict:
    """Estimate accommodation, food, local transport and activity costs in INR."""
    return estimate_trip_budget(destination, days, travelers, budget_inr, travel_style)

@mcp.tool()
def build_travel_itinerary(destination: str, days: int = 3, travelers: int = 2, budget_inr: int = 12000, interests: list[str] | None = None, travel_style: str = "balanced") -> dict:
    """Create a sample day-by-day itinerary with budget estimate."""
    return create_itinerary(destination, days, travelers, budget_inr, interests, travel_style)

@mcp.tool()
def adapt_travel_itinerary(destination: str, days: int, travelers: int, budget_inr: int, interests: list[str] | None = None, travel_style: str = "budget") -> dict:
    """Replan a trip when the budget or user preferences change."""
    return replan_trip(destination, days, travelers, budget_inr, interests, travel_style)

if __name__ == "__main__":
    mcp.run()
