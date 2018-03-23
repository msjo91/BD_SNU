# Read data
winedf <- read.table('~/projects/big_data_snu/math/QTR1/wine.tsv', header = T, sep = '\t')
# Open table
View(winedf)

### k-fold Cross Validation

# Assign subset number 1-to-10 for each wine
folds <- rep_len(1:10, nrow(winedf))
# Create variable for RMSE value (Root Mean Square Error)
rmse <- 0

# 10-fold
for (i in 1:10) {
    # Create subset Si
    test_set <- winedf[which(folds == i),]
    # Create training set
    training_set <- winedf[which(folds != i),]
    # Create a linear regression model for training set
    model <- lm(quality ~ ., data = training_set)
    # Get errors between predicted values and true values
    error <- predict(model, test_set) - test_set$quality
    # Cumulate RMSE values
    rmse <- rmse + sqrt(sum(error * error) / length(test_set))
}

# Get the average RMSE value
rmse <- rmse / 10