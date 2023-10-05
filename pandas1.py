
import numpy as np
import pandas as pd

# Create list of lists containing data.
list_df = [[32, 'Portugal', 94],
           [30, 'Argentina', 93],
           [25 , 'Brazil', 92]]

# Create index - names of players.
index = ['Christiano Ronaldo', 'Lionel Messi', 'Neymar']

# Create column names.
columns = ['Age', 'Nationality', 'Overall']

# Create dataframe by passing in data, index and columns.
print(pd.DataFrame(data=list_df, index=index, columns=columns))

# Create dictionary containing data.
dict_df = {
    "name":  ['Christiano Ronaldo', 'Lionel Messi', 'Neymar'],
    'Age':[32, 30, 25],
    'Nationality':['Portugal', 'Argentina', 'Brazil'],
    'Overall':[94, 93, 92]
    }

# Create index - names of players.
index = [1, 2, 3]

# Create dataframe by passing in data, index and columns.
print(pd.DataFrame(data=dict_df, index=index))

# Create numpy array containing data
array_df = np.array([
    ['Christiano Ronaldo', 32, 'Portugal', 94],
    ['Lionel Messi', 30, 'Argentina', 93],
    ['Neymar', 25 , 'Brazil', 92]
  ])

# Create index - names of players.
index = [1, 2, 3]

# Create column names.
columns = ["name", 'Age', 'Nationality', 'Overall']

# Create dataframe by passing in data, index and columns.
print(pd.DataFrame(data=array_df, index=index, columns=columns))

# Load data - pass 'Name' as our index column.
# For this exercise, we'll use football player data to evaluate our dataframe.
load_df = pd.read_csv('https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/fundamentals/football_players.csv', index_col='Name')

# Create dataframe called df.
df = pd.DataFrame(load_df)

# Use the head() function to look at the first 5 rows.
# you can also view the last 5 rows using .tail() function
print(df.head(10), df.tail(8))

#getting the shape or size of our data frame

print("shape of df: ", df.shape)

# Detailed information on the dataframe

print(df.info())

# Select the nth row using iloc[]. - iloc means index locator
print(df.iloc[17])
print(df.loc[17].head())

print(df.loc['T. Kroos'])

# Select by column.
print(df[['Nationality', 'Balance']].head())

#Exercise 1.
print(df[9:15])
print(df[['Preferred Positions', 'Overall', 'Age']].loc['Neymar'])
print(df[['Preferred Positions', 'Overall', 'Age']][df['Age']>=35])

# Sort column by ascending order (select first 5 entries).
print(df.sort_values(by='Age').head(5))
print(df.sort_values(by='Balance').tail(5))

# Sort column by descending order (select first 5 entries).
df.sort_values(by='Age', ascending=False).head()
df.sort_values(by='Balance', ascending=False).tail()

# Filtering.
print(df[(df['Age'] > 30)].tail())
print(df[(df['Overall'] > 70) & (df['Age'] < 30)].head())

print(df.describe())

under70players = df[(df['Overall'] <= 70)]
print(under70players.head())
print(under70players.shape)

# Unique gives use the distinct values in that column as an array
print(df['Nationality'].unique())
print(df['Balance'].unique().shape)

print(len(list(df['Balance'].unique())))
print(df['Nationality'].nunique())

# Create column of rating per year of age.
df['Rating Per Year of Age'] = df['Overall'] / df['Age']

# Look at first 5 entries.
print(df['Rating Per Year of Age'].head())

# Look at the minimum rating by age (first 5 rows).
print(df.groupby('Age').mean().tail())

# Look at the average rating by age and nationality (first 15 rows).
avrtng = df.groupby(['Age', 'Nationality']).mean().head(15)
print(avrtng)

#Exercise 1
print(df[df[['Preferred Positions']] == 'CB '])
print(df.loc['Neymar'])

df.groupby(['Nationality'], ascending  = False ).mean().head(15)
