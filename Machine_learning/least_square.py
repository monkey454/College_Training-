import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.linspace(0, 10, 50)
noise = np.random.normal(0, 1, size=x.shape)
y = 2 * x + 5 + noise

def compute_least_squares(x, y):
    """
    Compute the coefficients of the least squares line.
    :param x: Input feature values
    :param y: Target values
    :return: Coefficients (slope and intercept)
    """
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    a = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
    b = y_mean - a * x_mean
    return a, b

def plot_least_squares_line(x, y, a, b):
    """
    Plot the data points and the least squares line.
    :param x: Input feature values
    :param y: Target values
    :param a: Slope of the line
    :param b: Intercept of the line
    """
    plt.scatter(x, y, label='Data Points')
    plt.plot(x, a * x + b, color='red', label='Least Squares Line')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Least Squares Method')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    a, b = compute_least_squares(x, y)
    print(f"Computed coefficients: a = {a}, b = {b}")
    plot_least_squares_line(x, y, a, b)
    print("The least squares line has been plotted successfully.")
    print("This line represents the best fit for the given data points, minimizing the sum of squared differences between the predicted and actual values.")
    print("You can modify the data points or the noise level to see how it affects the least squares line.")
    print("This method is widely used in regression analysis to find the best-fitting line for a set of data points.")
    print("Feel free to explore further by adding more data points or changing the parameters.")
    print("Thank you for using the Least Squares Method example!")