from src.numerical_field_statistics import find_average_on_numeric_field
from src.numerical_field_statistics import find_median_on_numeric_field
from src.numerical_field_statistics import find_mode_on_numeric_field
from src.numerical_field_statistics import find_standard_deviation_on_numeric_field
from src.numerical_field_statistics import find_percentiles_on_numeric_field


def find_statistics_on_charges_for_categorical_field(data: list[dict], field_name: str):
    """
    Find the average, median, mode, standard deviation and percentiles of the charges for each value of a categorical field in a list of dictionaries.

    Args:
        data (list): A list of dictionaries.
        field_name (str): The name of the field to find the statistics of.

    Returns:
        dict: A dictionary with the values of the categorical field as keys and a list of the average, median, mode, and standard deviation of the charges for each value of the categorical field as values.
    """
    # Find the unique values of the field
    unique_values = set([row[field_name] for row in data])

    # Create a dictionary to store the statistics
    statistics = {}

    # Find the average, median, mode, and standard deviation of the charges for each value of the categorical field
    for value in unique_values:
        statistics[value] = {}
        statistics[value]['average'] = find_average_on_numeric_field(
            [row for row in data if row[field_name] == value], 'charges')
        statistics[value]['median'] = find_median_on_numeric_field(
            [row for row in data if row[field_name] == value], 'charges')
        statistics[value]['mode'] = find_mode_on_numeric_field(
            [row for row in data if row[field_name] == value], 'charges')
        statistics[value]['standard deviation'] = find_standard_deviation_on_numeric_field(
            [row for row in data if row[field_name] == value], 'charges')
        statistics[value]['percentiles'] = find_percentiles_on_numeric_field(
            [row for row in data if row[field_name] == value], 'charges')

    return statistics


def create_box_plot_for_categorical_field(data: list[dict], field_name: str):
    """
    Create a box plot for each value of a categorical field in a list of dictionaries.

    Args:
        data (list): A list of dictionaries.
        field_name (str): The name of the field to create the box plot for.
    """
    from matplotlib import pyplot as plt

    # Find the unique values of the field
    unique_values = set([row[field_name] for row in data])

    # Create a figure
    fig, axes = plt.subplots(1, len(unique_values), figsize=(10, 5))

    # Create a box plot for each value of the categorical field
    for i, value in enumerate(unique_values):
        # Create a list of the values of the field
        values = [float(row['charges']) for row in data if row[field_name] == value]

        # Create the box plot
        axes[i].boxplot(values, vert=False)
        axes[i].set_title(value)
        axes[i].set_yticklabels([])

    # Show the figure
    plt.show()
