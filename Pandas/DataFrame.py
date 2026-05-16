# DataFrame Basics
# A Pandas DataFrame is a two-dimensional, size-mutable, tabular data structure with labeled axes (rows and columns). Think of it as a spreadsheet in Python, but with superpowers for data analysis.
import pandas as pd
import numpy as np


print ("\n----------------- 1. Core Parts of DataFrame-----------------")
# DataFrame Attributes
data = {
    "Cust ID": [101, 102, 103, 104, 104],
    "Name": ["Alice", "Bob", "Charlie", "David", "David"],
    "Age": [25, np.nan, 30, -5, -5],
    "City": ["London", "Paris", "London", "Berlin", "Berlin"],
    "Sales": ["100", "200", None, "300", "300"],
    "Order Date": ["2023-01-01", "2023-02-01", "2023-03-01", "wrong_date", "wrong_date"]
}
df=pd.DataFrame(data)
print(df)

'''

print("DataFrame Values:\n", df.values)  # Numpy array of data 
print("DataFrame Index:\n", df.index)    # Row labels 
print("DataFrame Columns:\n", df.columns)  # Column labels as Index object

print ("\n----------------- See the structure of the data-----------------")
print("DataFrame Shape:", df.shape)          # (rows, columns)
print("DataFrame Size:", df.size)            # Total number of elements
print("DataFrame Data Types:\n", df.dtypes)  # Data types of each column
print("DataFrame Memory Usage:\n", df.memory_usage())  # Memory usage of each column
print("DataFrame Info:",df.info())           # Summary of DataFrame including data types and memory usage



print ("\n----------------- 2. DataFrame categorized -----------------")
print ("\t------ 2.1 Simple DataFrame--------")
simple_df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 92, 78]
})
print("Simple DataFrame:")
print(simple_df)
print()

print ("\t------ 2.2 Hierarchical/MultiIndex--------")
df_medium = pd.DataFrame({
    "Revenue": [500, 550, 400, 420, 300, 320],
    "Costs": [300, 330, 250, 260, 200, 210],
    "Department": ["Sales", "Sales", "IT", "IT", "HR", "HR"],
    "Year": [2023, 2024, 2023, 2024, 2023, 2024]
})

# Creating MultiIndex from 'Department' and 'Year'
df_mi=df_medium.set_index(['Department', 'Year'], inplace=False)
print("DataFrame with MultiIndex:\n", df_mi)


arrays_list = [
    ['Sales', 'Sales', 'Marketing', 'Marketing'],
    ['Q1', 'Q2', 'Q1', 'Q2']
]
index = pd.MultiIndex.from_arrays(arrays_list, names=['Dept', 'Quarter'])
hierarchical_df = pd.DataFrame({
    'Revenue': [100000, 120000, 80000, 90000],
    'Costs': [60000, 70000, 50000, 55000]
}, index=index)
print("Hierarchical DataFrame:")
print(hierarchical_df)
print()

print ("\t------ 2.3 CATEGORICAL DATAFRAME--------")
# Columns Size and Color are categorical.this saves memory and speeds up operations
categorical_df = pd.DataFrame({
    'Size': pd.Categorical(['S', 'M', 'L', 'M', 'S', 'L', 'M']), # Categorical data type
    'Color': pd.Categorical(['Red', 'Blue', 'Red', 'Blue', 'Red', 'Blue', 'Red']), # Categorical data type
    'Quantity': [10, 15, 8, 12, 20, 5, 18] # Regular integer type
})

print(categorical_df)

print("Categorical DataFrame (memory efficient):")
print(categorical_df.dtypes)
print()
print ("\t------ 2.4 TIME SERIES DATAFRAME--------")

dates = pd.date_range('2024-01-01', periods=5, freq='D')
timeseries_df = pd.DataFrame({
    'Temperature': [22.5, 23.1, 24.0, 23.5, 22.8],
    'Humidity': [65, 68, 70, 67, 66]
}, index=dates)
print("Time Series DataFrame:")
print(timeseries_df)
print()

dates = ['2024-01-01', '2024-01-02', '2024-01-10']
times = pd.to_datetime(dates)



print ("\t------ 2.5 SPARSE DATAFRAME (many NaN values)--------")

sparse_df = pd.DataFrame({
    'A': [1, np.nan, np.nan, np.nan, 5],
    'B': [np.nan, 2, np.nan, np.nan, np.nan],
    'C': [np.nan, np.nan, 3, np.nan, np.nan]
})
print("Sparse DataFrame (before optimization):")
print(sparse_df)

# Convert to sparse for memory savings
# pd.SparseDtype("float", np.nan) means we are defining a sparse data type where the underlying data type is float and the missing values are represented by NaN.

sparse_df_optimized = sparse_df.astype(pd.SparseDtype("float", np.nan)) 
print(f"\nMemory saved: {sparse_df.memory_usage().sum()} → "
      f"{sparse_df_optimized.memory_usage().sum()} bytes")

      


print ("\n----------------- 3. Creating a DataFrames  -----------------")
# DataFrames can be created using differenet structure and use case:

print ("\t------ 3.1 Using dictionary with diffrent data types -int, float , str, Boolean----")
# Each key-value pair in the dictionary represents a column in the DataFrame.
# Pandas automatically infers the data type for each column based on the values provided.

list_data = ['Alice', 'Bob', 'Charlie', 'Diana']
list_Age = [28, 35, 42, 31]
list_City = ['NYC', 'LA', 'Chicago', 'Boston']
list_Salary = [65000, 85000, 95000, 70000]

# Correct DataFrame: each list becomes a column
name1 = pd.DataFrame({
    "Name_of_EMP": list_data,
    "Age_of_EMP": list_Age,
    "Name_of_City": list_City,
    "Salary_of_EMP": list_Salary
})
print("DataFrame with column names:\n")
print(name1)


data = {
    "Employee_ID": [101, 102, 103],          # int
    "Salary": [50000.5, 60000.75, 55000.0],  # float
    "Name": ["Abhay", "Bony", "Carry"],      # string
    "Is_Active": [True, False, True]         # boolean
}
df = pd.DataFrame(data)  # Each column becomes a Series, Pandas automatically detects data types
print(df)

# Dataframe created using Dictionary of Series
df_series = pd.DataFrame({
    'Name': pd.Series(['Alice', 'Bob', 'Charlie', 'Diana']),
    'City': pd.Series(['NYC', 'LA', 'Chicago', 'Boston'])
})

print(df_series)

print ("\t------ 3.2 From a list of dictionaries----")


# Each dictionary represents one row in df 
employees = [
    {'Name': 'Alice', 'Age': 28, 'Salary': 65000},
    {'Name': 'Bob', 'Age': 35, 'Salary': 85000},
    {'Name': 'Charlie', 'Age': 42, 'Salary': 95000}
]
df = pd.DataFrame(employees)
print(df)

# Pnadas handles missing keys automatically
mixed_data = [
    {'Name': 'Alice', 'Age': 28},
    {'Name': 'Bob', 'Salary': 85000},  # Missing Age
    {'Age': 42, 'Salary': 95000}  # Missing Name
]
df_mixed = pd.DataFrame(mixed_data)
print("\n With missing values:")
print(df_mixed)

print ("\t------ 3.3 From CSV / Excel / SQL----")
#df = pd.read_csv('/Applications/Manisha/data_frame_excel.cvs')
#print(df)
# df = pd.read_excel('/Applications/Manisha/data_frame_excel.xlsx')
# print(df)


print ("\t------ 3.4 From NumPy array----")

data = np.array([
    [11, 222, 343],
    [445, 565, 678],
    [756, 867, 967]
])
df = pd.DataFrame(
    data,
    columns=['A', 'B', 'C'],
    index=['Row1', 'Row2', 'Row3'],
    dtype="float"
)
print(df)
print ("\n----------------- 4 DataFrame Columns -----------------")

print ("\t------ 1. Selecting Data from Columns ----")

# Select a single column
df.Name            # Returns a Series
df['Name']          # Returns a Series
print("Select 'Name' column:\n", df['Name'], type(df['Name']))  # Series

df[['Name']]        # Returns a DataFrame
print("Select 'Name' column:\n", df[['Name']] , type(df[['Name']]))  # Series

# Select multiple columns as DataFrame
print("\n Select multiple columns :\n", df[['Name', 'Age']])

print ("\t------ 2. .loc (label-based) columns selection ----\n")
# Select a single column
print(df.loc[:, 'Name'])
# Select multiple columns
print(df.loc[:, ['Name', 'Age',"Order Date"]])

print ("\t------ 3. .iloc (position-based) columns selection ----\n")
print(df.iloc[:,[0]] ) # First column as DataFrame
print(df.iloc[:,[0]].values) # First column as Numpy array
print(df.iloc[:, [0,1,2,5]]) # All rows, specific columns by position (0,1,2,5)
print(df.iloc[:, 0:4]) ## All rows, first 4 columns (0,1,2,3)
print(df.iloc[:, 2:5]) # All rows, columns from position 2 to 4 (2,3,4)

print ("\t------ 4. Mixed Access  (rows + columns) ----")

print(df.iloc[0:2, 2:5]) # First 2 rows, columns from position 2 to 4 (2,3,4)
print("\n\n")
print(df.iloc[[0,1,2], [0,2,5]]) # Specific rows (0,1,2) and specific columns (0,2,5)
'''
print ("\t------ 5. Get Data from column  ----")
print(df['Name'][0])
print(df.loc[0,'Name'])
print(df.iloc[0,1])
print(df.iloc[0:3,[1,3]]) # First 3 rows, columns at position 1 and 3 (Name and City)

print ("\t------ 6. Operations on column  ----")
# we can perform many operations on columns like renaming, selecting based on conditions, etc.
print (df.dtypes)  # Data types of each column
print (df.describe()) # Statistical summary of numeric columns
print (df["Name"].unique()) # Unique values in the 'Name' column
print(df["Sales"].isnull()) # Check for missing values in 'Sales' column
df["Sales"]=df["Sales"].fillna(0) # Fill missing values in 'Sales' column with 0
df["Sales"] = pd.to_numeric(df["Sales"], errors='coerce') # Convert 'Sales' column to numeric, coercing errors to NaN
print ("Total sales=",df["Sales"].sum()) 
print ("Standard deviation of sales=",df["Sales"].std()) 


# Rename all columns
df.columns= ['Customer ID', 'Employee Name', 'Employee Age', 'Employee City', 'Total Sales', 'Order Date']
print(df.columns)
# Rename one columns
df= df.rename(columns={'Order Date':'Order Date New'})
print(df)

#Convert column names to lowercase
df.columns = df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_') # Replace spaces with underscores
print(df.columns)

# Add a new column
df["bonus"] = [200, 300, 400, 250, 500]
#Filter rows using a column
print("Filter rows where 'employee_age' is greater than 30\n",df[df["employee_age"] >= 25]) 


df['order_date_new'] = df['order_date_new'].str.replace('wrong_date', '2023-01-01') # Replace wrong date with a valid date
print("\n\n",df,"\n\n")


df.columns = df.columns.str.lower().str.replace(' ', '_') #Rename then access with new names
print("\n",df.columns,"\n")

print(df.loc[:, df.columns.str.startswith('e')]) # Select columns that start with 'A' (e.g., 'Age')
print("All rows sorted by total sales (descending):\n", df.sort_values("total_sales", ascending=False)) 
print("Change datatypes:\n", df["total_sales"].astype(float))

print("Dropped employee_city column\n",df.drop(columns=["employee_city"]) ) # Drop the 'employee_city' column and return a new DataFrame without it. The original df remains unchanged unless you use inplace=True

'''

# Select rows by index
df.iloc[0]          # First row
df.iloc[0:3]        # First 3 rows
df.iloc[:, 0:2]     # All rows, first 2 columns
# Select by label
df.loc[0, 'Name']   # Specific cell
df.loc[0:2, 'Name':'Age']  # Range of rows and columns
# Filtering Data



# Simple filtering
df[df['Age'] > 30]                    # People older than 30
df[df['City'] == 'New York']          # People from New York
# Multiple conditions
df[(df['City'] == 'Tokyo') | (df['Age'] < 30)]  # OR
# Using isin() for multiple values
df[df['City'].isin(['Tokyo', 'Paris'])]
# Adding and Modifying Data


# Add a new column
#df['Full_Info'] = df['Name'] + ', ' + df['City']
# Modify existing column
df['Age'] = df['Age'] + 1
# Add new row
#new_row = {'Name': 'Eve', 'Age': 32, 'City': 'Berlin', 'Salary': 65000}
#df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
# Handling Missing Dat

# Check for missing values
df.isnull()         # Returns boolean DataFrame
df.isnull().sum()   # Count of missing values per column
# Drop missing values
df.dropna()         # Drop rows with any missing values
df.dropna(subset=['Name'])  # Drop rows where 'Name' is missing
# Fill missing values
df.fillna(0)        # Fill with 0
df.fillna(df.mean()) # Fill with mean (for numeric columns)
df['Age'].fillna(df['Age'].median())  # Fill specific column with median

#Grouping and Aggregation
# Group by a column
grouped = df.groupby('City')
# Aggregate functions
df.groupby('City')['Salary'].mean()    # Average salary by city
df.groupby('City')['Salary'].sum()     # Total salary by city
df.groupby('City').agg({
    'Salary': ['mean', 'max', 'min'],
    'Age': 'mean'
})
#Sorting



# Sort by one column
df.sort_values('Age')                  # Ascending
df.sort_values('Age', ascending=False) # Descending
# Sort by multiple columns
df.sort_values(['City', 'Age'])


print ("\n----------------- 5 DataFrame Rows -----------------")


print(df.index)

# get one row
print(df.loc[1])

# get multiple rows
print(df.iloc[1:4])

# get one value
print(df.loc[2, "name"])

# filter rows
print(df[df["age"] > 25])

# update one cell
df.loc[1, "salary"] = 4800

# update full row
df.loc[3] = ["Mina", 29, 4300]

# add new row
df.loc[5] = ["Emma", 27, 4700]

# delete one row
df = df.drop(0)

# delete multiple rows
df = df.drop([2, 4])

# reset index
df = df.reset_index(drop=True)

print(df)
print ("\n----------------- 6 DataFrame Index -----------------")
'''