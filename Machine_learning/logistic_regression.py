
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification

def generate_dataset():
    dataset = make_classification(n_samples=20, n_features=1, n_repeated=0, n_redundant=0, scale=10, n_classes=2, n_clusters_per_class=1, n_informative=1, class_sep=1, random_state=1)
    df = pd.DataFrame(dataset[0])
    df = pd.concat([(np.ceil(df)).astype(int), pd.DataFrame(dataset[1])], axis=1)
    df.columns = ['GRE_Score', 'Admission']
    return df

dataset = generate_dataset()
print(dataset.head())

map_color = np.array(['r', 'b'])
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values

plt.scatter(dataset.GRE_Score, dataset.Admission, c = map_color[y])
plt.title('GRE Score and Admission')
plt.xlabel('GRE Score')
plt.ylabel("Gets Admission - Yes or No")
plt.show()