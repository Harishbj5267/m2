import numpy as np
import matplotlib.pyplot as plt
dataset=[1,11,10,10,100,140,108,107,110,120,150,113,23,40,4,9,6,74,89,30,10,6,0,9,7,23,5]
outliers=[]
def detect_outliers(data):  
    threshold = 3
    mean = np.mean(data)
    std = np.std(data)
    for i in data:
        z_score= (i-mean)/std
        if np.abs(z_score) > threshold:
            outliers.append(i)
    return outliers
outliers_pt=detect_outliers(dataset)
outliers_pt


sorted(dataset)

quantile1, quantile3= np.percentile(dataset,[25,75])
print(quantile1,quantile3)

iqr_value=(quantile3-quantile1)
print(iqr_value)


lower_bound_val = quantile1 -(1.5 * iqr_value)
upper_bound_val = quantile3 +(1.5 * iqr_value)
print(lower_bound_val,upper_bound_val)


import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(data = dataset)
plt.xlabel('dataset')
plt.ylabel('harish')
plt.title('scatter plot')
plt.show()
