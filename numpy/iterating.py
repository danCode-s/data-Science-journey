import numpy as np

arr = np.array([1,2,3])
arr_2D = np.array([[2, 4, 7, 1], [1, 4, 7, 1]])
arr_3D = np.array([[[2, 6, 11, 2], [34, 5, 1, 7]], [[22, 5, 66, 1], [51, 32, 65, 2]]])

for i in arr:
    print(i)

#2D array
print("2D ARRAY")
for i in arr_2D:
    print(i)
    for j in i:
        print(j)

print("3D ARRAY")
for i in arr_3D:
    print(i)
    for j in i:
        print(j)
        for z in j:
            print(z)


#Using nditer

for x in np.nditer(arr_3D):
    print(x)


# different data types

for x in np.nditer(arr_3D, flags=['buffered'], op_dtypes=['S']):
    print(f"\n{x}")

#Iterate through every scalar element of the 2D array skipping 1 element:

for x in np.nditer(arr_2D[:, ::2]):
    print(x)


# Enumerated Iteration Using ndenumerate()
print("\n")
for idx, i in np.ndenumerate(arr_2D):
    print(idx, i)