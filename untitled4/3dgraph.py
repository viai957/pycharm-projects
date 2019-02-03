from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [5, 6, 7, 8, 9, 0, 3, 65, 7, 89]
z = [2, 3, 4, 5, 56, 77, 8, 78, 89]

ax.scatter(X, Y, Z , c="r", marker="c")
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.set_zlabel("z aixs")

plt.show()