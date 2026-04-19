import pandas as pd

s = pd.Series([10,20,30])
print(s)

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}
df = pd.DataFrame(data)
print(df)
print(df.head())  # first 5 rows
print(df.tail())  # first 5 columns
print(df[['Name', 'City']])
print(df.loc[0])    # row with index 0
print(df.loc[1, 'City'])    # bob's city


# task
print(df['Age'])
print(df[['Name', 'City']])
print(df.loc[1])
print(df.loc[2, 'City'])


# modifying and adding data
df['Country'] = ['USA', 'UK', 'France']
df['Age'] += 1
df.loc[3] = ['David', 28, 'Berlin', 'Germany']


#task
df['Gender'] = ['F', 'M', 'M', 'M']
df['Age'] += 2
df.loc[4] = ['Emma', 27, 'Rome', 'Italy', 'F']


# filtering and conditional selection
print(df[df['Age']>30])
print(df[df['City']=='London'])
print(df[(df['Age']<30) & (df['Gender']=='F')])


#task
print(df[df['Age']>28])
print(df[df['City']=='Rome'])
print(df[df['Gender']=='F'])
print(df[(df['Age']>26) & (df['Gender']=='M')])


# sorting and aggregating data
print(df.sort_values(by='Age'))
print(df.sort_values(by='Age', ascending=False))
print(df['Age'].mean())
print(df['Age'].max())
print(df['Age'].min())
print(df.groupby('Gender')['Age'].mean())


# task
print(df.sort_values(by='Name'))
print(df.sort_values(by='Age', ascending=False))
print(df['Age'].mean())
print(df.groupby('Gender')['Age'].mean())

