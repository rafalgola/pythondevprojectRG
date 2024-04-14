import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = pd.read_csv('detailedpesels.csv', delimiter=';')
features = df.drop(columns=['Bool'])
# features = df.drop(columns=['BirthDate', 'Century', 'Gender', 'Bool'])
X_train, X_test, y_train, y_test = train_test_split(features, df.Bool, test_size=0.1)
model = LogisticRegression()
model.fit(X_train, y_train)

print('Klasy są zbalansowane:')
print(df.Bool.value_counts())

print(model.score(X_test, y_test))
# print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))
df_confusion = pd.DataFrame((confusion_matrix(y_test, model.predict(X_test))),
                            index=['Known Negative', 'Known Positive'],
                            columns=['Predicted Negative', 'Predicted Positive'])
print(df_confusion)