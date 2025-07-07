# Pandas - library for data manipulation and analysis
# Pandas is a powerful library for data manipulation and analysis in Python, providing data structures like
# Series and DataFrame, which are essential for handling structured data.   

# Application of Pandas in Python:
# data analysis, data cleaning, data transformation, time series analysis and data visualization.

# stock market technical analysis:
import pandas as pd
import numpy as np
data = {
    "Name" : ['Steve', 'John', 'Alice', 'Bob'],
    "Age" : [25, 30, 22, 35],
    "Gender" : ['Male', 'Male', 'Female', 'Male'],
    "Rating" : [4.5, 3.8, 4.2, 4.0]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
# Accessing columns
print("\nAccessing 'Name' column:")
print(df['Name'])
# Accessing multiple columns
print("\nAccessing 'Name' and 'Age' columns:")
print(df[['Name', 'Age']])
# Accessing rows by index
print("\nAccessing row with index 2:")
print(df.iloc[2])
# Accessing rows by condition
print("\nAccessing rows where Age is greater than 25:")
print(df[df['Age'] > 25])
# Adding a new column
df['Salary'] = [50000, 60000, 55000, 70000]
print("\nDataFrame after adding 'Salary' column:")
print(df)
# Renaming a column
df.rename(columns={'Rating': 'Performance'}, inplace=True)
print("\nDataFrame after renaming 'Rating' to 'Performance':")
print(df)
# Dropping a column
df.drop(columns=['Salary'], inplace=True)
print("\nDataFrame after dropping 'Salary' column:")
print(df)

# Series example
s = pd.Series([1, 2, 3, 4, 5],
              index=['a', 'b', 'c', 'd', 'e'],
              name='Numbers')
print("\nSeries:")
print(s)
# Accessing elements in Series
print("\nAccessing element with index 'c':")
print(s['c'])
# Slicing Series
print("\nSlicing Series from index 'b' to 'd':")
print(s['b':'d'])
# Applying a function to Series
squared = s.apply(lambda x: x ** 2)
print("\nSeries after applying square function:")
print(squared)
# list of Series
series_list = [pd.Series([1, 2, 3]), pd.Series([4, 5, 6]), pd.Series([7, 8, 9])]
df_from_series = pd.DataFrame(series_list, columns=['A', 'B', 'C'])
print("\nDataFrame from list of Series:")
print(df_from_series)

# Indexing in Pandas
# Creating a DataFrame with custom index
df_custom_index = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
print("\nDataFrame with custom index:") 
print(df_custom_index)

# Line indexing
print("\nAccessing row with index 'c':")
print(df_custom_index.loc['c'])


# integer positional indexing
print("\nAccessing row with integer index 2:")
print(df_custom_index.iloc[2])

# Conditional indexing
print("\nAccessing rows where Age is less than 30:")    
print(df_custom_index[df_custom_index['Age'] < 30])

# random generation of DataFrame
random_df = pd.DataFrame({
    'A': pd.Series(np.random.randn(5)),
    'B': pd.Series(np.random.randn(5)),
    'C': pd.Series(np.random.randn(5))
})
print("\nRandomly generated DataFrame:")
print(random_df)

df1 = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])
df2 = pd.DataFrame(np.random.randn(5, 3), columns=['D', 'E', 'F'])
print("\nDataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)


df = pd.DataFrame({
    "A" : [1, 2,3],
    "B" : [4, 5, 6],
    "C" : [7, 8, 9]
})
print("\nOriginal DataFrame:")
print(df)
# Replace the contents of column 'A' with new values
df["A"] = [10, 20, 30]
print("\nDataFrame after replacing column 'A':")
print(df)
# Replace the contents
df.replace({"A" : {1: 100} , "B" : {4: 400}, "C" : {7: 700}}, inplace=True)
print("\nDataFrame after replacing values:")    
print(df)
df.replace({"A" : {10: 100} , "B" : {6: 600}, "C" : {8: 800}}, inplace=True)
print("\nDataFrame after replacing values again:")
print(df)
df.drop(columns=["B"], inplace=True)
print("\nDataFrame after dropping column 'B':")
print(df)
result = df.apply(lambda x: x + 1)
print("\nDataFrame after applying function to add 1 to each element:")
print(result)

# String.io example
import io
data = """Name,Age,Gender,Rating
Steve,25,Male,4.5
John,30,Male,3.8
Alice,22,Female,4.2
Bob,35,Male,4.0
"""
df_from_csv = pd.read_csv(io.StringIO(data))
print("\nDataFrame from CSV string:")
print(df_from_csv)
