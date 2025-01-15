import numpy as np

a = np.array([[0,1],[2,3],[4,5]])
b = np.array([[0,1,2,3],[4,5,6,7]])

result = np.dot(a,b)
print(result)

max_element = np.max(result)
print(max_element)