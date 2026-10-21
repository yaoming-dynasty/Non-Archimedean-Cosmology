import pytest
from core import calculate_distance, OMEGA

def test_ultrametric_distance_calculations():
    """Verifies that vector distance calculation accurately follows D(A, B) = max(a_i ⊕ b_i)."""
    # Vector A and B with discrete finite coordinates
    # 5 ⊕ 1 = 4 (Binary: 101 XOR 001 = 100)
    # 3 ⊕ 2 = 1 (Binary: 011 XOR 010 = 001)
    vec_a = [5, 3, 0]
    vec_b = [1, 2, 0]
    
    # The max coordinate diff should be max(4, 1, 0) = 4
    distance = calculate_distance(vec_a, vec_b)
    assert distance == 4, f"Expected finite distance of 4, but evaluated to {distance}."

def test_transfinite_domination_metric():
    """Asserts that the presence of OMEGA along any dimension causes the entire metric distance to evaluate to OMEGA."""
    vec_ground = [0, 0, 0]
    vec_transfinite = [999999, 1245, OMEGA]
    
    # Across an ultrametric space, the transfinite component must absorb all finite scales
    evaluated_distance = calculate_distance(vec_transfinite, vec_ground)
    assert evaluated_distance == OMEGA, "The finite coordinates leaked or interfered with the transfinite distance supremum."

def test_vector_dimension_mismatch():
    """Ensures that the metric processor catches and prevents calculation requests on dimensionally mismatched vector spaces."""
    vec_3d = [1, 2, 3]
    vec_2d = [1, 2]
    
    with pytest.raises(ValueError, match="Vectors must occupy the same coordinate dimensional space."):
        calculate_distance(vec_3d, vec_2d)
