import pandas as pd
import matplotlib.pyplot as plt

def plot_histogram(data, column, bins=10):
    plt.figure(figsize=(10, 6))
    plt.hist(data[column], bins=bins, color='blue', alpha=0.7)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

def plot_scatter(data, x_column, y_column):
    plt.figure(figsize=(10, 6))
    plt.scatter(data[x_column], data[y_column], color='red', alpha=0.5)
    plt.title(f'Scatter Plot of {x_column} vs {y_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.grid()
    plt.show()

def plot_box(data, column):
    plt.figure(figsize=(10, 6))
    plt.boxplot(data[column], vert=False)
    plt.title(f'Box Plot of {column}')
    plt.xlabel(column)
    plt.show()