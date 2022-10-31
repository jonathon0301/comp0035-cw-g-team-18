from pathlib import Path
import pandas as pd

#Load initial datasets
df_1 = pd.read_csv('/Users/shishengjie/Desktop/comp0035-cw-g-team-18/coursework1/Gender_Pay_Gap/UK Gender Pay Gap Data - 2017 to 2018.csv')
df_2 = pd.read_csv('/Users/shishengjie/Desktop/comp0035-cw-g-team-18/coursework1/Gender_Pay_Gap/UK Gender Pay Gap Data - 2018 to 2019.csv')
df_3 = pd.read_csv('/Users/shishengjie/Desktop/comp0035-cw-g-team-18/coursework1/Gender_Pay_Gap/UK Gender Pay Gap Data - 2019 to 2020.csv')
df_4 = pd.read_csv('/Users/shishengjie/Desktop/comp0035-cw-g-team-18/coursework1/Gender_Pay_Gap/UK Gender Pay Gap Data - 2020 to 2021.csv')
df_5 = pd.read_csv('/Users/shishengjie/Desktop/comp0035-cw-g-team-18/coursework1/Gender_Pay_Gap/UK Gender Pay Gap Data - 2021 to 2022-2.csv')
df_6 = pd.read_csv('/Users/shishengjie/Desktop/comp0035-cw-g-team-18/coursework1/Gender_Pay_Gap/UK Gender Pay Gap Data - 2022 to 2023-3.csv')
dfs = [df_1, df_2, df_3, df_4, df_5, df_6]
for df in dfs:
    print(df.shape, df.columns, df.dtypes)

#Merge datasets into a single large one and save
df_merge = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6], axis = 0)
print(df_merge.shape, df_merge.columns)
df.to_csv(r'/Users/shishengjie/Desktop/comp0035-cw-g-team-18/coursework1/gender_pay_gap_initial.csv')

#Delete unnessary columns
del df_merge['EmployerName', 'EmployerId','CompanyNumber','CompanyLinkToGPGInfo',
       'ResponsiblePerson','CurrentName']
print(df_merge)
