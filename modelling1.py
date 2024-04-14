import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
import keras
import numpy as np

df = pd.read_csv('detailedpesels.csv', delimiter=';')
features = df.drop(columns=['Bool'])
X_train, X_test, y_train, y_test = train_test_split(features, df.Bool, test_size=0.1)

inputs = keras.Input([4])
hidden_layer1 = keras.layers.Dense(100, activation='relu')(inputs)
hidden_layer2 = keras.layers.Dense(100, activation='relu')(hidden_layer1)
hidden_layer3 = keras.layers.Dense(100, activation='relu')(hidden_layer2)
hidden_layer4 = keras.layers.Dense(100, activation='relu')(hidden_layer3)
hidden_layer5 = keras.layers.Dense(100, activation='relu')(hidden_layer4)
hidden_layer6 = keras.layers.Dense(100, activation='relu')(hidden_layer5)
output_layer = keras.layers.Dense(1, activation='sigmoid')(hidden_layer6)
model = keras.Model(inputs=inputs, outputs=output_layer)
model.compile(optimizer='rmsprop', loss=keras.losses.BinaryCrossentropy())

history = model.fit(X_train, y_train, epochs=10, verbose=1)
sns.lineplot(x=history.epoch, y=history.history['loss'])
plt.show()
y_pred = model.predict(X_test)
roc_auc = roc_auc_score(y_test, y_pred)
print(f"ROC AUC score: {roc_auc}")
y_pred_bin = np.array(y_pred) > 0.5
y_pred_bin = y_pred_bin.astype(int)
accuracy = accuracy_score(y_test, y_pred_bin)
print(f"Accuracy score: {accuracy}")
df_confusion = pd.DataFrame((confusion_matrix(y_test, y_pred_bin)),
                            index=['Known Negative', 'Known Positive'],
                            columns=['Predicted Negative', 'Predicted Positive'])
print(df_confusion)
