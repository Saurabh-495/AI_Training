x = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]
y2 = [5, 15, 25, 35, 45]

plt.plot(x, y1, label="Line 1", color="blue", linestyle="--", marker="o")
plt.plot(x, y2, label="Line 2", color="red", linestyle="-.", marker="s")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Multiple Line Plot")
plt.legend()  # Show legend
plt.grid(True)  # Add grid lines

plt.show()

