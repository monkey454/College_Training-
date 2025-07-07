# code to visualize the best fit line
def visualize_best_fit_line():  
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LinearRegression

    # Sample data
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([1, 2, 3, 4, 5])

    # Create a linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Predict values
    y_pred = model.predict(X)

    # Plotting the data points and the best fit line
    plt.scatter(X, y, color='blue', label='Data Points')
    plt.plot(X, y_pred, color='red', label='Best Fit Line')
    plt.xlabel('Input Feature')
    plt.ylabel('Target Variable')
    plt.title('Best Fit Line using Linear Regression')
    plt.legend()
    plt.show()
# Call the function to visualize the best fit line
visualize_best_fit_line()