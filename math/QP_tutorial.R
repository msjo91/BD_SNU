# Quadratic Programming
# Load quadprog
library(quadprog)

# min x^2 + 4(y - 4)^2
# x + y ≤ 7
# -x + 2y ≤ 4
# y ≤ 4
# x ≥ 0
# y ≥ 0

hmat <- matrix(c(2, 0, 0, 8), ncol = 2, byrow = T)
cvec <- c(0, 32)
amat_t <- matrix(c(-1, -1, 1, -2, 0, -1), ncol = 2, byrow = T)
bvec <- c(-7, -4, -4)

# solve.QP(H, c, A, b, meq = 0)
solve.QP(hmat, cvec, t(amat_t), bvec)