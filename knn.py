from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import data
import numpy as np
import pandas as pd

# 데이터셋 로드 및 특성과 레이블 분리
# X: V1, V2, V3, V5, V7, Amount, Time
# y: Class
def modeling(dataset, features, label, k=5):
    X = dataset[features]
    y = dataset[label]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return accuracy_score(y_test, y_pred)

import matplotlib.pyplot as plt
def show_accbyrat():
    ratios = [0.001, 0.005, 0.01, 0.03]
    accuracies = []
    d, cols = data.get_normal_samples(ratio, ["V1", "V2", "V3", "V5", "V7", "Amount", "Time", "Class"])
    for ratio in ratios:
        accuracy = modeling(d, ["V1", "V2", "V3", "V5", "V7", "Amount", "Time"], ["Class"])
        accuracies.append(accuracy)

    # 그래프 그리기
    plt.plot(np.array(284808) * ratios, accuracies, marker='o')
    plt.xlabel('Samples')
    plt.ylabel('Accuracy')
    plt.title('Accuracy by Samples')
    plt.show()

k_values = [1, 3, 5, 7, 9] 
accuracies = []
d, cols = data.get_normal_samples(0.01, ["V1", "V2", "V3", "V5", "V7", "Amount", "Time", "Class"])
for k in k_values:
    accuracies.append(modeling(d, ["V1", "V2", "V3", "V5", "V7", "Amount", "Time"], ["Class"], k))

plt.plot(k_values, accuracies, marker='o')
plt.xlabel('k')
plt.ylabel('Accuracy')
plt.title('Accuracy vs k')
plt.show()
