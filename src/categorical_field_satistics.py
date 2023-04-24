def find_mode_on_categorical_field(data: list[dict], field_name: str):
    """
    Find the mode of a categorical field in a list of dictionaries.

    Args:
        data (list): A list of dictionaries.
        field_name (str): The name of the field to find the mode of.

    Returns:
        tuple: The mode of the field and the number of times the mode appears.
    """
    # Create a dictionary to store the number of times each value appears
    value_counts = {}

    # Count the number of times each value appears
    for row in data:
        if row[field_name] in value_counts:
            value_counts[row[field_name]] += 1
        else:
            value_counts[row[field_name]] = 1

    # Find the mode
    mode = max(value_counts, key=value_counts.get)

    return mode, value_counts[mode]