import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import data

cols = ["V1", "V2", "V3", "V5", "V7"]
pca_data, pca_columns = data.get_V_sample(0.0001, cols)
plt.figure(figsize=(12, 6))
plt.plot(np.transpose(pca_data), alpha=0.5)
plt.xlabel('Samples')
plt.ylabel('Values')
plt.title('Andrews Curve')
plt.legend(cols)
plt.show()

# 소분해서 시각화하기