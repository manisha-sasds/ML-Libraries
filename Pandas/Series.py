
# Syntax of Pandas Series 
# pd.Series(data, index=None, dtype=None)
#pd.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)

# A Series can hold only ONE data type- int64,float64,object (string),bool
import pandas as pd
import numpy as np

print ("\n----------------- 1. Creating a Series with diffrent data types -int, float , str, Boolean -----------------")
# To create a Series, we can use the pd.Series() constructor and pass in the data or many types of objects (like list, dict,numpy array, tuple etc) along with optional parameters like index and dtype. 

# created series with integer data type and default index which start from 0
series1= pd.Series([11,22,3344], index=None, dtype=None)
print("Series with default index:",series1)

# created series with float data type and default index which start from 0
series2= pd.Series([11,22.88,22.34], index=None, dtype=float)
print("Series with default index:",series2)
print("Data type of series2 before conversion:",series2.dtype)  # float64
# Convert types series2 from float to int using astype() method 

series2_int = series2.astype('int64')
print(series2_int.dtype)  # int64
print("Data type of series2 after conversion:",series2_int.dtype)  # int64

series3= pd.Series([11,22,33,44], index=[101,120,133,144], dtype=None)
print("Series with default index:",series3)

print ("\n----------------- 1.1 Create an Empty Series -----------------")
# When we create an empty Series, it will have no elements and its data type will be 'float64' by default.
empty_series= pd.Series()
print("Empty Series:", empty_series)
# Always specify dtype explicitly for better practice
empty_series= pd.Series(dtype=int)
print("Empty Series:", empty_series,empty_series.dtype)

print ("\n----------------- 1.2 Create a Series from a List -----------------")

#list_data= [10,20,"Mango", "Apple",234.56]
list_data= [11,22,3344]
series_from_list= pd.Series(list_data)
print(f"Series from List:, {series_from_list} , Data type is: {series_from_list.dtype}")


print ("\n----------------- 1.3 Series with Custom Index -you can give any index value (which is label for data) -----------------")
s = pd.Series([10, 20, 30,56,"Mango",5464.877], index=['1.a', '2.b', '303',67,'fruit', 101.11])
print(s)

# Temperature readings for a week
temperatures = pd.Series([22.5, 24.1, 23.8, 25.2, 26.0, 24.5, 23.1],index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
           'Friday', 'Saturday', 'Sunday'],
    name='Temperature_Celsius'
)
print(temperatures)

print ("\n----------------- 1.4 Create Series from NumPy ndarray -----------------")

array_data= np.array([10,20,30,40,50])
print(array_data)
series_from_array= pd.Series(array_data)
print("Series from NumPy ndarray:", series_from_array)

print ("\n----------------- 1.5 Create Series from Dictionary -----------------")
# Dictionary keys → index, values → data
data_dict = {'a': 100, 'b': 200, 'c': 300,"name":"My Series"}
#s = pd.Series(data_dict, index=['a','b','c'])
s = pd.Series(data_dict, index=['b','a','c'])
s.index = ['x','y','z']
print(s)
print(type(s))
print(s.dtype)

print ("\n----------------- 1.6 Create Series from Scalar Value -----------------")
# All index values will have the same scalar value 
s = pd.Series(5, index=['a', 'b', 'c'])
print(s)

print ("\n----------------- 2 How To Accessing Data in Series -----------------")
# You can access data in a Pandas Series using index labels or integer positions. Here are some common methods to access data:
print ("\n----------------- 2.1 Accessing Data in Series By index label-----------------")
ser_data= pd.Series([10,20,30,40,50])
ser_data1= pd.Series([10,20,30,40,50], index=['a','b','c','d','e'])
ser_data3= pd.Series([10,20,30,40,50], index=[101,102,103,104,105])

print(ser_data)
print(ser_data1)
print(ser_data3)    
ser_data3.loc[102:104]

print("\nAccessing vlues:\n")

print(ser_data[0]) ## by default index position
print(ser_data1['b']) ## by index label
print(ser_data3[103]) ## by index label

print("\n Accessing vlues by slicing :\n")

print("ser_data[0:2:",ser_data[0:2]) ## by default index position
print("ser_data1['b':'e']",ser_data1['b':'e']) ## by index label
print("ser_data3[102:104]",ser_data3[102:104]) ## by index label # give empty result
print("ser_data3.iloc[1:3]",ser_data3.iloc[1:3]) ## by index label

#   - By position
#   - By boolean indexing

print ("\n----------------- 2.1 Access by Index Label-----------------")

ser_list=pd.Series(["Mango","Kivi","Strawberry","Banaba"],index=["Fruit1","Fruit2","Fruit3","Fruit4"])
print("list of series:\n",ser_list)
# print(ser_list[0])  # Accessing by default index position not recommended
print("Accessing list of series by index:",ser_list.loc["Fruit1"])  # Accessing by index label#


ser_dict=pd.Series({"name":"John","age":30,"city":"Pune"})
print("Dictionary of series:\n",ser_dict)
print("Access ser_dict['age']:",ser_dict.loc["age"])  # Accessing by index label#

df = pd.DataFrame({
    'Name': ['Alia','Boby','Carry','Dina','Ella'],
    'Age': [21,22,23,24,25],
    'Marks': [60,70,80,90,100]
}, index=['r1','r2','r3','r4','r5'])

print(df)

df_index_based=df.loc['r2']  # Accessing row by index label
print("Accessing row by index label df.loc['r2']:\n",df_index_based)

print ("\n----------------- 2.2 Access by Position-----------------")
#position starts at 0)
print ("Accessing ser_list by position 2:",ser_list.iloc[2])  # Accessing by position#
print ("Accessing ser_dict by position 1:",ser_dict.iloc[1])  #Accessing by position#
print("Accessing df by position 2:\n",df.iloc[2])

print ("\n----------------- 2.3 Access Multiple Values-----------------")
print ("Accessing ser_list by multiple index labels:",ser_list.loc[["Fruit2","Fruit4"]])  # Accessing by multiple index labels#
print ("Accessing ser_dict by multiple index labels:",ser_dict.loc[["name","city"]])  # Accessing by multiple index labels#
df_index_multi=df.loc[['r2','r5']] # Accessing row by index label
print("Accessing row by index label df.loc[['r2','r5']]:\n",df_index_multi)
df_index_multi_pos=df.iloc[[1,3]] # Accessing row by position
print("Accessing row by index label df.iloc[[1,3]]:\n",df_index_multi_pos)

print ("\n----------------- 2.4 Slicing-----------------")
print("Accessing ser_list by slicing:",ser_list.loc["Fruit2":"Fruit4"])  # Accessing by slicing
print("Accessing ser_dict by slicing:",ser_dict.iloc[0:2])  # Accessing by slicing

df_index_slice=df.loc['r2':'r4'] # Accessing row by index label
print("Accessing row by index label df.loc['r2':'r4']:\n",df_index_slice)

df_index_slice1=df.loc['r2':'r4','Name':'Age'] # Accessing row by index label
print("Accessing row by index label df.loc['r2':'r4','Name':'Age']:\n",df_index_slice1)
df_index_slice_pos1=df.iloc[1:4,0:1] # Accessing row by position
print("Accessing row by index label df.iloc[1:4]:\n",df_index_slice_pos1)  
print ("\n----------------- 3 Series Index -----------------")
# Index objects are immutable sequences, so you use normal Python indexing ([]) and slicing.
#In Series.index, we can only access by position like a list; .loc or .iloc do not work.
s = pd.Series([10, 20, 30,"moni",67,87], index=['a','b','c','d','e','f'])

# View index
print("Oringinal Index",s.index)          # Index(['a','b','c','d','e','f'], dtype='object')

# Access by position
print("Access by posistion",s.index[1])       # 'b'
print(s.index[1:4])

# Access by label - Not possible
print(s.values)      # [10 20 30 'moni' 67 87]
print(s.values[1])       # 20
#print(s.values['b'])     # TypeError: only integer scalar arrays can be converted to a scalar index , 'b' is a string label, not an integer.
print(s.values[1:4])
# print(s.index.loc[5])       # AttributeError: 'Index' object has no attribute 'loc'
# print(s.index.iloc[1:3])  # AttributeError: 'Index' object has no attribute 'iloc'
print ("\n----------------- 3.1 Change Series Index -----------------")

# If we want to Change index from index=['a','b','c','d','e','f'] to index=["xx","yy","zz","ww","vv","uu"]
s.index = ["xx","yy","zz","ww","vv","uu"] 
print(s)
 # Reset index to default means to [0,1,2,3,4,5]
s.index=range(len(s))
print(s)

# Duplicate index
s2 = pd.Series([1,2,3,4,5,6,7,8], index=['a','a','b','c',100,100,100,200])
print(s2.loc['a'])      # 0    1
                        # 1  
                        # 
print(s2.loc[100])    # or 
print(s2.iloc[4:7])  
print ("\n----------------- 3.2  Series Index  Operations -----------------")
# we can do various operations on Series index like view, checking index type,rename, length, membership testing, slicing, etc.
s = pd.Series([10, 20, 30,"moni",67,87], index=['x','y','z','w','v','u'])
print("Before index renames",s,"\n")

s.rename(index={'x': 'a', 'y': 'b'}, inplace=True)
print("After index renames",s,"\n")
print("type of index:",type(s.index),"\n") # Index type is 'Index' object
print("type of index:",type(s.values),"\n") # Values are stored in ndarray format
print("Length of index:",len(s.index),"\n") # Length of index
print("Check if 'a' in index:",'a' in s.index,"\n")
print("Slice index from position 1 to 3:",s.index[1:4],"\n")

print ("\n----------------- 3.3  Useful Series Index Methods -----------------")

# index sorting using sort_index() method
s = pd.Series(["apple", "banana", "cherry", "date", "elderberry", "fig"], index=['x','y','c','w','b','a'])
print("Sorted index:\n",s.sort_index(),"\n")
print("Sorted index in descending order:\n",s.sort_index(ascending=False),"\n")

# Convert index to list, numpy array, and ndarray
s = pd.Series([10, 20, 30,40], index=['a', 'b', 'c','a'])
print(s.index)
print("type of index:",type(s.index),"\n")

# Convert index to list

print(s.index.tolist()) # It does. ot change original index to list for that we need to save in  new varaible 
print("type of index is l;ist :",type(s.index),"\n") # 
list_idx= s.index.tolist()  # convert index to list and save in new variable
print("type of list_idx is l;ist :",type(list_idx),"\n")

print("is duplicate avaialbe in index:", s.index.has_duplicates) # yes 
min_index= s.index.min()
max_index= s.index.max()
print("\n is min  of index:", min_index) # a
print("\n is max  of index:", max_index) # c
print("\n Check for multiple values of index:", s.index.isin(['a', 'c'])) 
print("Before coverting to numpy araray:",type(s.index))
s_numpy=s.index.to_numpy()
print("Converetd index to numpy arary:",s_numpy)
print("After coverting to numpy araray:",type(s_numpy)) # class 'numpy.ndarray

print ("\n----------------- 4 Mathematical Operations on Series-----------------")
print ("\t------ 4.1 Basic Mathematical Operations on Series +, -,/ ----")

s = pd.Series([10, 20, 30,40], index=['a', 'b', 'c','a'])
print("Original Series:\n",s)   
# Addition
s_add = s + 500
print("After Addition:\n",s_add)
# Subtraction
s_sub = s - 200
print("After Subtraction:\n",s_sub) 
# Multiplication
s_mul = s * 1000
print("After Multiplication:\n",s_mul)

print ("\t------ 4.2 Operations between two Series (index-aligned) ----")

s1 = pd.Series([10,20 , 30], index=['a','b', 'c'])
s2 = pd.Series([1, 2, 3,4], index=['a', 'b', 'c','d'])
print("Series 1:\n",s1)   
print("Series 2:\n",s2)     
# Addition  
s_add = s1 + s2
print("After Addition of two series:\n",s_add)
# Subtraction
s_sub = s1 - s2
print("After Subtraction of two series:\n",s_sub)
print ("\t------ 4.3 Using mathematical methods add(),sub() etc  ----")
# Adding 1000 to each element of the sereies using add() method
s_add_method = s1.add(1000)
print("After Addition using add() method:\n",s_add_method)
print ("\t------ 4.4 Using mathematical Aggregation functions sum(), mean() etc  ----")
# Sum of all elements in the series using sum() method
s_sum = s1.sum()
print("Sum of all elements using sum() method:",s_sum)
# Mean of all elements in the series using mean() method
s_mean = s1.mean()
print("Mean of all elements using mean() method:",s_mean)
# Standard Deviation of all elements in the series using std() method
s_std = s1.std()
print("Standard Deviation of all elements using std() method:",s_std)
# power of all elements in the series using pow() method
s_pow = s1.pow(2)
print("Power of all elements using pow() method:\n",s_pow)

s_cumsum = s1.cumsum()
print("Cumulative Sum of all elements using cumsum() method:\n",s_cumsum)

print ("\n----------------- 5 Comparison & Boolean Operations -----------------")
s = pd.Series([10, 20, 30,40], index=['a', 'b', 'c','a'])
print("Original Series:\n",s)   
# Comparison
s_gt = s > 25
print("Greater than 25:\n",s_gt)
print ("\n----------------- 6  Useful Built-in Series Functions like head(),tail(),unique() etc-----------------")

sal = pd.Series(
    [50000, 60000, 55000, np.nan, 60000, 70000, 50000],
    index=['Abhay', 'Bony', 'Carry', 'Dingo', 'Ella', 'Fisa', 'Goldie'])

# View data
print("Salary Series Data:\n", sal.head(4))  # First 4 entries
print("Salary Series Data:\n", sal.tail(3))  # Last 3 entries
# Summary statistics
print("Summary Statistics of Salary Series:\n", sal.describe())
# Unique values 
print("Unique Salary Values:\n", sal.unique())
# Value counts
print("Salary Value Counts:\n", sal.value_counts())
# Check for null values
print("Check for null values:\n", sal.isnull().sum())

print("Size of Salary Series:", sal.size)
print("Shape of Salary Series:", sal.shape) # (number of elements,)
print("Data type of Salary Series:", sal.dtype)
print("Memory usage of Salary Series:", sal.memory_usage())

# Increase salary by 10%
sal_increased = sal.apply(lambda x: x * 1.1)
print("Salary after 10% increase:\n", sal_increased)

# Categorize salary
sal_category = sal.map({
    50000: 'Low',
    55000: 'Medium',
    60000: 'Medium',
    70000: 'High'
})
print(sal_category)

print ("\n----------------- 7  Handling Missing Values (NaN)-----------------")
# Handling missing values
print("Original Salary Series with NaN:\n", sal)
# Fill NaN with a specific value

sal_filled = sal.fillna(sal.mean())
print("Salary Series after filling NaN with 58000:\n", sal_filled)

print ("\n----------------- 8  Converting Series-----------------")
# Convert Series to different formats
sal.to_list()       # Convert to Python list
print("Salary Series to list:", sal.to_list())
sal.to_numpy()      # Convert to NumPy array
print("Salary Series to numpy array:", sal.to_numpy())
sal.to_dict()       # Convert to Python dictionary
print("Salary Series to dictionary:", sal.to_dict())