def load_csv(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def clean_data(df):
    return df.dropna()

def get_column_stats(df, column_name):
    return {
        'mean': df[column_name].mean(),
        'median': df[column_name].median(),
        'mode': df[column_name].mode()[0],
        'std_dev': df[column_name].std()
    }