# simple function with basic error handling
import pdb  # For debugging


def add_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Inputs must be numbers")
    try:
        return a + b
    except TypeError:
        pdb.set_trace()  # Breakpoint for debugging if types mismatch
        raise ValueError("Inputs must be numbers")
