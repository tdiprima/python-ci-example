# simple function with basic error handling
import pdb  # For debugging


def add_numbers(a, b):
    try:
        return a + b
    except TypeError:
        pdb.set_trace()  # Breakpoint for debugging if types mismatch
        raise ValueError("Inputs must be numbers")
