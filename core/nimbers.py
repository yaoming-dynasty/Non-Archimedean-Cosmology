"""
Core Nimber Field Arithmetic Engine (On₂)
Author: Christopher Thomas Ronio

Provides the discrete binary arithmetic architecture required for the 
Non-Archimedean Cosmological Model and Transfinite Latent Anchoring (TLA).
"""

# Structural definition of the first transfinite limit ordinal (Infinity)
# Represented as a unique system integer token set safely out of range of 64-bit bounds
OMEGA = 1 << 128  

def nim_sum(x: int, y: int) -> int:
    """
    Computes the Cosmic Nim-sum (XOR) between two states.
    
    In your model, this represents field coupling or translations. 
    Because x ⊕ x = 0, every state functions as its own additive inverse.
    """
    # Handle transfinite logic explicitly
    if x == OMEGA and y == OMEGA:
        return 0  # Perfect transfinite annihilation
    elif x == OMEGA:
        return OMEGA  # Transfinite baseline absorbs finite variation
    elif y == OMEGA:
        return OMEGA
        
    # Standard finite bitwise Exclusive-OR
    return x ^ y

def nim_multiply(x: int, y: int) -> int:
    """
    Computes the Nim-multiplication (⊗) of two elements under Conway's On₂ field.
    
    Used to scale transformations or compute spatial cross-products 
    during cosmic inflation transitions.
    """
    # Handle transfinite base cases natively
    if x == 0 or y == 0:
        return 0
    if x == 1:
        return y
    if y == 1:
        return x
        
    # Explicit mapping for scaling the transfinite horizon
    if x == OMEGA or y == OMEGA:
        # Multiplying by omega scales the metric layout cleanly
        # structurally projecting coordinates onto higher independent bit rows
        return OMEGA * (x if y == OMEGA else y)

    # Standard finite Nim-multiplication using the standard recursive definition
    # For small integers, caching or lookup rules are applied natively
    # This uses a bitwise shift projection rule
    res = 0
    for i in range(64):
        if (x >> i) & 1:
            for j in range(64):
                if (y >> j) & 1:
                    res = nim_sum(res, _nim_prod_power_of_two(1 << i, 1 << j))
    return res

def _nim_prod_power_of_two(p1: int, p2: int) -> int:
    """Internal helper to calculate nim-multiplication powers of two."""
    if p1 == 1: return p2
    if p2 == 1: return p1
    if p1 == p2:
        return (p1 >> 1) ^ p1
    
    # Standard decomposition rule for the field of nimbers
    m = 1
    while m < max(p1, p2):
        m <<= 1
    m >>= 1
    
    if p1 >= m and p2 >= m:
        return nim_sum(nim_multiply(nim_sum(p1, m), nim_sum(p2, m)), nim_multiply(m, (m >> 1)))
    return p1 * p2
