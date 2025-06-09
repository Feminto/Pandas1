#Q1
#Create Pandas Dataframe from 2D List using pd.DataFrame()

import pandas as pd  

list_1 = [['Geek', 25],
          ['is', 30],
          ['for', 26],
          ['Geeksforgeeks', 22]] 

# creating df object with columns specified    
df = pd.DataFrame(list_1, columns =['Tag','number']) 
print(df )


#Q2
#Create Pandas Dataframe from 2D List using pd.DataFrame.from_records()

import pandas as pd

data = [['Geek1', 28, 'Analyst'],
        ['Geek2', 35, 'Manager'],
        ['Geek3', 29, 'Developer']]

columns = ['Name', 'Age', 'Occupation']

# Creating DataFrame using pd.DataFrame.from_records()
df = pd.DataFrame.from_records(data, columns=columns)
print(df)


#Q3
#Create Pandas Dataframe from 2D List using pd.DataFrame.from_dict()

import pandas as pd

data = [['Geek1', 26, 'Scientist'],
        ['Geek2', 31, 'Researcher'],
        ['Geek3', 24, 'Engineer']]

columns = ['Name', 'Age', 'Occupation']

# Creating DataFrame using pd.DataFrame.from_dict()
df = pd.DataFrame.from_dict(dict(zip(columns, zip(*data))))
print(df)



#Q4
#Create Pandas Dataframe from 2D List using Specifying Data Types
import pandas as pd

data = [['Geek1', 'Reacher', 25],
        ['Geek2', 'Pete', 30],
        ['Geek3', 'Wilson', 26],
        ['Geek4', 'Williams', 22]]

columns = ['FName', 'LName', 'Age']

# Creating DataFrame with specified data types
df = pd.DataFrame(data, columns=columns)
print(df)