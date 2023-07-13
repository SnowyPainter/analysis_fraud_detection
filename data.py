import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load():
    data = pd.read_csv('./csv_datas/credit_card_dataset.csv')
    return data

def get_V_sample(ratio, cols):
    data = load()
    data = data.sample(frac=ratio, random_state=42)
    pca_columns = cols
    pca_data = data[pca_columns]
    return pca_data, pca_columns

def get_corrects(data, ratio, cols):
    data = data[data['Class'] == 0].sample(frac=ratio, random_state=42)[cols]
    return data
def get_incorrects(data, cols):
    fraud_data = data[data['Class'] == 1][cols]
    return fraud_data

def get_normal_samples(ratio, cols):
    data = load()
    pca_columns = cols
    pca_data = pd.concat([get_corrects(data, ratio, cols), get_incorrects(data, cols)])[pca_columns]
    return pca_data, pca_columns