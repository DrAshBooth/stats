import pylab

x = [3, 4, 2, 4, 3, 5, 2, 3]
y = [4, 2, 5, 3, 3, 2, 4, 4]

##############################
########## Plotting ##########
##############################

# Histograms
pylab.hist(x)

# Scatter plots
pylab.scatter(x, y)

# Bar Charts
pylab.bar(x, y)

pylab.show()
