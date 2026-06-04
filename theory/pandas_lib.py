### Pandas Library in Python

# Pandas is a powerful and widely-used library in Python for data manipulation and analysis.
# It provides data structures like Series and DataFrame, which allow you to work with structured data efficiently. 
# With Pandas, you can easily handle missing data, perform data cleaning, and conduct various operations on your datasets.

# Key Features of Pandas:
# 1. Data Structures: Pandas provides two main data structures - Series (1D) and DataFrame (2D).
# 2. Data Manipulation: You can easily filter, sort, and group data using Pandas.
# 3. Handling Missing Data: Pandas has built-in functions to handle missing data, such as filling or dropping missing values.
# 4. Data Analysis: You can perform various operations like aggregation, merging, and reshaping data with Pandas.
# 5. Integration: Pandas integrates well with other libraries like NumPy, Matplotlib, and Scikit-learn, making it a versatile tool for data analysis and machine learning.  

# To use Pandas, you need to install it first using pip:
# pip install pandas
# Once installed, you can import it in your Python code as follows:
import pandas as pd

# Example: Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data) 
print(df)

# Example: Reading a CSV file into a DataFrame
# df = pd.read_csv('your_file.csv')
# print(df) 

# Example: Basic DataFrame Operations
# Filtering data
filtered_df = df[df['Age'] > 28]
print(filtered_df)

# Grouping data
grouped_df = df.groupby('City')['Age'].mean()
print(grouped_df)

# Handling missing data
# df['Age'] = df['Age'].fillna(df['Age'].mean())

### A larger dataframe is created in practical folder to demonstrate the use of pandas library.



