import pandas as pd
data = {'name':['roshan','amar','ashwini','lohith','mohan','promod'],
        'type':['regular','adhoc','regular','adhoc','contract','regular'],
        'department':['cs','cs','ec','ec','cs','ec'],
        'salary':[50000,15000,30000,15000,10000,40000]
       }
print(pd.DataFrame(data))        
       
