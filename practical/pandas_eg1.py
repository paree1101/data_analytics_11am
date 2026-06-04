import pandas as pd

data = {
    'Name':       ['Aarav','Priya','Rohan','Sneha','Vikram','Ananya','Karan','Meera',
                   'Arjun','Divya','Rahul','Kavya','Nikhil','Pooja','Siddharth',
                   'Ishaan','Riya','Aditya','Tara','Yash'],
    'City':       ['Mumbai','Delhi','Bangalore','Mumbai','Delhi','Chennai','Bangalore',
                   'Mumbai','Delhi','Chennai','Bangalore','Chennai','Mumbai','Delhi',
                   'Bangalore','Chennai','Mumbai','Delhi','Bangalore','Chennai'],
    'Dept':       ['Sales','Marketing','Tech','Tech','Sales','Marketing','Sales',
                   'Marketing','Tech','Sales','Marketing','Tech','Sales','Marketing',
                   'Tech','Marketing','Tech','Sales','Marketing','Sales'],
    'Age':        [28,32,26,30,35,27,31,29,24,33,36,25,38,28,34,29,27,40,31,23],
    'Sales':      [85,72,48,95,110,63,78,55,42,98,67,51,120,58,76,70,88,105,62,45],
    'Experience': [4,7,2,6,10,3,6,4,1,8,11,2,13,4,9,5,3,15,6,1],
    'Rating':     [4.2,3.8,4.5,4.7,4.1,3.9,4.0,4.3,4.6,4.4,3.7,4.8,4.0,3.6,4.2,
                   4.1,4.9,4.3,3.8,3.5],
}
df = pd.DataFrame(data)
print(df)

# groupby
print("\n--- groupby City ---")   # \n is used to add a new line before the output for better readability.
print(df.groupby('City')['Sales'].mean(numeric_only=True))

# filtering
print("\n--- Sales > 80 ---")
print(df[df['Sales'] > 80])

# pivot table
print("\n--- pivot table ---")
print(pd.pivot_table(df, values='Sales', index='City', columns='Dept', aggfunc='mean'))

# handling missing data
print("\n--- handling missing data ---")
df_with_nan = df.copy()
df_with_nan.loc[2, 'Sales'] = None  # Introduce a NaN value # NaN stands for "Not a Number" and is used to represent missing or undefined values in a DataFrame. In this case, we are setting the 'Sales' value for the row with index 2 to None, which will be treated as NaN in the DataFrame.
print(df_with_nan)
print("\n--- fill NaN with mean ---")
df_filled = df_with_nan.copy()
df_filled['Sales'] = df_filled['Sales'].fillna(df_filled['Sales'].mean()) # The fillna() function is used to replace NaN values in the 'Sales' column with the mean of the 'Sales' column. This is a common technique for handling missing data, as it allows us to retain the overall distribution of the data while filling in missing values with a reasonable estimate.
print(df_filled)

# merging dataframes
print("\n--- merging dataframes ---")
additional_data = {
    'Name': ['Aarav', 'Priya', 'Rohan', 'Sneha', 'Vikram'],
    'Bonus': [5000, 3000, 2000, 4000, 6000]
}
bonus_df = pd.DataFrame(additional_data)
merged_df = pd.merge(df, bonus_df, on='Name', how='left') # The merge() function is used to combine the original DataFrame (df) with the additional DataFrame (bonus_df) based on the 'Name' column. 
# The 'on' parameter specifies the column to merge on, and the 'how' parameter specifies the type of merge (in this case, 'left' means we want to keep all rows from the original DataFrame and add matching rows from the bonus DataFrame).
print(merged_df)
# NaN values in the 'Bonus' column indicate that there was no matching entry for those names in the bonus DataFrame, which is expected since we only provided bonus information for a subset of the names.

