import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import data

cols = ["V1", "V2", "V3", "V5", "V7"]
pca_data, pca_columns = data.get_V_sample(0.0001, cols)

# 편차 차트 그리기
plt.figure(figsize=(12, 6))
plt.plot(pca_data - pca_data.mean(), alpha=0.5)
plt.xlabel('Samples')
plt.ylabel('Deviation')
plt.title('Deviation Chart')
plt.legend(["V1", "V2", "V3", "V5", "V7"])
plt.show()