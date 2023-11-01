#!/usr/bin/python3
"""
lazy_matrix module
This function calculates multiplication of matrices using numpy library.

"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return a new matrix with the product of m_a and m_b.
    
    Args:
        m_a (list of list): A matrix.
        m_b (list of list): A matrix.

    Returns:
        np.ndarray: The resulting matrix.

    Raises:
        TypeError: If m_a or m_b is not a list of lists.
        ValueError: If m_a and m_b cannot be multiplied.

    """
    return (np.matmul(m_a, m_b))
