# imporing required libraries.
import pandas as pd
import numpy as np
import seaborn as sns #visualization
import matplotlib.pyplot as plt #visualization
# %matplotlib inline => specific command to Jupyter notebooks.
plt.show()
sns.set_color_codes = True
# sns.set_theme(style = "darkgrid", palette = "deep")

df = pd.read_csv("Exploratory data analysis\\data.csv")
# to diplay the top 5 rows.
print(df.head(5))

# to display the bottom 5 rows.
print(df.tail(5))

# ckeck the data  type.
print(df.dtypes)

# dropping irrelevant columns.
df = df.drop(['Engine Fuel Type', 'Market Category', 'Vehicle Style',
               'Popularity', 'Number of Doors', 'Vehicle Size'], axis = 1)
            # axis = 0 → operate along rows, axis = 1 → operate along columns.
print(df.head(5))

# renaming the columns.
df = df.rename(columns = {"Engine HP": "HP", "Engine Cylinders": "Cylinders", 
                          "Transmission Type": "Transmission", "Driven_Wheels": "Drive Mode",
                          "highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Price"})
print(df.head(5))

# total number of rows and columns.
print(df.shape)

# rows containing duplicate data.
duplicate_rows_df = df[df.duplicated()]
print("Number of duplicate rows: ", duplicate_rows_df.shape)

# used to count the number of rows before removing the data.
print(df.count())

# dropping the duplicates.
df = df.drop_duplicates()
print(df.head(5))

# counting the number of rows after removing duplicates.
print(df.count())

# finding null values.
print(df.isnull().sum())

# dropping the missing values.
df = df.dropna()
print(df.count())

# after dropping the values.
print(df.isnull().sum())


sns.boxplot(x = df['Price'])
plt.show()

sns.boxplot(x = df['HP'])
plt.show()

sns.boxplot(x = df['Cylinders'])
plt.show()

# plotting a Histogram.
df.Make.value_counts().nlargest(35).plot(kind = 'bar', figsize = (10, 5))
plt.title("Number of cars by Make")
plt.xlabel("Make")
plt.ylabel("Number of cars")
# plt.xticks(rotation = 60)
plt.tight_layout()
plt.show()

# finding the relations between the variables.
plt.figure(figsize = (10, 5))
co_r = df.select_dtypes(include = "number").corr()
# mask = np.triu(np.ones_like(co_r, dtype = bool))
sns.heatmap(co_r, cmap = "BrBG", annot = True)
plt.tight_layout()
plt.show()

# plotting a scatter plot.
fig, ax = plt.subplots(figsize = (10, 5))
ax.scatter(df['HP'], df['Price'])
ax.set_xlabel('HP')
ax.set_ylabel('Price')
plt.show()