import cvxpy as cp
import numpy as np
# Initialize A (m x n) and b (m x 1).
np.random.seed(0)
m, n = 20, 5
A = np.random.randn(m,n)
b = np.random.randn(m)
# Unconstrained Least Squares
x = cp.Variable(n) # Regression coefficients
objective = cp.Minimize(cp.sum_squares(A@x- b))
prob = cp.Problem(objective)
result = prob.solve()
print("Optimal value:", result)
print("Optimal x:", x.value)

# Constrained Least Squares
x_constrained = cp.Variable(n)
constraints = [ x_constrained >= 0.5,
cp.sum(x_constrained) <= 3.0 ]
obj_constrained = cp.Minimize(cp.sum_squares(A@x_constrained- b))
prob_constrained = cp.Problem(obj_constrained, constraints)
result_constrained = prob_constrained.solve()

print(result_constrained)