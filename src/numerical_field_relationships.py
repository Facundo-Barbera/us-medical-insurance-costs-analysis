def find_lowest_and_highest_values(data: list[dict], field_name: str):
    """
    Find the lowest and highest values of a field in a list of dictionaries.

    Args:
        data (list): A list of dictionaries.
        field_name (str): The name of the field to find the lowest and highest values of.

    Returns:
        tuple: The lowest and highest values of the field.
    """
    # Create a list of the values of the field
    values = [float(row[field_name]) for row in data]

    # Find the lowest and highest values
    lowest_value = min(values)
    highest_value = max(values)

    return lowest_value, highest_value


def divide_leading_field_into_groups(data: list[dict], leading_field_name: str, num_groups: int):
    """
    Divide a leading field into groups.

    Args:
        data (list): A list of dictionaries.
        leading_field_name (str): The name of the leading field.
        num_groups (int): The number of groups to divide the leading field into.

    Returns:
        list: A list of tuples, where each tuple contains the lower and upper bounds of a group.
    """
    # Find the lowest and highest values of the leading field
    lowest_value, highest_value = find_lowest_and_highest_values(data, leading_field_name)

    # Divide the leading field into groups with an integer number of values in each group
    group_size = (highest_value - lowest_value) // num_groups  # use integer division to get an integer group size
    groups = [(lowest_value + (group_size * i), lowest_value + (group_size * (i + 1) - 1)) for i in
              range(num_groups)]  # exclude the upper bound of the last group

    # Add the upper bound of the last group, which may be different from the previous bounds
    groups.append((lowest_value + (group_size * num_groups), highest_value))

    return groups


def find_relationship_between_two_numeric_fields(data: list[dict], leading_field_name: str, trailing_field_name: str,
                                                 num_groups: int):
    """
    Find the relationship between two numeric fields.

    Args:
        data (list): A list of dictionaries.
        leading_field_name (str): The name of the leading field.
        trailing_field_name (str): The name of the trailing field.
        num_groups (int): The number of groups to divide the leading field into.

    Returns:
        dict: A dictionary where the keys are the groups of the leading fields and the values are the statistics of the trailing field.
    """
    # Divide the leading field into groups
    groups = divide_leading_field_into_groups(data, leading_field_name, trailing_field_name, num_groups)
    print(f'Groups: {groups}')

    def find_median(values: list[float]):
        # Sort the values
        values.sort()

        # Find the median
        if len(values) % 2 == 0:  # if the number of values is even
            median = (values[len(values) // 2] + values[len(values) // 2 - 1]) / 2
        else:  # if the number of values is odd
            median = values[len(values) // 2]

        return median

    def find_mode(values: list[float]):
        # Create a dictionary to store the number of times each value appears
        value_counts = {}

        # Find the number of times each value appears
        for value in values:
            if value in value_counts:
                value_counts[value] += 1
            else:
                value_counts[value] = 1

        # Find the mode
        mode = max(value_counts, key=value_counts.get)

        return mode

    def find_standard_deviation(values: list[float]):
        # Find the average of the values
        average = sum(values) / len(values)

        # Find the standard deviation
        standard_deviation = (sum([(value - average) ** 2 for value in values]) / len(values)) ** 0.5

        return standard_deviation

    def find_percentiles(values: list[float]):
        # Sort the values
        values.sort()

        # Find the percentiles 25, 50, and 75
        percentile_25 = values[len(values) // 4]
        percentile_50 = values[len(values) // 2]
        percentile_75 = values[len(values) // 4 * 3]

        return percentile_25, percentile_50, percentile_75

    # Create a dictionary to store the statistics of the trailing field for each group
    statistics = {}

    # Find the statistics of the trailing field for each group
    for group in groups:
        # Create a list of the values of the trailing field in the group
        values = [float(row[trailing_field_name]) for row in data if
                  group[0] <= float(row[leading_field_name]) <= group[1]]

        # Check if there are any values in the group
        if len(values) == 0:
            continue

        # Find the average, median, mode, standard deviation, and percentiles of the values
        average = sum(values) / len(values)
        median = find_median(values)
        mode = find_mode(values)
        standard_deviation = find_standard_deviation(values)
        percentiles = find_percentiles(values)

        # Store the statistics in the dictionary
        statistics[group] = (average, median, mode, standard_deviation, percentiles)

    return statistics
