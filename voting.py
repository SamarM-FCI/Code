# -*- coding: utf-8 -*-
"""Voting.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S5Cf1RtxJqxkwAo7MXk9m4iwH5fDShLD
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

data_f = pd.read_csv("predictions_bert.csv")
data_s = pd.read_csv("predictions.csv")

pred_SVC.head()

data_f = pd.read_csv("predictions_bert.csv")

data_s = pd.read_csv("predictions.csv")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

x = data_f.Actual_Label
y = data_f.Predicted_Label
# Evaluate the model
accuracy = accuracy_score(x, y)
print(f"Accuracy: {accuracy}")

merged_predictions = pd.concat([pred_BLSTM['Predicted_Label'], data_s['Predicted_Label'], data_f['Predicted_Label']], axis=1, keys=['BLSTM', 'SVC', 'BERT'])

merged_predictions

#soft voting mechanism, where you combine the probabilities or logits from each model and then make a decision based on the combined information.
# This can be done using logistic regression,
#but it requires stacking the predicted probabilities from each model as features for training the logistic regression model.

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(merged_predictions, pred_SVC['Actual_Label'], test_size=0.2, random_state=42)

# Train logistic regression model
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = lr_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

predictions = y_pred
val_y = y_test

from sklearn.metrics import classification_report, roc_auc_score, accuracy_score, f1_score, precision_score, recall_score
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

# Assuming val_y is your true labels and predictions are your predicted labels

# Print Classification Report
print("Classification Report:")
print(classification_report(val_y, predictions))

# Calculate and Print ROC-AUC Score
roc_auc = roc_auc_score(val_y, predictions)
print(f"ROC-AUC Score: {roc_auc:.4f}")

# Calculate and Print Accuracy
accuracy = accuracy_score(val_y, predictions)
print(f"Accuracy: {accuracy:.4f}")

# Calculate and Print F1 Score
f1 = f1_score(val_y, predictions)
print(f"F1 Score: {f1:.4f}")

# Calculate and Print Precision
precision = precision_score(val_y, predictions)
print(f"Precision: {precision:.4f}")

# Calculate and Print Recall
recall = recall_score(val_y, predictions)
print(f"Recall: {recall:.4f}")

# Plot ROC Curve
fpr, tpr, thresholds = roc_curve(val_y, predictions)
roc_auc_curve = auc(fpr, tpr)

plt.figure(figsize=(10, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = {:.2f})'.format(roc_auc_curve))
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()

fpr_lstm, tpr_lstm, thresholds_lstm = roc_curve(y_true, y_pred)

fpr_lstm

tpr_lstm