#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if type(m_a) is not list:
        raise TypeError(listErr.format('m_a'))
    if type(m_b) is not list:
        raise TypeError(listErr.format('m_b'))

    if len(m_a) == 0 or type(m_a[0]) is list and len(m_a[0]) == 0:
        raise ValueError(emptyErr.format('m_a'))
    if len(m_b) == 0 or type(m_b[0]) is list and len(m_b[0]) == 0:
        raise ValueError(emptyErr.format('m_b'))

    s = -1

    for x in m_a:
        if type(x) is list:
            if s == -1:
                s = len(x)
            else:
                if s != len(x):
                    raise TypeError(sizeErr.format('m_a'))
            for y in x:
                if not isinstance(y, (int, float)):
                    raise TypeError(typeErr.format('m_a'))
        else:
            raise TypeError(typeErr.format('m_a'))

    s = -1

    for x in m_b:
        if isinstance(x, list):
            if s == -1:
                s = len(x)
            else:
                if s != len(x):
                    raise TypeError(sizeErr.format('m_b'))
            for y in x:
                if not isinstance(y, (int, float)):
                    raise TypeError(typeErr.format('m_b'))
        else:
            raise TypeError(typeErr.format('m_b'))

    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    final = [[0 for a in m_b[0]] for x in m_a]
    for i in range(len(m_a)):
        for n in range(len(m_b[0])):
            for k in range(len(m_b)):
                final[i][n] += m_a[i][k] * m_b[k][n]

    return final
