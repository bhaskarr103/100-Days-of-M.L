import numpy as np


#    Perform gradient descent to minimize the mean squared error.
#    Parameters:
#    - x: Input features (numpy array)
#    - y: Target values (numpy array)
#    - learning_rate: Step size for each iteration
#    - iterations: Number of iterations
#
#    Returns:
#    - cost: List of cost values at each iteration


def gradient_descent(x,y):
    m_curr = b_curr = 0
    iterations = 10
    learning_rate = 0.01
    n = len(x)

    for i in range(iterations):
        y_pred = m_curr * x + b_curr

        cost = (1/n) * sum([val**2 for val in (y - y_pred)])
        md = -(2/n) * sum(x*(y-y_pred)) # derivative of m
        bd = -(2/n) * sum(y-y_pred) # derivative of b

        m_curr = m_curr - learning_rate * md # (m)new = (m)old - lr * derivative of m
        b_curr = b_curr - learning_rate * md

        print("m {}, b {}, cost {}, iterations {}".format(m_curr,b_curr,cost,i))

    pass

x = np.array([1,2,3,4,5])
y = np.array([5,6,7,9,10])

gradient_descent(x,y)