# -*- coding: utf-8 -*-
"""

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1v3bbJw8B3-tOgEW1iXTmE5fq8HJOjGW6
"""

import pandas as pd

df=pd.read_csv('adult.csv')

df

df.education.value_counts()

df.workclass.value_counts()

df.occupation.value_counts()

df.gender.value_counts()

import pandas as pd

df = pd.concat([df.drop('occupation', axis=1), pd.get_dummies(df['occupation']).add_prefix('occupation')], axis=1)
df = pd.concat([df.drop('workclass', axis=1), pd.get_dummies(df['workclass']).add_prefix('workclass')], axis=1)
df = df.drop('education', axis=1)
df = pd.concat([df.drop('marital-status', axis=1), pd.get_dummies(df['marital-status']).add_prefix('marital-status')], axis=1)
df = pd.concat([df.drop('relationship', axis=1), pd.get_dummies(df['relationship']).add_prefix('relationship')], axis=1)
df = pd.concat([df.drop('race', axis=1), pd.get_dummies(df['race']).add_prefix('race')], axis=1)
df = pd.concat([df.drop('native-country', axis=1), pd.get_dummies(df['native-country']).add_prefix('native_country')], axis=1)

df

df['gender']=df['gender'].apply(lambda x:1 if x=='Male' else 0)
df['income']=df['income'].apply(lambda x:1 if x== '>50' else 0)

df['income']

df.columns.values

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(18, 12))
sns.heatmap(df.corr(), annot=False, cmap='coolwarm')
plt.show()

df.corr()

correlations = df.corr()['income'].abs()
sorted_correlations = correlations.sort_values()
num_cols_to_drop = int(0.5 * len(df.columns))
cols_to_drop = sorted_correlations.iloc[:num_cols_to_drop].index
df_dropped = df.drop(cols_to_drop, axis=1)

df_dropped

plt.figure(figsize=(15,10))
sns.heatmap(df_dropped.corr(), annot=True, cmap='coolwarm')
plt.show()

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
df = df.drop(['fnlwgt'], axis=1)

train_df,test_df=train_test_split(df,test_size=0.2)

train_df

test_df

train_X=train_df.drop('income',axis=1)
train_y=train_df['income']

test_X=test_df.drop('income',axis=1)
test_y=test_df['income']

forest= RandomForestClassifier()
forest.fit(train_X,train_y)

forest.score(test_X,test_y)

forest.feature_importances_

importances = dict(zip(forest.feature_names_in_, forest.feature_importances_))
importances = {k: v for k, v in sorted(importances.items(), key=lambda X: X[1], reverse=True)}

importances

from sklearn.model_selection import GridSearchCV
param_grid={
    'n_estimators': [50,100,250],
    'max_depth':[5,10,30, None],
    'min_samples_split':[2,4],
    'max_features':['sqrt','log2']
}
grid_search=GridSearchCV(estimator=RandomForestClassifier(),param_grid=param_grid,verbose=10)

grid_search.fit(train_x, train_y)

best_estimator = grid_search.best_estimator_
best_estimator

best_estimator.score(test_x,test_y)

importances

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# Assuming X is your feature matrix, y is the target variable
clf = RandomForestClassifier(n_estimators=100, random_state=42)
scores = cross_val_score(clf, train_x, train_y, cv=5)  # Use an appropriate number of folds (e.g., cv=5)
print("Cross-Validation Accuracy: {:.2f}%".format(scores.mean() * 100))
