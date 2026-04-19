import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load a real dataset
df = sns.load_dataset('titanic')    # real dataset od titanic passengers

# print(df.head())    
# print(df.shape)
# print(df.columns)

# df.info()
# print(df.isnull().sum())

# pd.set_option('display.max_columns', None)
# print(df.describe())

# print(df['sex'].value_counts())
# print(df['pclass'].value_counts())
# print(df['embarked'].value_counts())
# print(df['survived'].value_counts())

sns.set(style="darkgrid")   # makes plot look nicer

# pie chart (gender)
df['sex'].value_counts().plot.pie(autopct='%1.1f%%', startangle= 90, colors=['skyblue', 'lightcoral'])
plt.title('Gender Distribution')
plt.ylabel('')  # remove y-label
plt.show()

# bar chart (class)
sns.countplot(x='pclass', data=df, palette='viridis')
plt.title('Passenger Class Distribution')
plt.xlabel('Class')
plt.ylabel('Count')
plt.show()

# bar chart (survival by gender)
sns.countplot(x='sex', hue='survived', data=df)
plt.title('Survival Count by Gender')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.show()

# histogram of age
df['age'].plot.hist(bins=30, edgecolor='black', color='teal')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.show()

# boxplot - age vs pclass
sns.boxplot(x='pclass', y='age', data= df, palette='Pastel1')
plt.title('Age vs Passenger class')
plt.xlabel('Class')
plt.ylabel('Age')
plt.show()

