import matplotlib.pyplot as plt

# Data
subjects = ["Math", "Science", "English", "History", "Computer"]
students = [25, 30, 15, 10, 20]  # Har subject ko choose karne wale students

# Pie Chart Banana
# plt.pie(students, labels=subjects, autopct='%1.1f%%', startangle=90)
explode = (0, 0, 0.1, 0, 0)  # Science ka slice thoda bahar aayega
plt.pie(students, labels=subjects, explode=explode, autopct='%1.1f%%', startangle=90)
# plt.show()


# Title
plt.title("Subjects Distribution among Students")

# Chart Dikhana
plt.show()
