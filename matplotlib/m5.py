import pandas as pd
import matplotlib.pyplot as plt


student = {
    "Monthly": ['Feb', 'Apr', 'June' , 'Sep' , 'Nov' , 'Dec'],
    "Eng" : [45,67,78,58,87,89],
    "Maths" : [55,87,98,88,97,69]
}

df_data = pd.DataFrame(student)
df_data['Totals'] = df_data['Eng'] + df_data['Maths']
df_data['PCT'] = df_data['Totals']/2

plt.scatter('Monthly', 'PCT' , s=50 , color= 'r' , data = df_data)
plt.xlabel('Monthly Exam')
plt.ylabel('Percentage')
plt.title('Percent')
plt.show()
