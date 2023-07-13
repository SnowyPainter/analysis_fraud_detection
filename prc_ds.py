import data
import numpy as np
import matplotlib.pyplot as plt

cols = ["V1", "V2", "V3", "V5", "V7", "Amount", "Time", "Class"]
ratio = 0.01 #1/10
pca_data, pca_columns = data.get_normal_samples(ratio, cols)

pca_data.to_csv("./csv_datas/normal_dataset.csv")

nc = ["V1", "V2", "V3", "V5", "V7"]
d = pca_data[nc]
def print_corr():
    print(d.corr(method='pearson'))
def show_andrews():
    plt.figure(figsize=(12, 6))
    plt.plot(np.transpose(d), alpha=0.5)
    plt.xlabel('Samples')
    plt.ylabel('Values')
    plt.title('Andrews Curve')
    plt.legend(nc)
    plt.show()

print_corr()
show_andrews()