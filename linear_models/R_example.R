# Author: Jonathan Lisic
# License: BSD-3

library(readxl); library(dplyr); library(magrittr); library(ggplot2)

#download file
download.file('http://www2.census.gov/prod2/statcomp/usac/excel/INC01.xls',
              '~/INC01.xls')

# open csv, select variables, and keep counties
# STCOU is state and county fips
census_inc <- read_xls('~/INC01.xls') %>% 
  select(Area_name, STCOU, INC110179D, INC110189D, INC110199D, INC110209D) %>%
  filter( substr(STCOU,3,5) != '000' )

# create a linear model
fit <-  lm(INC110209D ~ INC110179D + INC110189D + INC110199D, 
     data=census_inc)

# plot observed vs fitted
p <- ggplot( census_inc, aes(x=INC110209D, y=fit$fitted.values)) + 
  geom_point() + 
  labs( title="Median Income by County 2009\nFitted v.s. Observed",
        x="Observed",
        y="Fitted")
plot(p)
