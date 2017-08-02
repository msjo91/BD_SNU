# Load subway.csv file to a data frame
# Use read.table
df <- data.frame(read.table('~/projects/big_data_snu/math/subway.csv', header = TRUE, sep = ',', stringsAsFactors = FALSE))

# Create a new column "passengers"
df$passengers <- df$get_in + df$get_off

# (a) What is the average number of passengers of Sinchon station?
# The number should be stored in the variable 'ans_a'.
ans_a <- mean(df$passengers[which(df$station_name == "신촌" & df$line == "2호선")])

# (b) Find top 10 subway stations in terms of the avg. number of passengers.
# The list of top 10 subway stations should be stored in the variable 'ans_b'.
# (Hint: you may use sort function like the following codes)
t <- c(1, 3, 2, 5, 4)
s <- sort(t, decreasing = T)
s
# Rename certain values
df$station_name[which(df$station_name == '신촌' & df$line == '2호선')] <- '신촌(2호선)'
df$station_name[which(df$station_name == '신촌')] <- '신촌(경의선)'
df$station_name[which(df$station_name == '양평' & df$line == '5호선')] <- '양평(5호선)'
df$station_name[which(df$station_name == '양평' & df$line == '중앙선')] <- '양평(중앙선)'
# Create a new table of average passengers grouped by station.
msdf <- aggregate(df$passengers ~ df$station_name, data = df, FUN = mean)
# Rename columns
names(msdf) <- c("station_name", "avg_passengers")
# Get the names!
ans_b <- msdf$station_name[head(order(msdf$avg_passengers, decreasing = TRUE), 10)]

# (c) Find top 3 subway lines in terms of the average number of passengers.
# The list of top 3 subway lines should be stored in the variable 'ans_c'.
# Create a new table of average passengers grouped by line.
mldf <- aggregate(df$passengers ~ df$line, data = df, FUN = mean)
# Rename columns
names(mldf) <- c("line", "avg_passengers")
# Get the lines!
ans_c <- mldf$line[head(order(mldf$avg_passengers, decreasing = TRUE), 3)]

# (d) Draw scatter plots for the number of passengers of Nakseongdae station and Incheon Int'l Airport station.
# Create a new table of total passengers in Nakseongdae grouped by day.
ndf <- aggregate(df$passengers[which(df$station_name == '낙성대')] ~ df$date[which(df$station_name == '낙성대')], data = df, FUN = sum)
# Rename columns
names(ndf) <- c("date", "passengers")
# Plot
plot(ndf$passengers ~ ndf$date, xlab = 'Date', ylab = 'Passengers', main = 'Nakseongdae')
# Create a new table for Incheon Int'l Airport station grouped by day.
idf <- aggregate(df$passengers[which(df$station_name == '인천국제공항')] ~ df$date[which(df$station_name == '인천국제공항')], data = df, FUN = sum)
# Rename columns
names(idf) <- c("date", "passengers")
# Plot
plot(idf$passengers ~ idf$date, xlab = 'Date', ylab = 'Passengers', main = 'Incheon Int\'l Airport')