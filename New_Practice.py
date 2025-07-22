import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.show()
sns.set_color_codes = True

df = pd.read_csv('Exploratory data analysis\\data.csv')

# print(df.head(5))

# print(df.tail(5))

# print(df.dtypes)

# print(df.shape)

df = df.drop(['Model', 'Engine Fuel Type', 'Market Category', 'Vehicle Style',
               'Popularity', 'Number of Doors', 'Vehicle Size', 'Driven_Wheels'], axis = 1)
# print(df.head(5))

df = df.rename(columns = {"Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission",
                "highway MPG": "MPG", "city mpg": "mpg"})
# print(df.head(5))

duplicate_df = df[df.duplicated()]
# print("Number of duplicate rows: ", duplicate_df.shape)

# print(df.count())

df = df.drop_duplicates()
# print(df.head(5))

# print(df.count())

# print(df.isnull().sum())

df = df.dropna()
# print(df.count())

# print(df.isnull().sum())

# sns.boxplot(x = df['Transmission'])
# plt.show()
# sns.boxplot(x = df['HP'])
# plt.show()
# sns.boxplot(x = df['Make'])
# plt.show()

# df.Make.value_counts().nlargest(40).plot(kind = 'bar', figsize = (10, 5))
# plt.title("Number of cars")
# plt.ylabel("num of cars")
# plt.xlabel("make")
# plt.show()

# plt.figure(figsize = (10, 5))
# c = df.select_dtypes(include = 'number').corr()
# sns.heatmap(c, cmap = 'BrBG', annot = True)
# plt.show()

fig, ax = plt.subplots(figsize = (10, 5))
ax.scatter(df['HP'], df['Year'])
ax.set_xlabel('HP')
ax.set_ylabel('Year')
plt.show()