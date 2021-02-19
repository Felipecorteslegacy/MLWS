setwd("C:/Users/TheCO/Downloads/Python/pythonProject")

#data = read.csv(file = "./Hoodies_data.csv", header = T, sep = ",")

#repeated_indices = c()

#for (row in 2:dim(data)[1]){
#  if(data$title[row] == data$title[row-1]){
#    next
#  } else{repeated_indices = c(repeated_indices, row)}
#}

#data_f = data[repeated_indices,]

library(readxl)

Hoodie_data = read_excel("Hoodie data clean.xlsx")


for (row in 1:dim(Hoodie_data)[1]){
  if (is.na(Hoodie_data$Units_sold[row]) == T){
    Hoodie_data$Units_sold[row] = 0
  }
}

price_mean = mean(Hoodie_data$Price)
price_sd = sd(Hoodie_data$Price)

us_mean = mean(Hoodie_data$Units_sold)
us_sd = sd(Hoodie_data$Units_sold)

windows()
hist(Hoodie_data$Price, breaks = 20)

x = seq(1, dim(Hoodie_data)[1], 1)

windows()
plot(x, Hoodie_data$Price)

index_random = which(Hoodie_data$Price > 500000)
random_data = Hoodie_data[index_random,]

Hoodie_data = Hoodie_data[-index_random,]

windows()
hist(Hoodie_data$Price, breaks = 20)

windows()
plot(Hoodie_data$Price, Hoodie_data$Units_sold)


# Data worth to analyse

Hoodie_data_w = Hoodie_data[which(Hoodie_data$Units_sold > 0),]

windows()
hist(Hoodie_data_w$Price, breaks = 20)

windows()
plot(Hoodie_data_w$Price, Hoodie_data_w$Units_sold)
