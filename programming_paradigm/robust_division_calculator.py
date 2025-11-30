def safe_divide(numerator, denominator):
    """
    Performs division with error handling for division by zero and non-numeric input.
    
    Args:
        numerator: The dividend (can be string or numeric)
        denominator: The divisor (can be string or numeric)
    
    Returns:
        str or float: Error message or the result of division
    """
    try:
        # Attempt to convert arguments to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division
        result = num / denom
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
