#Introduction to numpy
#numpy is library for numerical computing in python providing support for arrays and efficient operation
import numpy as np
import time
# creating 1 dimension array
arr_1d = np.array([1,2,3,4])
print("1d array: ",arr_1d)
print("type: ",type(arr_1d))
print("shape: " ,arr_1d.shape)

# creating 1 dimension array
arr_2d = np.array([[1,2,3],[4,5,6]])
print("2d array:\n",arr_2d)
print("shape: ",arr_2d.shape)

# accessing and modifying elements
print("element at [0]:",arr_1d[0])
arr_1d[0]=10
print("modified 1d array: ",arr_1d)

#performance comparison
large_list = list(range(1000000))
start = time.time()
sum_large = sum(large_list)
print("python list sum time: ",time.time()-start)

large_array = np.array(large_list)
start = time.time()
sum_large_np = np.sum(large_array)
print("numpy array sum time: ",time.time()-start)
#output:
# python list sum time:  0.018830060958862305
# numpy array sum time:  0.0029938220977783203

#-------- array operation and function -------
#   numpy supports element-wise operations and mathematical functions efficiently
#element-wise operations
arr1 = np.array([1,2])
arr2 = np.array([3,4])
print('addition: ',arr1+arr2)
print ('addition with np.add',np.add(arr1,arr2))

print("multiplication: ",arr1 * arr2)
print("matrix multiplication with np.multiply: ",np.multiply(arr1 , arr2))

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
print("matrix multiplication:\n",np.dot(arr1,arr2))
"""
top-left : 1*5+2*7=5+14=19
top-right : 1*6+2*8 = 6+16=22
bottom-left:3*5+4*7 =15+28=43
bottom-right:3*6+4*8=18+32=50
"""
# https://youtu.be/6-iJVFItnF8?t=189