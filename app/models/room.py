from enum import Enum

from .fixtures import Door, Fixture, Ventilation, WallFeature, Window
from .base import (
    BaseModel,
    Dimension,
    Material,
    Position,
    Field,
    Optional,
    List,
    UUID,
    uuid4,
)


class RoomShape(str, Enum):
    RECTANGULAR = "rectangular"
    L_SHAPED = "l_shaped"
    IRREGULAR = "irregular"


class WallType(str, Enum):
    STANDARD = "standard"
    TILE = "tile"
    MOISTURE_RESISTANT = "moisture_resistant"
    CONCRETE = "concrete"


class Wall(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    dimension: Dimension
    wall_type: WallType
    features: List[WallFeature] = []
    material: Optional[Material] = None


class BathRoom(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    shape: RoomShape
    dimension: Dimension
    ceiling_height: float
    walls: List[Wall]
    floor_type: Material
    ceiling_type: Material
    fixtures: List[Fixture]
    windows: List[Window]
    doors: List[Door]
    ventilation: Optional[Ventilation]

    class Config:
        arbitrary_types_allowed = True
