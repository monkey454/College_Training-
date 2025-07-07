# NumPy - Numerical Python
# NumPy is a powerful library for numerical computing in Python, providing support for arrays, matrices,
# and a wide range of mathematical functions.
# NumPy is widely used in data science, machine learning, and scientific computing.


# How NumPy is used in Python:
# 1. Importing NumPy:
import numpy as np  

# 2. Creating NumPy arrays:
array_1d = np.array([1, 2, 3, 4, 5])  # 1D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # 3D array

# 3. Array attributes:
print("1D Array Shape:", array_1d.shape)  # Shape of the array
print("2D Array Dimensions:", array_2d.ndim)  # Number of dimensions
print("3D Array Size:", array_3d.size)  # Total number of elements

# [start, stop, step] slicing
print("1D Array Slicing:", array_1d[1:4])  # Slicing a 1D array
print("2D Array Slicing:", array_2d[0:2, 1:3])  # Slicing a 2D array

# array indexing
print("1D Array Indexing:", array_1d[2])  # Accessing an element in a 1D array
print("2D Array Indexing:", array_2d[1, 2])  # Accessing an element in a 2D array
print("3D Array Indexing:", array_3d[-1, 0, 1])  # Accessing an element in a 3D array

# 4. Array operations:
# Arithmetic operations
array_sum = array_1d + 5  # Adding 5 to each element
array_product = array_2d * 2  # Multiplying each element by 2   

print("Array Sum:", array_sum)
print("Array Product:", array_product)


# Data types in NumPy:
# 1. Integer data type
import numpy as np
int_array = np.array([1, 2, 3], dtype=np.int32)
print("Integer Array:", int_array)

# 2. Float data type
float_array = np.array([1.0, 2.0, 3.0], dtype=np.float64)
print("Float Array:", float_array)

# 3. Complex data type
complex_array = np.array([1+2j, 3+4j], dtype=np.complex128)
print("Complex Array:", complex_array)

# 4. Boolean data type
bool_array = np.array([True, False, True], dtype=np.bool_)
print("Boolean Array:", bool_array) 

# 5. String data type
string_array = np.array(['Hello', 'World'], dtype=np.str_)
print("String Array:", string_array)    

# 6. Object data type
object_array = np.array([{'key': 'value'}, [1, 2, 3]], dtype=object)
print("Object Array:", object_array)

# 7. Structured data type
structured_array = np.array([(1, 'Alice'), (2, 'Bob')], dtype=[('id', 'i4'), ('name', 'U10')])
print("Structured Array:", structured_array)

# 8. Record data type
record_array = np.array([(1, 'Alice'), (2, 'Bob')], dtype=[('id', 'i4'), ('name', 'U10')])
print("Record Array:", record_array)

# 9. Mixed data type
mixed_array = np.array([1, 'Hello', 3.14], dtype=object)
print("Mixed Array:", mixed_array)  


arr1 = np.array([1, 2, 3, 4])
arr2 = np.array(['apple', 'banana', 'cherry'])
print(arr1.dtype)
print(arr2.dtype)

arr = arr1.copy()
arr1[0] = 10  # Modifying the original array
print("Original array:", arr1)
print("Copied array:", arr)

new_arr = np.array_split(arr1, 2)  # Splitting the array into sub-arrays
print("Split array:", new_arr)

# 5. Array reshaping:
reshaped_arr = arr1.reshape(2, 2)  # Reshaping the array to 2x2
print("Reshaped array:\n", reshaped_arr)

# sorting the array
sorted_arr = np.sort(arr1)  # Sorting the array
print("Sorted array:", sorted_arr)

# NumPy arithemetic operations:
arr3 = np.array([5, 6, 7, 8])
arr_sum = arr1 + arr3  # Element-wise addition
arr_diff = arr1 - arr3  # Element-wise subtraction
arr_prod = arr1 * arr3  # Element-wise multiplication
arr_div = arr1 / arr3  # Element-wise division
print("Array Sum:", arr_sum)
print("Array Difference:", arr_diff)
print("Array Product:", arr_prod)
print("Array Division:", arr_div)

# NumPy mathematical functions:
arr4 = np.array([1, 2, 3, 4])
arr_sqrt = np.sqrt(arr4)  # Square root of each element
arr_exp = np.exp(arr4)  # Exponential of each element
arr_log = np.log(arr4)  # Natural logarithm of each element
arr_min = np.min(arr4)  # Minimum value in the array
arr_max = np.max(arr4)  # Maximum value in the array
print("Minimum Value:", arr_min)
print("Maximum Value:", arr_max)
print("Square Root:", arr_sqrt)
print("Exponential:", arr_exp)
print("Natural Logarithm:", arr_log)


import numpy as np
usage_kwh = np.array([100, 150, 200, 250, 300])
bills = np.zeros_like(usage_kwh, dtype=float)  # Initialize bills array with zeros
for i in range(len(usage_kwh)):
    if usage_kwh[i] <= 150:
        bills[i] = usage_kwh[i] * 0.12  # $0.12 per kWh for first 150 kWh
    else:
        bills[i] = (150 * 0.12) + ((usage_kwh[i] - 150) * 0.15)  # $0.15 per kWh for usage above 150 kWh

print("Electricity Usage (kWh):", usage_kwh)
print("Electricity Bills ($):", bills)

max_usage = np.max(usage_kwh)
max_users = np.where(usage_kwh == max_usage)[0]  # Find indices of maximum usage
print("Maximum Usage (kWh):", max_usage)
print("Users with Maximum Usage (Indices):", max_users)

average_bill = np.mean(bills)
print("Average Electricity Bill ($):", average_bill)