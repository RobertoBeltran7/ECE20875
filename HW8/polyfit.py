import numpy as np
import matplotlib.pyplot as plt


# Return fitted model parameters to the dataset at datapath for each choice in degrees.
# Input: datapath as a string specifying a .txt file, degrees as a list of positive integers.
# Output: paramFits, a list with the same length as degrees, where paramFits[i] is the list of
# coefficients when fitting a polynomial of d = degrees[i].
def main(datapath, degrees):
    paramFits = []

    # fill in
    # read the input file, assuming it has two columns, where each row is of the form [x y] as
    # in poly.txt.
    # iterate through each n in degrees, calling the feature_matrix and least_squares functions to solve
    # for the model parameters in each case. Append the result to paramFits each time.
    file_open = open(datapath, 'r')
    data = file_open.readlines()
    x = [float(j[0]) for j in (i.split() for i in data)]
    y = [float(j[1]) for j in (i.split() for i in data)]

    file_open.close()

    for d in degrees:
        feat_mtrx = feature_matrix(x, d)
        Beta = least_squares(feat_mtrx, y)
        paramFits.append(Beta)

    return paramFits


# Return the feature matrix for fitting a polynomial of degree d based on the explanatory variable
# samples in x.
# Input: x as a list of the independent variable samples, and d as an integer.
# Output: X, a list of features for each sample, where X[i][j] corresponds to the jth coefficient
# for the ith sample. Viewed as a matrix, X should have dimension #samples by d+1.
def feature_matrix(x, d):
    # fill in
    # There are several ways to write this function. The most efficient would be a nested list comprehension
    # which for each sample in x calculates x^d, x^(d-1), ..., x^0.
    X = [[num ** deg for deg in range(d, -1, -1)] for num in x]

    return X


# Return the least squares solution based on the feature matrix X and corresponding target variable samples in y.
# Input: X as a list of features for each sample, and y as a list of target variable samples.
# Output: B, a list of the fitted model parameters based on the least squares solution.
def least_squares(X, y):
    X = np.array(X)
    y = np.array(y)

    # fill in
    # Use the matrix algebra functions in numpy to solve the least squares equations. This can be done in just one line.
    least_sqrs = np.linalg.inv(X.T @ X) @ X.T @ y
    B = least_sqrs.tolist()

    return B


if __name__ == '__main__':
    datapath = 'poly.txt'
    degrees = [2, 4]

    paramFits = main(datapath, degrees)
    print(paramFits)

    # Step 2
    degrees = [1, 2, 3, 4, 5]
    paramFits = main(datapath, degrees)
    print(paramFits)

    # Step 3
    file_open = open(datapath, 'r')
    data = file_open.readlines()
    x = [float(j[0]) for j in (i.split() for i in data)]
    y = [float(j[1]) for j in (i.split() for i in data)]

    file_open.close()

    plt.scatter(x, y, c='red', marker='*',label='datapoints')

    x.sort()
    for coeff in paramFits:
        deg_num = len(coeff) - 1
        feat_mtrx = np.array(feature_matrix(x, deg_num))
        y_hat = feat_mtrx @ coeff
        plt.plot(x, y_hat, label= 'd = '+str(deg_num))
    plt.legend(fontsize=10)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of fitted models')
    plt.show()

