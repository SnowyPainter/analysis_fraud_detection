# About Dataset
## Context
It is important that credit card companies are able to recognize fraudulent credit card transactions so that customers are not charged for items that they did not purchase.

## Content
The dataset contains transactions made by credit cards in September 2013 by European cardholders.
This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.

It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, we cannot provide the original features and more background information about the data. Features V1, V2, … V28 are the principal components obtained with PCA, the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount, this feature can be used for example-dependant cost-sensitive learning. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.

Given the class imbalance ratio, we recommend measuring the accuracy using the Area Under the Precision-Recall Curve (AUPRC). Confusion matrix accuracy is not meaningful for unbalanced classification.

## Acknowledgements
The dataset has been collected and analysed during a research collaboration of Worldline and the Machine Learning Group (http://mlg.ulb.ac.be) of ULB (Université Libre de Bruxelles) on big data mining and fraud detection.

# Korean
데이터셋에 대해서 ...  
신용카드 회사는 고객이 자신이 구매하지 않은 물품에 대해 청구되지 않도록 사기성 신용카드 거래를 인식할 수 있어야 합니다.

## 내용
이 데이터셋은 2013년 9월에 유럽 카드 소지자들의 신용카드 거래 내역을 담고 있습니다. 이 데이터셋은 2일 동안 발생한 거래를 보여줍니다. 이 중 284,807건의 거래 중 492건은 사기입니다. 이 데이터셋은 매우 불균형하며, 양성 클래스(사기)는 전체 거래의 0.172%를 차지합니다.

이 데이터셋은 PCA 변환의 결과인 숫자형 입력 변수만 포함하고 있습니다. 기밀성 문제로 인해 원래의 특성 및 데이터에 대한 추가적인 배경 정보는 제공할 수 없습니다. V1, V2, ..., V28은 PCA를 통해 얻은 주요 구성 요소입니다. PCA로 변환되지 않은 유일한 특성은 'Time'과 'Amount'입니다. 'Time' 특성은 각 거래와 데이터셋의 첫 번째 거래 사이에 경과한 시간(초)을 나타냅니다. 'Amount' 특성은 거래 금액으로, 예를 들어 종속 비용 감도 학습에 사용할 수 있습니다. 'Class' 특성은 응답 변수이며, 사기일 경우 값이 1이고 그렇지 않으면 0입니다.

클래스 불균형 비율을 고려하여, 불균형 분류에 대한 정확도를 측정할 때는 Precision-Recall 곡선 아래 면적 (AUPRC)을 사용하는 것이 좋습니다. 혼동 행렬의 정확도는 불균형한 분류에 대해 의미가 없습니다.