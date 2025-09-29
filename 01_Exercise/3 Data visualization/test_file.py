import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)
plt.title('Square Numbers')
plt.xlabel('Value')
plt.ylabel('Square')
plt.show()
"""

import matplotlib.pyplot as plt
x_value = [1,2,3,4,5]
y_value = [1,4,9,16,25]
plt.scatter(x_value, y_value, c='red', s=100)
plt.title("Square Numbers", fontsize = 8)
plt.xlabel("value", fontsize = 4)
plt.ylabel("square", fontsize = 4)

plt.savefig('squares.png')
"""