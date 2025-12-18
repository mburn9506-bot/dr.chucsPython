# https://youtu.be/XX44XYjK_JQ?t=12022
#importing numpy
import numpy as np
import time

arr_3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(" array:\n",arr_3d)
print("shape: ",arr_3d.shape)
"""output:
 array:
 [[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
shape:  (2, 2, 3)
"""
print("2d slice at [0]:\n",arr_3d[0])
arr_3d[0,0,0]=20
print("modified 3d array:\n",arr_3d)
"""output:
 [[[20  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
  """
large_3d = np.full((100,100,100),100)
start = time.time()
sum_np=np.sum(large_3d)
print("numpy sum time: ",time.time()-start)
#output:numpy sum time:  0.0006000995635986328
start = time.time()
sum_loop = 0
for i in range(100):
        for j in range(100):
                for k in range(100):
                        sum_loop += large_3d[i,j,k]
print("python loop sum time",time.time()- start)
"""output:
numpy sum time:  0.0011668205261230469
python loop sum time 1.520794153213501
"""
"""large_3d = np.array((100,100,100))
This creates a 1-D array, not a 3-D one:

this create a 3d array:
large_3d = np.ones((100, 100, 100))
or
large_3d = np.zeros((100, 100, 100))
or
large_3d = np.full((100, 100, 100),100)


"""
