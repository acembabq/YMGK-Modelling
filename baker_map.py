import numpy as np
import matplotlib.pyplot as plt

def baker_map_with_input():
    def baker_map(points):
        mapped_points = np.empty_like(points)
        for i, (x, y) in enumerate(points):
            if x < 0.5:
                mapped_points[i] = 2 * x, y / 2
            else:
                mapped_points[i] = 2 * (1 - x), 1 - (y / 2)
        return mapped_points

    num_points = int(input("Kaç nokta girmek istiyorsunuz? "))
    points = np.empty((num_points, 2))

    for i in range(num_points):
        x = float(input("{}. noktanın x koordinatını girin: ".format(i+1)))
        y = float(input("{}. noktanın y koordinatını girin: ".format(i+1)))
        points[i] = x, y

    mapped_points = baker_map(points)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.scatter(points[:, 0], points[:, 1], color='blue', s=1)
    plt.title('Original Points')
    plt.xlim(0, 1)
    plt.ylim(0, 1)

    plt.subplot(1, 2, 2)
    plt.scatter(mapped_points[:, 0], mapped_points[:, 1], color='red', s=1)
    plt.title('Mapped Points by Baker Map')
    plt.xlim(0, 1)
    plt.ylim(0, 1)

    plt.tight_layout()
    plt.show()

baker_map_with_input()
