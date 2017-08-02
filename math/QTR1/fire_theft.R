# Read data
firedf <- read.table('~/projects/big_data_snu/math/QTR1/fire_theft.tsv', header=TRUE, sep=',')
# Open table
View(firedf)
# Draw a scatter plot
plot(firedf$X, firedf$Y)
# Create a linear regression model
model <- lm(firedf$Y ~ firedf$X, data = firedf)
# Draw a line
abline(model, col = 'red')