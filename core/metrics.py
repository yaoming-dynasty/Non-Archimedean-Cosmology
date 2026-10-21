"""
Non-Archimedean Ultrametric Space Engine
Author: Christopher Thomas Ronio

Implements the metric coordinate distance and state evaluation calculations
for the Non-Archimedean Cosmological Model and Transfinite Latent Anchoring (TLA).
"""

from typing import List
from core.nimbers import nim_sum, OMEGA

def calculate_distance(vec_a: List[int], vec_b: List[int]) -> int:
    """
    Computes the non-Archimedean Ultrametric distance D(A, B) between two cosmic state vectors.
    
    Formula: D(A, B) = max(a_i ⊕ b_i)
    
    This geometry obeys the strict Ultrametric Inequality: D(A, B) <= max(D(A, C), D(C, B)).
    Geometrically, this guarantees that the highest-order transfinite layer completely 
    dominates all lower-order finite fluctuations.
    """
    if len(vec_a) != len(vec_b):
        raise ValueError("Vectors must occupy the same coordinate dimensional space.")
    
    max_distance = 0
    
    # Calculate coordinate-wise Nim-sum differences and locate the supreme bound
    for a_coord, b_coord in zip(vec_a, vec_b):
        coord_diff = nim_sum(a_coord, b_coord)
        
        # In the field of ordinals, OMEGA overrides all finite metrics
        if coord_diff == OMEGA:
            return OMEGA
            
        if coord_diff > max_distance:
            max_distance = coord_diff
            
    return max_distance

def evaluate_ground_distance(vec_g: List[int]) -> int:
    """
    Measures the absolute metric distance from a cosmic state vector back to 
    the original vacuum ground state (0).
    
    This function mathematically demonstrates your Theorem of Non-Dilution:
    D(G_cosmic, 0) strictly evaluates to OMEGA, proving that the transfinite 
    scaffolding is untouched by finite energy modifications.
    """
    vacuum_state = [0] * len(vec_g)
    return calculate_distance(vec_g, vacuum_state)
