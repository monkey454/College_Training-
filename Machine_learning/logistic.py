import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Simulated GRE data
def generate_dataset():
    gre_scores = np.array([280, 290, 295, 300, 305, 310, 315, 320, 325, 330,
                           285, 295, 305, 315, 325, 335, 340, 290, 300, 310])
    admissions =  np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
                            0, 0, 0, 1, 1, 1, 1, 0, 0, 1])
    df = pd.DataFrame({
        'GRE_Score': gre_scores,
        'Admission': admissions
    })
    return df

# Load dataset
dataset = generate_dataset()
print(dataset.head())

# Feature and label
x = dataset[['GRE_Score']].values
y = dataset['Admission'].values

# Plot
map_color = np.array(['r', 'b'])
plt.scatter(x, y, c=map_color[y])
plt.title('GRE Score and Admission')
plt.xlabel('GRE Score')
plt.ylabel('Gets Admission - Yes or No')
plt.grid(True)
plt.show()

# Train model
logistic_regression = LogisticRegression()
logistic_regression.fit(x, y)

# Predict class
class_label_Jacob = logistic_regression.predict([[304]])
print("The predicted class label for Jacob is:", class_label_Jacob)

class_label_Lacy = logistic_regression.predict([[299]])
print("The predicted class label for Lacy is:", class_label_Lacy)

# Predict log probabilities
probability_Jacob = logistic_regression.predict_log_proba([[304]])
print("The log probabilities for Jacob is:", probability_Jacob)

probability_Lacy = logistic_regression.predict_log_proba([[299]])
print("The log probabilities for Lacy is:", probability_Lacy)
