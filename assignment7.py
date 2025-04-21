import pandas as pd
import matplotlib.pyplot as plt

## Task 1: Load and explore dataset
# File loading with error handling
try:
    dataset = pd.read_csv('path_to_your_dataset.csv')
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: The specified file was not found.")
except pd.errors.ParserError:
    print("Error: There was an issue parsing the file. Please check if the CSV is properly formatted.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# Show the first few rows to inspect the dataset
print(dataset.head())

# Inspecting the structure of the dataset
print(dataset.info())

# Checking for any missing values in the dataset
missing_data = dataset.isnull().sum()

if missing_data.any():
    print(f"Missing values found:\n{missing_data}")
else:
    print("No missing values detected.")

# Check and fix data types
try:
    dataset['numeric_column'] = dataset['numeric_column'].astype(float)
    print("Data type conversion successful!")
except ValueError:
    print("Error: Unable to convert column to the correct data type.")    

# Drop rows with any missing values
dataset.dropna(inplace=True)

# Displaying the first few rows after cleaning
print(dataset.head())


## Task 2: Basic Data analysis
# Compute summary statistics for numerical columns
print(dataset.describe())

# Group by the categorical column (e.g., 'species') and compute the mean of the numerical columns
grouped = dataset.groupby('species').mean()

# Show the result
print(grouped)

## Task 3: Data Visualization
# Bar chart for average petal length per species
plt.figure(figsize=(10, 6))
dataset.groupby('species')['petal_length'].mean().plot(kind='bar', color=['lightgreen', 'lightblue', 'lightcoral'])
plt.title('Average Petal Length per Species', fontsize=16)
plt.xlabel('Species', fontsize=14)
plt.ylabel('Average Petal Length', fontsize=14)
plt.xticks(rotation=0, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# Histogram for petal length distribution
plt.figure(figsize=(10, 6))
plt.hist(dataset['petal_length'], bins=25, color='skyblue', edgecolor='black')
plt.title('Distribution of Petal Length', fontsize=16)
plt.xlabel('Petal Length', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


# Scatter plot for sepal length vs petal length
plt.figure(figsize=(10, 6))
scatter = plt.scatter(dataset['sepal_length'], dataset['petal_length'], c=pd.Categorical(dataset['species']).codes, cmap='viridis', s=100)
plt.title('Sepal Length vs Petal Length', fontsize=16)
plt.xlabel('Sepal Length', fontsize=14)
plt.ylabel('Petal Length', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.colorbar(scatter, label='Species')
plt.grid(True, linestyle='--', alpha=0.7)  
plt.show()





