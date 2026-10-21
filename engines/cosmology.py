"""
Non-Archimedean Cosmological Model Simulation Engine
Author: Christopher Thomas Ronio

Simulates the early universe transfinite singularity metrics and executes 
cosmic inflation projections using non-Archimedean Nim-Matrix Transformations.
"""

from typing import List, Tuple
from core import CosmicVector, nim_multiply, nim_sum, OMEGA, evaluate_ground_distance

class NonArchimedeanCosmology:
    def __init__(self):
        """Initializes the model workspace, anchoring the early state to OMEGA."""
        # Pre-inflationary universe vector: G_early = [0, 0, ω]
        self.g_early = CosmicVector([0, 0, OMEGA])

    def get_initial_state(self) -> CosmicVector:
        """Returns the pristine, un-diluted transfinite initial state vector."""
        return self.g_early

    def execute_inflation(self, alpha: int, beta: int) -> CosmicVector:
        """
        Executes Cosmic Inflation via a non-Archimedean Nim-Matrix Transformation.
        
        Maps the transfinite scalar ω into a spatial superposition of rapidly
        expanding finite components across the coordinate planes.
        
        Matrix T_inflation = 
        [[0, 0, alpha],
         [0, 0, beta ],
         [0, 0, 0    ]]
        """
        if alpha >= OMEGA or beta >= OMEGA:
            raise ValueError("Inflation parameters must be strictly finite (less than ω).")

        # Row-by-row matrix multiplication evaluation using Nim-arithmetic rules
        # Row 1: (0⊗0) ⊕ (0⊗0) ⊕ (alpha⊗ω) = alpha ⊗ ω
        coord_x = nim_multiply(alpha, OMEGA)
        # Row 2: (0⊗0) ⊕ (0⊗0) ⊕ (beta⊗ω) = beta ⊗ ω
        coord_y = nim_multiply(beta, OMEGA)
        # Row 3: (0⊗0) ⊕ (0⊗0) ⊕ (0⊗ω) = 0
        coord_z = 0

        self.g_post = CosmicVector([coord_x, coord_y, coord_z])
        return self.g_post

    def verify_stability(self, finite_fluctuations: List[int]) -> Tuple[int, bool]:
        """
        Verifies that localized generation of finite particles or energy fluctuations
        cannot dilute or warp the background transfinite metric distance.
        """
        if not hasattr(self, 'g_post'):
            # If inflation hasn't run, use the early state
            state = self.g_early
        else:
            state = self.g_post

        fluc_vector = CosmicVector(finite_fluctuations)
        # Apply the field interaction via coordinate-wise Nim-summation (⊕)
        g_new = state.nim_add(fluc_vector)
        
        # Calculate metric distance back to absolute vacuum ground state (0)
        distance = evaluate_ground_distance(g_new.get_coordinates())
        
        # Check if the transfinite anchor remains intact
        is_stable = (distance == OMEGA)
        return distance, is_stable
