from matplotlib import pyplot as plt


def find_average_on_numeric_field(data: list[dict], field_name: str) -> float:
    """
    Find the average of a numeric field in a list of dictionaries.
    The average is rounded to two decimal places.

    Args:
        data (list): A list of dictionaries.
        field_name (str): The name of the field to find the average of.

    Returns:
        float: The average of the field.
    """
    return round(sum([float(row[field_name]) for row in data]) / len(data), 2)


def find_median_on_numeric_field(data: list[dict], field_name: str) -> float:
    """
    Find the median of a numeric field in a list of dictionaries.
    The median is rounded to two decimal places.

    Args:
        data (list): A list of dictionaries.
        field_name (str): The name of the field to find the median of.

    Returns:
        float: The median of the field.
    """
    # Sort the data
    sorted_data = sorted([float(row[field_name]) for row in data])

    # Find the median
    if len(sorted_data) % 2 == 0:
        # If the length of the data is even, the median is the average of the two middle values
        median = (sorted_data[len(sorted_data) // 2] + sorted_data[len(sorted_data) // 2 - 1]) / 2
    else:
        # If the length of the data is odd, the median is the middle value
        median = sorted_data[len(sorted_data) // 2]

    return round(median, 2)


def find_mode_on_numeric_field(data: list[dict], field_name: str):
    """
    Find the mode of a numeric field in a list of dictionaries.

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
        if float(row[field_name]) in value_counts:
            value_counts[float(row[field_name])] += 1
        else:
            value_counts[float(row[field_name])] = 1

    # Find the mode
    mode = max(value_counts, key=value_counts.get)

    return mode, value_counts[mode]


def find_standard_deviation_on_numeric_field(data: list[dict], field_name: str) -> float:
    """
    Find the standard deviation of a numeric field in a list of dictionaries.
    The standard deviation is rounded to two decimal places.

    Args:
        data (list): A list of dictionaries.
        field_name (str): The name of the field to find the standard deviation of.

    Returns:
        float: The standard deviation of the field.
    """
    # Find the average
    average = find_average_on_numeric_field(data, field_name)

    # Find the sum of the squared differences between each value and the average
    sum_of_squared_differences = sum([(float(row[field_name]) - average) ** 2 for row in data])

    # Find the standard deviation
    standard_deviation = (sum_of_squared_differences / len(data)) ** 0.5

    return round(standard_deviation, 2)


def find_percentiles_on_numeric_field(data: list[dict], field_name: str) -> tuple[float, float, float]:
    """
    Find the 25th, 50th, and 75th percentiles of a numeric field in a list of dictionaries.
    The percentiles are rounded to two decimal places.

    Args:
        data (list): A list of dictionaries.
        field_name (str): The name of the field to find the percentiles of.

    Returns:
        tuple: The 25th, 50th, and 75th percentiles of the field.
    """
    # Sort the data
    sorted_data = sorted([float(row[field_name]) for row in data])

    # Find the percentiles
    percentile_25 = sorted_data[len(sorted_data) // 4]
    percentile_50 = sorted_data[len(sorted_data) // 2]
    percentile_75 = sorted_data[len(sorted_data) // 4 * 3]

    return round(percentile_25, 2), round(percentile_50, 2), round(percentile_75, 2)


def plot_box_plots_for_numerical_fields(data, fields):
    # Create a figure
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))

    # Loop through the numerical fields
    for i, field in enumerate(fields):
        # Get the row and column of the subplot
        plot_row = i // 2
        plot_col = i % 2

        # Create a list of the values of the field
        values = [float(row[field.lower()]) for row in data]

        # Create the boxplot
        axes[plot_row, plot_col].boxplot(values, vert=False)
        axes[plot_row, plot_col].set_title(field)
        axes[plot_row, plot_col].set_yticklabels([])

    # Show the figure
    plt.show()


def plot_histograms_for_numerical_fields(data, fields):
    from matplotlib import pyplot as plt

    # Create a figure
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))

    # Loop through the numerical fields
    for i, field in enumerate(fields):
        # Get the row and column of the subplot
        plot_row = i // 2
        plot_col = i % 2

        # Create a list of the values of the field
        values = [float(row[field.lower()]) for row in data]

        # Create the histogram
        axes[plot_row, plot_col].hist(values)
        axes[plot_row, plot_col].set_title(field)

    # Show the figure
    plt.show()
