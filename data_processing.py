import pandas as pd

def load_data(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    return df

def get_data_summary(df):
    # Return a summary of the data
    return df.describe()

# Example usage
if __name__ == "__main__":
    df = load_data("data.csv")
    summary = get_data_summary(df)
    print(summary)
