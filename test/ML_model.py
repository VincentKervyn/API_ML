
import pandas as pd

from sklearn.externals import joblib



df = pd.read_csv('../test.csv')
include = ['Age', 'Sex', 'Embarked']
df_ = df[include]  # only using 3 variables

# replace Nan with 0
categoricals = []
for col, col_type in df_.dtypes.iteritems():
     if col_type == 'O':
          categoricals.append(col)
     else:
          df_[col].fillna(0, inplace=True)

# OneHotEncoder
df_ohe = pd.get_dummies(df, columns=categoricals, dummy_na=True)

#  to train our model.
dependent_variable = 'Embarked'
x = df_ohe[df_ohe.columns.difference([dependent_variable])]
y = df_ohe[dependent_variable]
clf = rf()
clf.fit(x, y)

# save model
joblib.dump(clf, 'model.pkl')




