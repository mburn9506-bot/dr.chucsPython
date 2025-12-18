import numpy as np
import time

large_3d = np.ones((100, 100, 100))

start = time.time()
sum_np = np.sum(large_3d)
print("numpy sum time:", time.time() - start)

start = time.time()
sum_loop = 0
for i in range(100):
    for j in range(100):
        for k in range(100):
            sum_loop += large_3d[i, j, k]
print("python loop sum time:", time.time() - start)
"""output:
numpy sum time: 0.0017559528350830078
python loop sum time: 1.6399848461151123
"""

