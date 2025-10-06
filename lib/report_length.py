def report_length(string):
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    length = len(string)
    return f"This string was {length} characters long."