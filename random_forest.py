import data
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import accuracy_score

d, cols = data.get_normal_samples(0.01, ["V1", "V2", "V3", "V5", "V7", "Amount", "Time", "Class"])

X = d[["V1", "V2", "V3", "V5", "V7", "Amount", "Time"]]
y = d[["Class"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

rfm = RandomForestClassifier(random_state=42)
rfm.fit(X_train, y_train)
#test data acc
y_scores = rfm.predict_proba(X_test)[:, 1]

def plot_ROC():
    #ROC curve
    fpr, tpr, thresholds = roc_curve(y_test, y_scores)
    roc_auc = auc(fpr, tpr)
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='blue', lw=2, label='ROC curve (AUC = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='red', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('FP rate')
    plt.ylabel('TP rate)')
    plt.title('ROC curve')
    plt.legend(loc="lower right")

    plt.show()

def find_appropriate(fpr_cutoff, tpr_cutoff):
    fpr, tpr, thresholds = roc_curve(y_test, y_scores)
    threshold_idx = (fpr <= fpr_cutoff) & (tpr >= tpr_cutoff)
    if np.sum(threshold_idx) > 0:
        optimal_threshold = thresholds[threshold_idx][0]
        y_pred = (y_scores >= optimal_threshold).astype(int)
        return accuracy_score(y_test, y_pred)
    else:
        return None

fpr_cutoffs = np.arange(0.1, 0.35, 0.05)
tpr_cutoffs = np.arange(0.8, 1.01, 0.03)
accuracies = []

for fpr_cutoff in fpr_cutoffs:
    for tpr_cutoff in tpr_cutoffs:
        accuracy = find_appropriate(fpr_cutoff, tpr_cutoff)
        accuracies.append(accuracy)

accuracies = np.array(accuracies).reshape(len(fpr_cutoffs), len(tpr_cutoffs))

plt.figure(figsize=(10, 6))
x, y = np.meshgrid(tpr_cutoffs, fpr_cutoffs)
plt.scatter(x, y, c=accuracies, cmap='hot', edgecolors='k', linewidths=0.5)
plt.colorbar(label='Accuracy')
plt.xlabel('TPR Cutoff')
plt.ylabel('FPR Cutoff')
plt.title('Accuracy for Different Cutoff Combinations')
plt.show()