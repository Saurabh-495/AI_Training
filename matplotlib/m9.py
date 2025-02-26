import matplotlib.pyplot as plt

# Example data
marks = [89,90,70,89,100,80,90,100,80,34]
marks_range = [10,20,30,40,50,60,70,80,90,100]

colors = 'r'

circle_area = 25
contrast = 0.9
#plot

plt.scatter(marks , marks_range , s = circle_area, c=colors , alpha = contrast)
plt.title("Plot Marks")
plt.xlabel("Mark Range")

plt.ylabel("Marks obtained")

plt.show()