import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
# Data Visualization
df_visualization = pd.read_csv('gender_pay_gap_prepared.csv')
df_visualization.drop(['Unnamed: 0', 'PostCode', 'SicCodes', 'EmployerSize'], axis=1, inplace=True)
print(df_visualization.shape, df_visualization.columns, df_visualization.isnull().sum(), df_visualization.head(5))
pd.set_option('display.max_columns', None)
print(df_visualization.describe())
# Plot graphs
# Plot1: Histogram on DiffMeanHourly Percent
fig1, ax1 = plt.subplots()
ax1.set_title('Distribution of DiffMeanHourlyPercent')
ax1.hist(df_visualization[['DiffMeanHourlyPercent']], bins=50)
# Plot2: Histogram on DiffMedianHourly Percent
fig2, ax2 = plt.subplots()
ax2.set_title('Distribution of DiffMedianHourlyPercent')
ax2.hist(df_visualization[['DiffMedianHourlyPercent']], bins=50)
# Plot3: BoxPlot of DiffMeanHourlyPercent against EmployerSizeMedian
fig3, ax3 = plt.subplots()
ax3 = sns.boxplot(data=df_visualization, y="DiffMeanHourlyPercent", x="EmployerSizeMedian")
ax3.set(ylim=(-200, 200))
ax3.set_title('BoxPlot of DiffMeanHourlyPercent against EmployerSizeMedian')
# Plot4: BoxPlot of DiffMeanBonusPercent against EmployerSizeMedian
fig4, ax4 = plt.subplots()
ax4 = sns.boxplot(data=df_visualization, y="DiffMeanBonusPercent", x="EmployerSizeMedian")
ax4.set(ylim=(-200, 200))
ax4.set_title('BoxPlot of DiffMeanBonusPercent against EmployerSizeMedian')
# Plot5: BoxPlot of FemaleTopQuartile against EmployerSizeMedian
fig5, ax5 = plt.subplots()
ax5 = sns.boxplot(data=df_visualization, y="FemaleTopQuartile", x="EmployerSizeMedian")
ax5.set(ylim=(-200, 200))
ax5.set_title('BoxPlot of DiffMeanBonusPercent against EmployerSizeMedian')
# Plot6: BoxPlot of DiffMeanHourlyPercent against EmployerSizeMedian & Industry
fig6, ax6 = plt.subplots()
ax6 = sns.boxplot(data=df_visualization, y="DiffMeanHourlyPercent", x="Industry", hue='EmployerSizeMedian')
ax6.set(ylim=(-200, 200))
ax6.tick_params(axis='x', labelrotation=90)
ax6.set_title('BoxPlot of DiffMeanHourlyPercent against EmployerSizeMedian & Industry')
# Plot7: BoxPlot of DiffMeanBonusPercent against EmployerSizeMedian & Industry
fig7, ax7 = plt.subplots()
ax7 = sns.boxplot(data=df_visualization, y="DiffMeanBonusPercent", x="Industry", hue='EmployerSizeMedian')
ax7.set(ylim=(-200, 200))
ax7.tick_params(axis='x', labelrotation=90)
ax7.set_title('BoxPlot of DiffMeanBonusPercent against EmployerSizeMedian & Industry')
# Plot8: BoxPlot of FemaleTopQuartile against EmployerSizeMedian & Industry
fig8, ax8 = plt.subplots()
ax8 = sns.boxplot(data=df_visualization, y="FemaleTopQuartile", x="Industry", hue='EmployerSizeMedian')
ax8.set(ylim=(-50, 150))
ax8.tick_params(axis='x', labelrotation=90)
ax8.set_title('BoxPlot of DiffMeanHourlyPercent against EmployerSizeMedian & Industry')
plt.show()
