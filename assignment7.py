import pandas as pd

## Task 1: Load and explore dataset

# Load dataset from CSV
dataset = pd.read_csv()

# Show the first few rows to inspect the dataset
print(dataset.head())

# Inspecting the structure of the dataset
print(dataset.info())

# Checking for any missing values in the dataset
print(dataset.isnull().sum())

# Drop rows with missing values
dataset_cleaned = dataset.dropna()

# Displaying the first few rows after cleaning
print(dataset_cleaned.head())


## Task 2: Basic Data analysis
# Compute summary statistics for numerical columns
print(dataset.describe())

# Group by the categorical column (e.g., 'species') and compute the mean of the numerical columns
grouped = dataset.groupby('species').mean()

# Show the result
print(grouped)

## Task 3: Data Visualization

