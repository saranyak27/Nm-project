import pandas as pd

# Load the CSV file
df = pd.read_csv('/mnt/data/Housing.csv')

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Summary information
print("\nDataset Info:")
print(df.info())

# Basic statistics
print("\nStatistical Summary:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())
