import pandas as pd
import numpy as np

def read_csv(file_path):
    return pd.read_csv(file_path)

def calculate_statistics(data):
    numeric_data = data.select_dtypes(include=[np.number])
    mean = numeric_data.mean()
    median = numeric_data.median()
    mode = numeric_data.mode().iloc[0]
    std_dev = numeric_data.std()
    return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'std_dev': std_dev
    }

def main():
    file_path = './data/sample.csv'
    data = read_csv(file_path)
    statistics = calculate_statistics(data)
    print("Statistics:", statistics)

if __name__ == "__main__":
    main()