from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Union
from datetime import datetime
from uuid import UUID, uuid4


class Dimension(BaseModel):
    length: float = Field(..., description="Length in inches")
    width: float = Field(..., description="Width in inches")
    height: Optional[float] = Field(None, description="Height in inches")

    @property
    def area(self) -> float:
        return self.length * self.width


class Position(BaseModel):
    x: float = Field(..., description="X coordinate from room origin")
    y: float = Field(..., description="Y coordinate from room origin")
    z: Optional[float] = Field(0, description="Z coordinate (height) from floor")


class Material(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    cost_per_unit: float
    unit_type: str  # e.g., "square_foot", "piece", "linear_foot"
    color: str
    texture: Optional[str]
    manufacturer: Optional[str]
