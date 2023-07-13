import data
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def modeling(data, features, label):
    data_x = data[features]
    data_y = d[label]
    X_train, X_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.25, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

def check_accuracy():
    # 일부 특성만 decision tree
    ratio = 0.05

    d, cols = data.get_normal_samples(ratio, ["V1", "V2", "V3", "V5", "V7", "Amount", "Time", "Class"])
    print(modeling(d, ["V1", "V2", "V3", "V5", "V7", "Amount", "Time"], ["Class"]))

    # 전체 데이터로 decision tree
    v = ["V" + str(i) for i in range(1, 29)] + ["Amount", "Time", "Class"]
    entire_data, cols = data.get_normal_samples(ratio, v)
    print(modeling(entire_data, v[:-1], ["Class"]))

import matplotlib.pyplot as plt

ratios = [0.001, 0.005, 0.01, 0.03]
accuracies = []

for ratio in ratios:
    d, cols = data.get_normal_samples(ratio, ["V1", "V2", "V3", "V5", "V7", "Amount", "Time", "Class"])
    accuracy = modeling(d, ["V1", "V2", "V3", "V5", "V7", "Amount", "Time"], ["Class"])
    accuracies.append(accuracy)

# 그래프 그리기
plt.plot(np.array(284808) * ratios, accuracies, marker='o')
plt.xlabel('Samples')
plt.ylabel('Accuracy')
plt.title('Accuracy by Samples')
plt.show()