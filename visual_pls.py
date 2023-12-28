import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import webbrowser
df=pd.read_csv('regression_pls.csv')
df.head()
df.shape
t=df['Target'].values
x=df.drop('Target', axis=1).values
t.shape
x.shape
x_train, x_test,t_train, t_test=train_test_split(x, t, test_size=0.3, random_state=0)
model=LinearRegression()
model.fit(x_train, t_train)
print(f'train score: {model.score(x_train, t_train)}')
print(f'test score: {model.score(x_test, t_test)}')
df_corr=df.corr()
plt.figure(figsize=(12,8))
sns.heatmap(df_corr.iloc[:20, :20], annot=True)
PdfFile='output\\heatmap.pdf'
plt.savefig(PdfFile)
webbrowser.open_new(PdfFile)
sns.jointplot(x='x1', y='Target', data=df)
PdfFile='output\\jointplot.pdf'
plt.savefig(PdfFile)
webbrowser.open_new(PdfFile)