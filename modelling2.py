import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

df = pd.read_csv('detailedpesels.csv', delimiter=';')
# features = df.drop(columns=['Bool'])
# features = df.drop(columns=['BirthDate', 'Century', 'Gender', 'Bool'])
features = df.drop(columns=['BirthDate', 'Bool'])
X_train, X_test, y_train, y_test = train_test_split(features, df.Bool, test_size=0.1)
model = MLPClassifier(hidden_layer_sizes=(11, 100, 100, 100, 100, 100, 100, 100, 100, 100), max_iter=10000, activation='relu')

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
# model.score(X_test,y_test)
# print(f"Score: {model.score(X_test,y_test)}")
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy score: {accuracy}")
df_confusion = pd.DataFrame((confusion_matrix(y_test, y_pred)),
                            index=['Known Negative', 'Known Positive'],
                            columns=['Predicted Negative', 'Predicted Positive'])
print(df_confusion)
