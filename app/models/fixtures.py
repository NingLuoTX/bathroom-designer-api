from enum import Enum
from typing import Dict
from .base import (
    BaseModel,
    Dimension,
    Position,
    Material,
    Field,
    Optional,
    List,
    UUID,
    uuid4,
)


class FixtureType(str, Enum):
    TOILET = "toilet"
    SINK = "sink"
    SHOWER = "shower"
    BATHTUB = "bathtub"
    VANITY = "vanity"
    MIRROR = "mirror"
    LIGHTING = "lighting"
    TOWEL_BAR = "towel_bar"
    TOILET_PAPER_HOLDER = "toilet_paper_holder"


class FixtureStyle(str, Enum):
    MODERN = "modern"
    TRADITIONAL = "traditional"
    CONTEMPORARY = "contemporary"
    RUSTIC = "rustic"
    INDUSTRIAL = "industrial"
    MINIMALIST = "minimalist"


class Fixture(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    fixture_type: FixtureType
    name: str
    manufacturer: str
    model_number: str
    dimension: Dimension
    position: Position
    style: FixtureStyle
    material: Material
    color: str
    is_existing: bool = False
    replacement_for: Optional[UUID] = None  # ID of fixture being replaced
    installation_requirements: Dict[str, str] = {}
    plumbing_requirements: Optional[Dict[str, str]]
    electrical_requirements: Optional[Dict[str, str]]
    cost: float
    weight: Optional[float]


class Toilet(Fixture):
    flush_type: str
    water_usage: float  # gallons per flush
    height: float  # comfort height or standard
    rough_in: float  # distance from wall to center of drain


class Sink(Fixture):
    mount_type: str  # pedestal, wall-mounted, undermount, vessel
    faucet_holes: int
    drain_type: str


class Shower(Fixture):
    enclosure_type: str  # frameless, framed, walk-in
    door_type: Optional[str]
    drain_position: Position
    shower_head_type: List[str]
    valve_type: str


class Bathtub(Fixture):
    tub_type: str  # freestanding, alcove, corner, drop-in
    water_capacity: float
    has_jets: bool
    jet_count: Optional[int]


class WallFeature(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    position: Position
    dimension: Dimension
    material: Optional[Material] = None


class Window(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    position: Position
    dimension: Dimension
    window_type: str  # e.g., "sliding", "casement", "fixed"
    material: Optional[Material] = None
    is_openable: bool = True


class Door(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    position: Position
    dimension: Dimension
    door_type: str  # e.g., "hinged", "sliding", "pocket"
    material: Optional[Material] = None
    swing_direction: Optional[str] = None  # "inward" or "outward"


class Ventilation(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    ventilation_type: str  # e.g., "natural", "mechanical", "hybrid"
    capacity: Optional[float] = None  # in cubic meters per hour
    position: Optional[Position] = None
