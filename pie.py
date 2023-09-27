import matplotlib.pyplot as plt
enames = ['rohan','ashwini','lohith','amar']
salary = [50000,15000,30000,40000]
plt.figure(figsize=(6,6))
plt.pie(salary, labels=enames, autopct='%1.2f%%', startangle=140)
plt.title('pie chart')
plt.legend()
plt.show()
