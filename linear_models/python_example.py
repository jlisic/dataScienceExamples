# Author: Jonathan Lisic
# License: BSD-3

import pandas 
from sklearn import linear_model
from matplotlib import pyplot as plot

#read in excel file
census_inc = pandas.read_excel('http://www2.census.gov/prod2/statcomp/usac/excel/INC01.xls')

#subset data and query fips
census_inc = census_inc[
  ["Area_name", "STCOU", "INC110179D", "INC110189D", "INC110199D", "INC110209D"]].query('STCOU % 100 != 0')

# create a linear model
fit = linear_model.LinearRegression()
fit.fit(
  census_inc[["INC110179D", "INC110189D", "INC110199D"]].astype(float),
  census_inc["INC110209D"].astype(float)
  )

fitted = fit.predict(census_inc[["INC110179D", "INC110189D", "INC110199D"]].astype(float))

# Plot outputs
plot.scatter( census_inc["INC110209D"],fitted,color='black')
plot.title("Median Income by County 2009\nFitted v.s. Observed")
plot.xlabel( "Observed" )
plot.ylabel( "Fitted" )
plot.show()


