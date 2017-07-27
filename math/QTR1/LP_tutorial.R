# Load 'linprog' package
library(linprog)

# Create a cost vector
cvec <- c(3, 4)
# Create a constraint vector
bvec <- c(14, 0, 2)
#Create a constraint matrix
amat <- matrix(c(1, 2, -3, 1, 1, -1), ncol = 2, byrow = TRUE)
# Solve it: solveLP(c, b, A, maximum = TRUE)
solveLP(cvec, bvec, amat, maximum = TRUE)