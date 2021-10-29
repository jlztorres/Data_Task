# Question 1 - a
import pandas as pd
ratings_df = pd.read_csv(r'C:\Users\José Luciano\Downloads\BID-PY\ratings.csv')

# Question 1 - b
print(len(ratings_df['worker'].unique()),  ' unique respondents')
print(len(ratings_df['aspect'].unique()), ' unique aspects')

# Question 1 - c
ratings_df.sort_values(['worker','time'])        
ratings_df.drop_duplicates(['aspect','worker'], keep='last')
print(len(ratings_df) - len(ratings_df.drop_duplicates(['aspect','worker'], keep='last')), 'observations delete')
unique_rating_df = ratings_df.drop_duplicates(['aspect','worker'], keep='last')

# Question 1 - d
unique_rating_df[['worker','rating']]
average_rating_df = unique_rating_df[['worker','rating']].groupby('worker', as_index=False).mean()
average_rating_df 
average_rating_df.describe()['subjective riches'][-5:] #only min max and lower medean upper quartile

# Question 2 - a
demographics_df = pd.read_csv(r'C:\Users\José Luciano\Downloads\BID-PY\demographics.csv')

# Question 2 - b
print(len(demographics_df), '... rows number of demographics.csv')
print(len(demographics_df) == len(average_rating_df))

# Question 2 - c
demographics_df
demographics_order = demographics_df.sort_values('worker')
demographics_order
average_rating_df_order = average_rating_df.sort_values('worker')
average_rating_df_order
df_order = pd.DataFrame
df_order = df_order.merge(demographics_order,average_rating_df_order)
df_order 

# Question 2 - d
import numpy as np
from sklearn.linear_model import LinearRegression
x = np.array(df_order['income']).reshape(-1,1)
y = np.array(df_order['subjective riches'])
lr_model = LinearRegression()
lr_model.fit(x,y)
print(str(lr_model.coef_), 'b1')
print(str(lr_model.intercept_), 'b0')

# Question 2 - e
x1 = df_order['age'].tolist()
x_2 = df_order['age'].tolist()
x2=[]
for i in range(len(x_2)):
    x2.append(pow(x_2[i],2))
    
x3 = df_order['male'].tolist()
x4 = df_order['education'].tolist()
x5 = df_order['race'].tolist()

    # categorical values (education) to numerical
    # usaría encoders pero las comillas (  Bachelor's degree...Master's degree  ) no lo permite
    # also REGEX could be used

# Question 3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_order[['age','income','subjective riches']]
corr_df = df_order[['age','income','subjective riches']].corr(method='pearson')
plt.figure(figsize=(8, 6))
sns.heatmap(corr_df, annot=True)
plt.show()