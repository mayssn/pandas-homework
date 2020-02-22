import numpy as np
import pandas as pd

df = pd.read_csv (r'~/Desktop/insurance.csv')


#----------------------

#makes the DataFrame reader-friendly on console
# print(df.to_string())

#----------------------


#prints the column lables
print(df.columns)

#----------------------

#prints range of rows of the DataFrame
# print(df.index)

#----------------------

#the data type of each column
#print(df.dtypes)

#----------------------

# the shape of the data set, in this case it is 2 D so rows then columns (1338, 7)
# print(df.shape)

#----------------------

# Prints info about the DataFrame. First number of rows, and the range in which they are on the file.  Number of
# columns, and datatypes. non values and memory usage.
#print(df.info())

#----------------------

#  General stats on the table (only numeric values it seems). The count of records on each column, mean, stf,
#  min value, 25, 50%, 75% and max value.
#print(df.describe())

#----------------------

# Print only the column age
#print(df['age'])

#----------------------

# Print only the columns age,children and charges
# print(df[['age', 'children', 'charges']])

#----------------------

# Print only the first 5 lines and only the columns age,children and charges
# print(df[['age', 'children', 'charges']].head(5))

#----------------------

# What is the average, minimum and maximum charges ?

# print(df['charges'].describe())

# min: 1121.873900, ,max: 63770.428010  , average : 13270.422265


#----------------------

# What is the age and sex of the person that paid 10797.3362. Was he/she a smoker?

# print(df.query('charges == 10797.3362'))

# 52 years old female


#----------------------

# What is the age of the person who paid the maximum charge?

# Method 1
# print(df['charges'].describe())
# print(df.query('charges == 63770.428010'))

# Method 2
# print(df.loc[df['charges'].idxmax()])

# answer: age 54

#----------------------

# How many insured people do we have for each region?
#print(df.groupby(['region']).size())

# answer  northeast  = 324  / northwest    325 / southeast    364  / southwest    325
#----------------------

# How many insured people are children?
# print(df.groupby(['age']).size())

# right away i can see that none. usually i research further to find the formula to give me the specific answer
#but will try to complete other tasks first

#----------------------

# What do you expect to be the correlation between charges and age, bmi and children?

# 1- Smokers pay more.

# 2- First instinct is to say that charges go up with age. But based on experience, they usually ask:
    # "are you above x age". So i think it might be fixed per age until a specific age point then premium goes up)
    # As such, there will be a correlation, but weak-moderate one.

# 3- BMI and charges : strong positive

# 4- I do not have enough information to determine the correlation between premiums and children.
    # I could say that group purchases will make price go down, but I don't have sufficient info to assume
    # that the insurer is getting a family plan. It could be, for example travel insurance

#----------------------

# Using the method corr(), check if your assumptions were correct.

# smoker is non numeric therefore I need to convert categories into numeric first
# I will use kendall, spearman and pearson - and merge the columns into one table for comparison purposes

# df['smoker']=df['smoker'].astype('category').cat.codes
# cork= df.corr(method ='kendall')
# a= cork['charges']
# print(a)
#
#
# cors= df.corr(method ='spearman')
# b= cors['charges']
# print(b)
#
# corp= df.corr(method ='pearson')
# c= corp['charges']
# print(c)
#
# # joining and averaging:
# d = pd.concat([a, b, c], axis=1, join='inner')
# d['average'] = d.mean(axis=1)
#
# print(d)

#I tried to rename the columns using this method, it isn't working. It is extracting the index from original file.
#not sure how to fix it
#d= df.rename(index={0: "kendall", 1: "spearman", 2: "pearson"})


# Back to the analysis , the answers are:
# there is according to Kendall and spearman (not pearson) a moderate positive correlation btw BMI and charges
# there no/ weak correlation btw charges and BMI (weird)
# no correlation with having children
# smokers do pay more
