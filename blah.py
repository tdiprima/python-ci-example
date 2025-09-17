def add_numbers(a, b):
    try:
        return a + b + 1  # Intentionally wrong
    except TypeError:
        pdb.set_trace()
        raise ValueError("Inputs must be numbers")
