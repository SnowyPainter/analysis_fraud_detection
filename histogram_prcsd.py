import data
import pandas as pd
import matplotlib.pyplot as plt

cols = ["V1", "V2", "V3", "V5", "V7"]
d = data.load()
fraud_data = data.get_incorrects(d, cols)
normal_data = data.get_corrects(d, 0.01, cols)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
for column in fraud_data.columns[:-1]:
    ax1.hist(fraud_data[column], bins=30, alpha=0.5, label=column)
for column in normal_data.columns[:-1]:
    ax2.hist(normal_data[column], bins=30, alpha=0.5, label=column)

ax1.legend()
ax2.legend()

ax1.set_ylabel('point count')
ax2.set_ylabel('point count')

ax1.set_title("Histogram of Fraud Detected Features")
ax2.set_title("Histogram of Normal Features")

plt.show()