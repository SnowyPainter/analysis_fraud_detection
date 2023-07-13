import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 데이터셋 로드
data = pd.read_csv('credit_card_dataset.csv')

fraud_transactions = data[data['Class'] == 1]

# 사기 거래의 금액 분포
plt.figure(figsize=(12, 6))
plt.hist(fraud_transactions['Amount'], bins=30, label='Fraud Transactions')
plt.xlabel('Transaction Amount')
plt.ylabel('Count')
plt.title('Transaction Amount Distribution')
plt.legend()
plt.show()