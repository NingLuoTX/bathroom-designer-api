from enum import Enum
from typing import Dict, List, Optional, Tuple
from .base import BaseModel, Field, Material, UUID, uuid4


class DesignStyle(str, Enum):
    MODERN = "modern"
    TRADITIONAL = "traditional"
    CONTEMPORARY = "contemporary"
    RUSTIC = "rustic"
    INDUSTRIAL = "industrial"
    MINIMALIST = "minimalist"
    COASTAL = "coastal"
    FARMHOUSE = "farmhouse"


class ColorScheme(BaseModel):
    primary_color: str
    secondary_color: str
    accent_colors: List[str]


class CostRange(BaseModel):
    min_cost: float
    max_cost: float


class DesignTheme(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    style: str = Field(default="Modern")
    color_scheme: List[str] = Field(default_factory=lambda: ["White", "Gray"])
    materials: List[str] = Field(default_factory=lambda: ["Ceramic", "Glass"])
    recommended_fixtures: List[str] = Field(default_factory=lambda: ["Sink", "Toilet"])
    estimated_cost_range: CostRange = Field(
        default_factory=lambda: CostRange(min_cost=1000.0, max_cost=5000.0)
    )

    class Config:
        arbitrary_types_allowed = True
