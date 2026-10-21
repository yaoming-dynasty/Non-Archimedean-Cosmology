"""
Multi-Dimensional State Vector Engine (O₂ⁿ)
Author: Christopher Thomas Ronio

Manages creation, field translation, and manipulation of coordinate vectors 
representing cosmic states or AI cognitive profiles under Nim-Geometry rules.
"""

from typing import List, Union
from core.nimbers import nim_sum, nim_multiply, OMEGA

class CosmicVector:
    """
    Represents a coordinate vector in a non-Archimedean multi-dimensional space.
    Used to track the physical attributes of the universe or AI latent states.
    """
    def __init__(self, coordinates: List[Union[int, float]]):
        # Cast coordinates to integers or the OMEGA system token natively
        self.coords = [int(c) if c != OMEGA else OMEGA for c in coordinates]
        self.dimensions = len(self.coords)

    def __repr__(self) -> str:
        readable_coords = ["ω" if c == OMEGA else str(c) for c in self.coords]
        return f"CosmicVector({', '.join(readable_coords)})"

    def nim_add(self, other: 'CosmicVector') -> 'CosmicVector':
        """
        Translates this vector by another vector using coordinate-wise Nim-summation (⊕).
        
        Formula: A ⊕ B
        Because x ⊕ x = 0, translating by the exact same vector twice yields 0,
        enforcing closed-loop trajectories natively.
        """
        if self.dimensions != other.dimensions:
            raise ValueError("Vector dimensions must match for field operations.")
            
        new_coords = [nim_sum(s, o) for s, o in zip(self.coords, other.coords)]
        return CosmicVector(new_coords)

    def nim_scale(self, scalar: int) -> 'CosmicVector':
        """
        Scales the vector components using Nim-multiplication (⊗).
        Used to calculate cross-dimensional projections during cosmic inflation.
        """
        new_coords = [nim_multiply(c, scalar) for c in self.coords]
        return CosmicVector(new_coords)

    def get_coordinates(self) -> List[int]:
        """Returns the raw ordinal array representation of the vector."""
        return self.coords
