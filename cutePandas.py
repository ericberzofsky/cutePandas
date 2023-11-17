import pandas as pd
import matplotlib.pyplot as plt

###########
# Series are defined by list

members = ['Brazil', 'Russia', 'India', 'China', 'South Africa']
bricks1 = pd.Series(members)
print(bricks1)
print(type(bricks1))

#############
# Output:
#0          Brazil
#1          Russia
#2           India
#3           China
#4    South Africa

# DataFrames are defined by dictionaries

members = {"country": ['Brazil', 'Russia', 'India', 'China', 'South Africa'],
           "capital": ['Brasilia', 'Moscow', 'New Delhi', 'Beijing', 'Pretoria'],
           "gdp": [2750, 1650, 3202, 15270, 370],
           "literacy": [.944, .997, .721, .964, .943],
           "expectency": [76.8, 72.7, 68.8, 76.4, 63.6],
           "population": [210.87, 143.96, 1367.09, 1415.05, 57.4]}
bricks2 = pd.DataFrame(members)
print(bricks2)
print(type(bricks2))

#############
# Output:
#        country    capital    gdp  literacy  expectency  population
#0        Brazil   Brasilia   2750     0.944        76.8      210.87
#1        Russia     Moscow   1650     0.997        72.7      143.96
#2         India  New Delhi   3202     0.721        68.8     1367.09
#3         China    Beijing  15270     0.964        76.4     1415.05
#4  South Africa   Pretoria    370     0.943        63.6       57.40

# You can also define a DataFrame with two sets of lists:
# a list of the value,
# and a list of the labels
members = [['Brazil', 'Brasilia', 2750, .944, 76.8, 210.87],
           ['Russia', 'Moscow', 1650, .997, 72.7, 143.96],
           ['India', 'New Delhi', 3202, .721, 68.8, 1367.09],
           ['China', 'Beijing', 15270, .964, 76.4, 1415.05],
           ['South Africa', 'Pretoria', 370, .943, 63.6, 57.4]]
labels = ["country", "capital", "gdp", "literacy", "expectency", "population"]
bricks3 = pd.DataFrame(members, columns=labels)
print(bricks3)
print(type(bricks3))

# pd.read_csv
# pd.read_excel, imports first sheet by default
# pd.read_excel(sheet_name=)

# Visualizations
plt.scatter(x=bricks3['country'], y=bricks3['gdp'])
plt.show()
