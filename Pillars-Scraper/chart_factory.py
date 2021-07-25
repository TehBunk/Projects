

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_timeframe(dataframe):
    return dataframe.columns


def reverse_order(dataframe):
    return dataframe.iloc[:, ::-1]


def get_xvalues(dataframe):
    return get_timeframe(reverse_order(dataframe))


# Create a bar chart with given data
def chart_bar(dataframe, *datatypes, labels=False, stacked=False, legend=True, ylabel=None, xlabel=None, title=None, xrotation='90', more_yticks=True):
    x_values = get_xvalues(dataframe)
    reverse = reverse_order(dataframe)

    fig, ax = plt.subplots()

    x = np.arange(len(x_values)) * \
        (1 if stacked else (len(datatypes)/2))  # the label locations
    width = 0.01 * len(x_values)  # the width of the bars
    loops = 1
    # for each datatype create the bars for said datatype
    for datatype in datatypes:
        bar_data = pd.to_numeric(reverse.loc[datatype])
        position = (x if stacked else (x + (width * loops)))
        bar = ax.bar(position, bar_data, width, label=datatype)
        if (labels):
            ax.bar_label(bar, padding=3)
        loops += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    if (ylabel != None):
        ax.set_ylabel(ylabel)
    if (xlabel != None):
        ax.set_xlabel(xlabel)
    if (title != None):
        ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(x_values)

    if (legend):
        ax.legend()
    if (more_yticks):
        plt.locator_params(axis="y", nbins=(len(x_values) / 1.5))

    fig.tight_layout()
    plt.xticks(rotation=xrotation)

    plt.show()


def chart_stem(dataframe, datatype, ylabel=None, xlabel=None, title=None, xrotation='90', more_yticks=True):
    x_values = get_xvalues(dataframe)
    reverse = reverse_order(dataframe).loc[datatype]

    fig = plt.figure()

    if (ylabel != None):
        plt.ylabel(ylabel)
    if (xlabel != None):
        plt.xlabel(xlabel)
    if (title != None):
        fig.suptitle(title)
    if (more_yticks):
        plt.locator_params(axis="y", nbins=(len(x_values) / 1.5))

    plt.xticks(rotation=xrotation)
    plt.stem(x_values, reverse)
    plt.show()


def chart_line(dataframe, *datatypes, labels=False, legend=True, ylabel=None, xlabel=None, title=None, xrotation='90', more_yticks=True):
    x_values = get_xvalues(dataframe)
    reverse = reverse_order(dataframe)

    fig = plt.figure()

    for datatype in datatypes:
        line_data = pd.to_numeric(reverse.loc[datatype])
        plt.plot(x_values,  line_data, label=datatype)
        if (labels):
            for x, y in zip(x_values, line_data):
                label = "{:.2f}".format(y)
                plt.annotate(label, (x, y), textcoords="offset points",
                             xytext=(0, 10), ha='center')

    if (ylabel != None):
        plt.ylabel(ylabel)
    if (xlabel != None):
        plt.xlabel(xlabel)
    if (title != None):
        fig.suptitle(title)
    if (legend):
        plt.legend()
    if (more_yticks):
        plt.locator_params(axis="y", nbins=(len(x_values) / 1.5))

    plt.xticks(rotation=xrotation)
    plt.show()


def chart_stackedarea(dataframe, *datatypes, legend=True, ylabel=None, xlabel=None, title=None, xrotation='90', more_yticks=True):
    x_values = get_xvalues(dataframe)
    reverse = reverse_order(dataframe)
    rev_data = datatypes[::-1]
    data = []

    for datatype in rev_data:
        data.append(pd.to_numeric(reverse.loc[datatype]))

    fig = plt.figure()

    plt.stackplot(x_values, data, alpha=0.4, labels=rev_data)

    if (ylabel != None):
        plt.ylabel(ylabel)
    if (xlabel != None):
        plt.xlabel(xlabel)
    if (title != None):
        fig.suptitle(title)
    if (legend):
        plt.legend(loc='upper left')
    if (more_yticks):
        plt.locator_params(axis="y", nbins=(len(x_values) / 1.5))

    plt.xticks(rotation=xrotation)
    plt.show()
