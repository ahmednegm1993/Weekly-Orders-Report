import pandas as pd
import datetime
df=pd.read_excel(r'E:\Data_analysis_projects\Weekly Orders Report\dataset\Weekly Orders Report.xlsx')
df['week']=pd.to_datetime(df['week'])
df['week_number'] = df['week'].dt.isocalendar().week
df_q1_2023 = df[df['week_number'].between(1, 13)]
result = df_q1_2023.groupby('week_number')['quantity'].sum().reset_index()
print(result)
