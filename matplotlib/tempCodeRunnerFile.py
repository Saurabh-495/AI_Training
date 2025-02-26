data = (g1, g2, g3)
colors = ("red", "green", "blue")
groups = ("Red House", "Green House", "Blue House")
for data, color, group in zip(data, colors, groups):
x, y = data
plt.scatter(y, x, alpha=0.8, c=color, edgecolors='none', s=30, label=group)