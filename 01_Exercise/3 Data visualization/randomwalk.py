from random import choice

class RandomWalk():
    def __init__(self, num_points=500):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)


#print(rw.x_values)
#print(rw.y_values)

import matplotlib.pyplot as plt

"""
while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.title("Random Walk,", fontsize = 8)
    plt.xlabel("x-value", fontsize = 4)
    plt.ylabel("y-value", fontsize = 4)

    plt.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors=None,
        s=2
    )

    plt.show()

    keep_running = input('Make another walk? (y/n)')
    if keep_running == 'n':
        break
"""

while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.title("Random Walks", fontsize = 8)
    plt.xlabel("x-value", fontsize = 4)
    plt.ylabel("y-value", fontsize = 4)

    plt.plot(
        rw.x_values,
        rw.y_values,
        linewidth=1,
        c=point_numbers,
        cmap=plt.cm.Blues,
    )

    plt.show()

    keep_running = input('Make another walk? (y/n)')
    if keep_running == 'n':
        break
