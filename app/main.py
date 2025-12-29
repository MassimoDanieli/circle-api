from __future__ import annotations

import math
from typing import Literal, Optional

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI(title="Circle API", version="1.0.0")


class CircleResponse(BaseModel):
    radius: float = Field(..., gt=0, description="Circle radius (> 0)")
    area: float = Field(..., description="Area of the circle")
    circumference: float = Field(..., description="Circumference of the circle")
    units: Optional[str] = Field(None, description="Unit label (optional)")
    pi: Literal["math.pi"] = "math.pi"


@app.get("/healthz")
def healthz() -> dict:
    return {"ok": True}


@app.get("/circle", response_model=CircleResponse)
def circle(
    radius: float = Query(..., gt=0, description="Radius (>0)"),
    units: Optional[str] = Query(None, description="Optional units label, e.g. 'cm'"),
) -> CircleResponse:
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return CircleResponse(
        radius=radius,
        area=area,
        circumference=circumference,
        units=units,
    )

