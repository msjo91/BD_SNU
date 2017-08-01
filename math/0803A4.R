library(linprog)

### Q2
# x: chocolate cream bread
# y: baguette
# 10x + 4y
# 100x + 50y ≤ 3000
# 10x ≤ 100

## Q2(a)
# Create a cost vector
cvec <- c(10, 4)
# Create a constraint vector
bvec <- c(3000, 100)
# Create a constraint matrix
amat <- matrix(c(100, 50, 10, 0), ncol = 2, byrow = TRUE)

## Q2(b)
# Solve it!
solveLP(cvec, bvec, amat, maximum = TRUE)

### Q3
# 18A + 29B + 25C
# 0.5A + 0.2B + 0.75C ≤ 1500
# 0.2A + 0.4B + 0.2C ≤ 600
# A ≥ 1000
# B ≥ 200
# C ≥ 400

## Q3(a)
# Create a cost vector
cvec <- c(18, 29, 25)
# Create a constraint vector
bvec <- c(1500, 600, -1000, -200, -400)
# Create a constraint matrix
amat <- matrix(c(0.5, 0.2, 0.75, 0.2, 0.4, 0.2, -1, 0, 0, 0, -1, 0, 0, 0, -1), ncol = 3, byrow = TRUE)

## Q3(b)
# Solve it!
solveLP(cvec, bvec, amat, maximum = TRUE)

### Q4
# xi: hired in the i-th month
# yi: fired in the i-th month
# 8000(x1 - y1 + x1 - y1 + x2 - y2 + x1 - y1 + x2 - y2 + x3 - y3) + 10000(y1 + y2 + y3) + 5000(x1 + x2 + x3)
# 8000(3x1 + 2x2 + x3 - 3y1 - 3y2 - y3) + 10000(y1 + y2 + y3) + 5000(x1 + x2 + x3)
# 29000x1 + 21000x2 + 13000x3 - 14000y1 - 6000y2 + 2000y3
# 20 + x1 - y1 ≥ 30
# 20 + x1 - y1 + x2 - y2 ≥ 60
# 20 + x1 - y1 + x2 - y2 + x3 - y3 ≥ 55

##Q4(a)
cvec <- c(29000, 21000, 13000, -14000, -6000, 2000)
# Create a constraint vector
bvec <- c(-10, -40, -35)
# Create a constraint matrix
amat <- matrix(
    c(
        -1, 0, 0, 1, 0, 0,
        -1, -1, 0, 1, 1, 0,
        -1, -1, -1, 1, 1, 1
        ),
    ncol = 6,
    byrow = TRUE
    )

##Q4(b)
# Solve it!
solveLP(cvec, bvec, amat, maximum = FALSE)
