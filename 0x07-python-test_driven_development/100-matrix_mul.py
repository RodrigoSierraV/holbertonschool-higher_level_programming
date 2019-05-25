#!/usr/bin/python3
"""function that multiplies 2 matrices
   Args:
        m_a: list of lists of integers or floats
        m_b: list of lists of integers or floats
"""


def matrix_mul(m_a, m_b):
    """Raises: TypeError if m_a or m_b aren't lists of lists, if each one
       doesn't have the same len of elements
               ValueError if lists are empty or can't be multiplied"""
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if False in [isinstance(mat, list) for mat in m_a]:
        raise TypeError('m_a must be a list of lists')
    if False in [isinstance(mat1, list) for mat1 in m_b]:
        raise TypeError('m_b must be a list of lists')
    if not any(m_a):
        raise ValueError("m_a can't be empty")
    if not any(m_b):
        raise ValueError("m_b can't be empty")
    if False in [isinstance(a, int) for b in m_a for a in b] and\
            False in [isinstance(c, float) for d in m_a for c in d]:
        raise TypeError('m_a should contain only integers or floats')
    if False in [isinstance(f, int) for g in m_b for f in g] and\
            False in [isinstance(h, float) for k in m_b for h in k]:
        raise TypeError('m_b should contain only integers or floats')
    if False in [len(m_a[0]) is len(m) for m in m_a]:
        raise TypeError('each row of m_a must should be of the same size')
    if False in [len(m_b[0]) is len(n) for n in m_b]:
        raise TypeError('each row of m_b must should be of the same size')
    if len(m_b) is not len(m_a[0]):
        raise ValueError("m_a and m_b can't be multiplied")
    A = np.array(m_a)
    B = np.array(m_b)

    return A.dot(B)
