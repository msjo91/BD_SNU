# Load 'linprog' package
library(linprog)

## Requirements
# x1 + x2 + x3 + x4 ≤ 1000000
# 0.6x1 - 0.4x2 - 0.4x3 + 0.6x4 ≤ 0 
# -0.2x1 - 0.2x2 - 0.2x3 + 0.8x4 ≤ 0
# -x1 ≤ -200000
# -x4 ≤ -80000
# -x3 ≤ -60000
# x3 ≤ 220000
# -3x2 + x3 ≤ 0

# Create a cost vector
cvec <- c(0.09, 0.14, 0.1, 0.05)
# Create a constraint vector
bvec <- c(1000000, 0, 0, -200000, -80000, -60000, 220000, 0)
# Create a constraint matrix
amat <- matrix(
    c(
        1, 1, 1, 1,
        0.6, -0.4, -0.4, 0.6,
        -0.2, -0.2, -0.2, 0.8,
        -1, 0, 0, 0,
        0, 0, 0, -1,
        0, 0, -1, 0,
        0, 0, 1, 0,
        0, -3, 1, 0
    ),
    ncol = 4,
    byrow = TRUE
)
# Solve
solveLP(cvec, bvec, amat, maximum = TRUE)