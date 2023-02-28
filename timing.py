"""
Functions for plotting timing data.
"""

from timeit import timeit

import networkx as nx
import matplotlib.pyplot as plt

def get_timing_data(functions: dict[str, tuple], graphs: tuple[nx.Graph]) -> dict[str, tuple]:
    """
    Get timing data for a set of functions.

    Parameters
    ----------
    functions : dict[str, tuple]
        Dictionary of functions and their parameters.
    graphs : tuple[nx.Graph]
        Tuple of graphs to use for timing.

    Returns
    -------
    dict[str, tuple]
        Dictionary of timing data.
    """
    timing_data = {}

    for func_name, value in functions.items():
        func = value[0]

        timing_data[func_name] = ([], [])

        for graph in graphs:
            timing_data[func_name][0].append(len(graph.nodes))

            timing_data[func_name][1].append(
                timeit(
                    lambda: func(graph),
                    number=1
                )
            )

    return timing_data

def plot_timing_data(timing_data, title=None, xlabel=None, ylabel=None):
    """
    Plot timing data.

    Parameters
    ----------
    timing_data : dict
        Dictionary of timing data.
    title : str, optional
        Title for the plot.
    xlabel : str, optional
        Label for the x-axis.
    ylabel : str, optional
        Label for the y-axis.
    """
    fig, axp = plt.subplots()

    for key, value in timing_data.items():
        plt.plot(
            value[0], value[1],
            marker='o',
            linestyle='--',
            color=['c', 'm', 'y'][list(timing_data.keys()).index(key)],
            label=key
        )

    axp.legend()

    if title is not None:
        axp.set_title(title)

    if xlabel is not None:
        axp.set_xlabel(xlabel)

    if ylabel is not None:
        axp.set_ylabel(ylabel)

    fig.show()
