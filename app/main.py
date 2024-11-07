from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException, Path
from typing import List, Union, Dict
from fastapi.middleware.cors import CORSMiddleware
from .models.room import BathRoom
from .models.fixtures import Fixture, WallFeature, Window, Door, Ventilation
from .models.styles import DesignTheme, CostRange

# Create demo data
BATHROOMS: Dict[UUID, BathRoom] = {}
DESIGN_THEMES = [
    DesignTheme(
        name="Modern Minimalist",
        description="Clean lines and minimal decoration",
        style="Modern",
        color_scheme=["White", "Gray", "Black"],
        materials=["Glass", "Ceramic", "Steel"],
        recommended_fixtures=[
            "Wall-mounted toilet",
            "Floating vanity",
            "Walk-in shower",
        ],
        estimated_cost_range=CostRange(min_cost=5000.0, max_cost=15000.0),
    ),
    DesignTheme(
        name="Classic",
        description="Traditional and timeless design",
        style="Traditional",
        color_scheme=["Beige", "White", "Brown"],
        materials=["Marble", "Wood", "Brass"],
        recommended_fixtures=["Clawfoot tub", "Pedestal sink", "Classic toilet"],
        estimated_cost_range=CostRange(min_cost=8000.0, max_cost=20000.0),
    ),
    DesignTheme(
        name="Contemporary",
        description="Current trends and modern aesthetics",
        style="Contemporary",
        color_scheme=["Gray", "Blue", "White"],
        materials=["Porcelain", "Chrome", "Glass"],
        recommended_fixtures=["Smart toilet", "LED mirror", "Rain shower"],
        estimated_cost_range=CostRange(min_cost=10000.0, max_cost=25000.0),
    ),
]

app = FastAPI(
    title="Bathroom Designer API",
    description="API for designing and managing bathroom layouts",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/bathroom/", response_model=BathRoom)
async def create_bathroom(bathroom: BathRoom):
    """
    Create a new bathroom design
    """
    BATHROOMS[bathroom.id] = bathroom
    return bathroom


@app.get("/bathroom/{bathroom_id}", response_model=BathRoom)
async def get_bathroom(bathroom_id: UUID):
    """
    Retrieve a specific bathroom design
    """
    if bathroom_id not in BATHROOMS:
        raise HTTPException(status_code=404, detail="Bathroom not found")
    return BATHROOMS[bathroom_id]


@app.post("/bathroom/{bathroom_id}/fixtures", response_model=Fixture)
async def add_fixture(bathroom_id: UUID, fixture: Fixture):
    """
    Add a new fixture to a bathroom
    """
    if bathroom_id not in BATHROOMS:
        raise HTTPException(status_code=404, detail="Bathroom not found")
    bathroom = BATHROOMS[bathroom_id]
    bathroom.fixtures.append(fixture)
    return fixture


@app.get("/design-themes/", response_model=List[DesignTheme])
async def get_design_themes() -> List[DesignTheme]:
    """
    Get all available design themes
    """
    return DESIGN_THEMES


@app.put("/bathroom/{bathroom_id}/fixture/{fixture_id}", response_model=Fixture)
async def update_fixture(bathroom_id: UUID, fixture_id: UUID, fixture: Fixture):
    """
    Update a specific fixture in a bathroom
    """
    if bathroom_id not in BATHROOMS:
        raise HTTPException(status_code=404, detail="Bathroom not found")
    if fixture.id != fixture_id:
        raise HTTPException(status_code=400, detail="Fixture ID mismatch")

    bathroom = BATHROOMS[bathroom_id]
    for i, existing_fixture in enumerate(bathroom.fixtures):
        if existing_fixture.id == fixture_id:
            bathroom.fixtures[i] = fixture
            return fixture
    raise HTTPException(status_code=404, detail="Fixture not found")


@app.put("/bathroom/{bathroom_id}/wall/{wall_id}", response_model=WallFeature)
async def update_wall(bathroom_id: UUID, wall_id: UUID, wall: WallFeature):
    """
    Update a specific wall in a bathroom
    """
    if bathroom_id not in BATHROOMS:
        raise HTTPException(status_code=404, detail="Bathroom not found")
    if wall.id != wall_id:
        raise HTTPException(status_code=400, detail="Wall ID mismatch")

    bathroom = BATHROOMS[bathroom_id]
    for i, existing_wall in enumerate(bathroom.walls):
        if existing_wall.id == wall_id:
            bathroom.walls[i] = wall
            return wall
    raise HTTPException(status_code=404, detail="Wall not found")


@app.put("/bathroom/{bathroom_id}/window/{window_id}", response_model=Window)
async def update_window(bathroom_id: UUID, window_id: UUID, window: Window):
    """
    Update a specific window in a bathroom
    """
    if bathroom_id not in BATHROOMS:
        raise HTTPException(status_code=404, detail="Bathroom not found")
    if window.id != window_id:
        raise HTTPException(status_code=400, detail="Window ID mismatch")

    bathroom = BATHROOMS[bathroom_id]
    for i, existing_window in enumerate(bathroom.windows):
        if existing_window.id == window_id:
            bathroom.windows[i] = window
            return window
    raise HTTPException(status_code=404, detail="Window not found")


@app.put("/bathroom/{bathroom_id}/door/{door_id}", response_model=Door)
async def update_door(bathroom_id: UUID, door_id: UUID, door: Door):
    """
    Update a specific door in a bathroom
    """
    if bathroom_id not in BATHROOMS:
        raise HTTPException(status_code=404, detail="Bathroom not found")
    if door.id != door_id:
        raise HTTPException(status_code=400, detail="Door ID mismatch")

    bathroom = BATHROOMS[bathroom_id]
    for i, existing_door in enumerate(bathroom.doors):
        if existing_door.id == door_id:
            bathroom.doors[i] = door
            return door
    raise HTTPException(status_code=404, detail="Door not found")


@app.put("/bathroom/{bathroom_id}/ventilation/{vent_id}", response_model=Ventilation)
async def update_ventilation(
    bathroom_id: UUID, vent_id: UUID, ventilation: Ventilation
):
    """
    Update a specific ventilation in a bathroom
    """
    if bathroom_id not in BATHROOMS:
        raise HTTPException(status_code=404, detail="Bathroom not found")
    if ventilation.id != vent_id:
        raise HTTPException(status_code=400, detail="Ventilation ID mismatch")

    bathroom = BATHROOMS[bathroom_id]
    for i, existing_vent in enumerate(bathroom.ventilation):
        if existing_vent.id == vent_id:
            bathroom.ventilation[i] = ventilation
            return ventilation
    raise HTTPException(status_code=404, detail="Ventilation not found")


@app.delete("/bathroom/{bathroom_id}/{component_type}/{component_id}")
async def delete_component(
    bathroom_id: UUID,
    component_id: UUID,
    component_type: str = Path(..., regex="^(fixture|wall|window|door|ventilation)$"),
):
    """
    Delete a specific component from a bathroom
    """
    if bathroom_id not in BATHROOMS:
        raise HTTPException(status_code=404, detail="Bathroom not found")

    bathroom = BATHROOMS[bathroom_id]
    component_list = getattr(bathroom, f"{component_type}s")

    for i, component in enumerate(component_list):
        if component.id == component_id:
            component_list.pop(i)
            return {
                "status": "success",
                "message": f"{component_type} deleted successfully",
            }

    raise HTTPException(status_code=404, detail=f"{component_type} not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
