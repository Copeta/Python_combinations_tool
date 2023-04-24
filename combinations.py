import pandas as pd
import itertools

#df=pd.read_excel('D:/Aleksa/data.xlsx')

"""
column1 = df['Wagon_type'].tolist()
column2 = df['Air_Supply'].tolist()
column3 = df['Passenger_Capacity'].tolist()
column4 = df['Number_of_Doors'].tolist()
column5 = df['Number_of_windows'].tolist()
column6 = df['Cabin_Door'].tolist()
column7 = df['Operation_Point'].tolist()
column8 = df['Weather_Category'].tolist()
"""
#"""
column1 = ['MC + MC','MC + M + MC','MC + T1 + MC','MC + M1 + M1 + MC','MC + T1 + M1 + MC','MC + T1 + T1 + MC','MC + M1 + M + M1 + MC',
           'MC + M1 + T + M1 + MC','MC + T1 + M + T1 + MC','MC + M1 + M + M + M1 + MC','MC + T1 + M + M + T1 + MC','MC + T1 + M + T + T1 + MC']
column2 = [4000,5000,6000,7000,8000]
column3 = [70,80,90,100,110,120,130,140,150,160]
column4 = [6,8,10]
column5 = [8,10,12]
column6 = ['Yes','No']
column7 = ['OP1','OP2','OP3','OP4','OP5','OP6','OP7','OP8','OP9','OP10','OP11','OP12','OP13','OP14','OP15','OP16']
column8 = ['I','II','III']
#"""
all_columns = [column1,column2,column3,column4,column5,column6,column7,column8]

combinations = list(itertools.product(*all_columns))
df_combinations = pd.DataFrame(combinations)
df_combinations.to_excel('combinations.xlsx', index=False)
#print(df)