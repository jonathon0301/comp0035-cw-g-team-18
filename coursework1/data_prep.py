from pathlib import Path
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# Load initial datasets
df_1 = pd.read_csv(
    '/Users/shishengjie/Desktop/comp0035-cw-g-team-18/coursework1/Gender_Pay_Gap/UK Gender Pay Gap Data - 2017 to 2018.csv')
df_2 = pd.read_csv(
    '/Users/shishengjie/Desktop/comp0035-cw-g-team-18/coursework1/Gender_Pay_Gap/UK Gender Pay Gap Data - 2018 to 2019.csv')
df_3 = pd.read_csv(
    '/Users/shishengjie/Desktop/comp0035-cw-g-team-18/coursework1/Gender_Pay_Gap/UK Gender Pay Gap Data - 2019 to 2020.csv')
df_4 = pd.read_csv(
    '/Users/shishengjie/Desktop/comp0035-cw-g-team-18/coursework1/Gender_Pay_Gap/UK Gender Pay Gap Data - 2020 to 2021.csv')
df_5 = pd.read_csv(
    '/Users/shishengjie/Desktop/comp0035-cw-g-team-18/coursework1/Gender_Pay_Gap/UK Gender Pay Gap Data - 2021 to 2022-2.csv')
df_6 = pd.read_csv(
    '/Users/shishengjie/Desktop/comp0035-cw-g-team-18/coursework1/Gender_Pay_Gap/UK Gender Pay Gap Data - 2022 to 2023-3.csv')
dfs = [df_1, df_2, df_3, df_4, df_5, df_6]
for df in dfs:
    print(df.shape, df.columns, df.dtypes)

# Merge datasets into a single large one and save
df_merge = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6], axis=0)
print(df_merge.shape, df_merge.columns)
df_merge.to_csv(r'/Users/shishengjie/Desktop/comp0035-cw-g-team-18/coursework1/gender_pay_gap_initial.csv')

# Delete unnecessary columns
df_merge.drop(['Address', 'EmployerName', 'EmployerId', 'CompanyNumber', 'CompanyLinkToGPGInfo',
               'ResponsiblePerson', 'CurrentName', 'SubmittedAfterTheDeadline', 'DueDate'], axis=1, inplace=True)
print(df_merge.shape, df_merge.columns)

# Check null values
print(df_merge.isnull().sum())

# Show correlations
pd.set_option('display.max_columns', None)
print(df_merge.corr())
ax = sns.heatmap(df_merge.corr(), linewidth=0.5)
plt.show()

# Deal with null values
df_merge = df_merge.dropna(subset=['MaleLowerQuartile', 'SicCodes', 'PostCode'])
print(df_merge.shape, df_merge.columns, df_merge.isnull().sum())
# Split the dataset into training and testing
df_merge_training = df_merge[df_merge['DiffMedianBonusPercent'].notnull()].dropna(subset=['DiffMeanBonusPercent'])
print(df_merge_training.shape, df_merge_training.columns, df_merge_training.isnull().sum())
df_merge_testing = df_merge[df_merge['DiffMedianBonusPercent'].isnull()]
print(df_merge_testing.shape, df_merge_testing.columns, df_merge_testing.isnull().sum())
# Train random forest regression model
# NOTE: This can quite slow, please wait
X_train = df_merge_training[['DiffMeanHourlyPercent',
                             'DiffMedianHourlyPercent', 'MaleBonusPercent', 'FemaleBonusPercent',
                             'MaleLowerQuartile', 'FemaleLowerQuartile', 'MaleLowerMiddleQuartile',
                             'FemaleLowerMiddleQuartile', 'MaleUpperMiddleQuartile',
                             'FemaleUpperMiddleQuartile', 'MaleTopQuartile', 'FemaleTopQuartile']]
y_1_train = df_merge_training[['DiffMeanBonusPercent']]
y_2_train = df_merge_training[['DiffMedianBonusPercent']]
X_test = df_merge_testing[['DiffMeanHourlyPercent',
                           'DiffMedianHourlyPercent', 'MaleBonusPercent', 'FemaleBonusPercent',
                           'MaleLowerQuartile', 'FemaleLowerQuartile', 'MaleLowerMiddleQuartile',
                           'FemaleLowerMiddleQuartile', 'MaleUpperMiddleQuartile',
                           'FemaleUpperMiddleQuartile', 'MaleTopQuartile', 'FemaleTopQuartile']]
model_1 = RandomForestRegressor(n_estimators = 100, random_state = 0)
model_2 = RandomForestRegressor(n_estimators = 100, random_state = 0)
model_1.fit(X_train, y_1_train)
model_2.fit(X_train, y_2_train)
# Predict the value with the testing data and substitute values to null values
y_1_pred = model_1.predict(X_test)
y_2_pred = model_2.predict(X_test)
print(y_1_pred, y_2_pred)
df_merge_testing = df_merge_testing.assign(DiffMeanBonusPercent=y_1_pred)
df_merge_testing = df_merge_testing.assign(DiffMedianBonusPercent=y_2_pred)
print(df_merge_testing.shape, df_merge_testing.columns, df_merge_testing.isnull().sum())

# Bind the two dataset together again
df_none_na = pd.concat([df_merge_training, df_merge_testing], axis=0)
print(df_none_na.shape, df_none_na.columns, df_none_na.isnull().sum(), df_none_na.head(5))
