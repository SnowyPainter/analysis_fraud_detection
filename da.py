import pandas as pd

data = pd.read_csv('credit_card_dataset.csv')

correlation = data.drop(['Class', 'Time'], axis=1).corr(method='pearson')
correlation.to_csv('./csv_datas/correlation_matrix.csv', index=True)
descriptive_stats = data.describe()
descriptive_stats.to_csv('./csv_datas/descriptive_stats.csv')

print("Correlation matrix saved to correlation_matrix.csv")
print("Descriptive statistics saved to descriptive_stats.csv")