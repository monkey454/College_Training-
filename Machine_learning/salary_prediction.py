import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.impute import SimpleImputer  

# load dataset
df = pd.read_csv('Salary Data.csv')
print('first 5 rows:\n',df.head())

# basic information
print(df.info())

# finding total missing values
print(df.isnull().sum())

# Plot pairwise relationships in a DataFrame (Age, Years of Experience and Salary)
sns.pairplot(df)
plt.suptitle('pairplot of variables',y=1.02)
plt.show()

# plotting correlation between each pair of variables.
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True),annot=True,cmap='Blues')
plt.title('Correlation heatmap')
plt.show()

# Converts each categorical column into multiple binary (0/1) columns
df_encoded = pd.get_dummies(df, columns=['Gender', 'Education Level', 'Job Title'], drop_first=True)
print("\nEncoded Columns:\n", df_encoded.columns)

# Data Preprocessing (removing the rows with missing values (NaN))
df_encoded.dropna(inplace=True)

# Step 7: Feature and Target Selection
X = df_encoded.drop('Salary', axis=1)
y = df_encoded['Salary']

# Step 8: Impute Missing Values in X (if any)
imputer = SimpleImputer(strategy="mean")
X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

# Splitting the training/testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 10: Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# display the coefficients (weights) learned by a linear model after training
print("\nModel Coefficients:")
coeff_df = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print(coeff_df)

#Predict values on Test Data
y_pred = model.predict(X_test)
print(y_pred)

# Model Evaluation
print("\nModel Performance:")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R-squared:", r2_score(y_test, y_pred))

# Visualization - Actual vs Predicted
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred, alpha=0.6, color="blue")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel("Actual Salary")
plt.ylabel("Predicted Salary")
plt.title("Actual vs Predicted Salary")
plt.show()

# Residual Analysis (shows how your prediction errors (residuals) are distributed)
residuals = y_test - y_pred

sns.histplot(residuals, kde=True)
plt.title("Residuals Distribution")
plt.xlabel("Residuals")
plt.show()

plt.figure(figsize=(6, 4))
plt.scatter(y_pred, residuals, alpha=0.5)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel("Predicted Salary")
plt.ylabel("Residuals")
plt.title("Residuals vs Predicted")
plt.show()

# Step 16: Predict Salary from New Input
def predict_salary(age, gender, education_level, job_title, years_of_experience):
    input_data = pd.DataFrame({
        'Age': [age],
        'Years of Experience': [years_of_experience],
        'Gender_' + gender: [1],
        'Education Level_' + education_level: [1],
        'Job Title_' + job_title: [1],
    })

    # Ensure all columns match
    for col in X.columns:
        if col not in input_data.columns:
            input_data[col] = 0

    input_data = input_data[X.columns]  # Order columns
    predicted_salary = model.predict(input_data)[0]
    print(f"\nPredicted Salary for Input: NPR {predicted_salary:.2f}")
    return predicted_salary

#example
predict_salary(age=30,gender='Male',education_level='Bachelors',job_title='Data Scientist',years_of_experience=15)