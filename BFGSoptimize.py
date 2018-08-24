import numpy as np
from scipy.optimize import minimize


def rosenbrock(x):
    return 100*((x[2] - x[1]**2)**2 + (x[1] - x[0]**2)**2) + (1-x[1])**2 + (1-x[0])**2


def rosen_derivative(x):
    derivative = np.zeros(3)
    derivative[0] = -400*(x[1] - x[0]**2)*x[0] - 2*(1-x[0])
    derivative[1] = 200*(x[1] - x[0]**2) - 400*(x[2] - x[1]**2)*x[1] - 2*(1-x[1])**2
    derivative[2] = (200*(x[2] - x[1]**2))
    return derivative


if __name__ == '__main__':
    opt_res = None
    opt_val = float('Inf')
    for x in np.linspace(-10, 10, 10):
        for y in np.linspace(-10, 10, 10):
            for z in np.linspace(-10, 10, 10):
                res = minimize(rosenbrock, [x, y, z], method='BFGS', jac=rosen_derivative)
            if res.fun < opt_val:
                opt_val = res.fun
                opt_res = res

print(opt_res)

