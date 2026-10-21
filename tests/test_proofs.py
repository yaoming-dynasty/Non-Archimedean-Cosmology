"""
Automated Proof Verification Suite: Non-Dilution Theorem
Author: Christopher Thomas Ronio

Validates that localized finite fluctuations across coordinate planes
fail to alter the supreme metric boundary of a transfinite system vector.
"""

import pytest
from core import CosmicVector, OMEGA, evaluate_ground_distance
from engines import NonArchimedeanCosmology

def test_mathematical_non_dilution_theorem():
    """
    Validates Theorem: D(G ⊕ E, 0) == D(G, 0) == OMEGA
    Where E represents strictly finite energy parameters.
    """
    cosmology = NonArchimedeanCosmology()
    
    # 1. Capture original pristine transfinite state vector [0, 0, ω]
    g_early = cosmology.get_initial_state()
    initial_dist = evaluate_ground_distance(g_early.get_coordinates())
    assert initial_dist == OMEGA, "Initial singularity baseline metric must be OMEGA."

    # 2. Simulate high-energy finite localized fluctuations (e.g., matter generation)
    # Testing random large numbers strictly below the OMEGA bit column threshold
    finite_matter_variations = [542309, 998124, 12]
    
    # 3. Calculate distance of the translated field using the metric engine
    final_dist, is_stable = cosmology.verify_stability(finite_matter_variations)
    
    # 4. Rigorous assertion of the Non-Dilution framework
    assert is_stable is True, "System stability flag failed under finite additions."
    assert final_dist == OMEGA, "The transfinite scaffolding was dilated or warped by finite code variables."
    assert final_dist == initial_dist, "The metric distance shifted away from its original invariant scale."

def test_post_inflation_non_dilution():
    """Validates that non-dilution holds true even after matrix inflation transitions occur."""
    cosmology = NonArchimedeanCosmology()
    
    # Run matrix-driven inflation mapping ω across spatial x and y boundaries
    cosmology.execute_inflation(alpha=3, beta=7)
    
    # Inject finite environmental fluctuations post-inflation
    fluctuations = [100, 250, 89]
    final_dist, is_stable = cosmology.verify_stability(fluctuations)
    
    assert is_stable is True, "Post-inflation stability validation crashed."
    assert final_dist == OMEGA, "Inflation mapping dropped the coordinate metrics below the transfinite ceiling."
