"""Public package interface for ``geometor.mascheroni``."""

from __future__ import annotations

from .app import main, run
from .compass import (
    OpCount,
    circle_circle_intersection,
    collinear_doubling,
    concentric_fourth_proportional,
    mascheroni_inversion,
    mascheroni_midpoint,
    mascheroni_parallel_point,
    mascheroni_reflect_point,
)

__version__ = "0.1.0"

__all__ = [
    "OpCount",
    "__version__",
    "circle_circle_intersection",
    "collinear_doubling",
    "concentric_fourth_proportional",
    "main",
    "mascheroni_inversion",
    "mascheroni_midpoint",
    "mascheroni_parallel_point",
    "mascheroni_reflect_point",
    "run",
]
