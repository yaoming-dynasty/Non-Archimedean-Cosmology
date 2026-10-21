"""
Core Mathematical Field Execution Package Initializer
Author: Christopher Thomas Ronio

Exposes the foundational non-Archimedean components, nimber arithmetic, 
and ultrametric calculation algorithms to the system-level simulation engines.
"""

from core.nimbers import nim_sum, nim_multiply, OMEGA
from core.vectors import CosmicVector
from core.metrics import calculate_distance, evaluate_ground_distance

__all__ = [
    "nim_sum",
    "nim_multiply",
    "OMEGA",
    "CosmicVector",
    "calculate_distance",
    "evaluate_ground_distance",
]
