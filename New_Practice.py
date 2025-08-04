import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.show()
sns.set_color_codes = True
data_frame = pd.read_csv("Exploratory data analysis\data.csv")
# print(data_frame.head())
# print(data_frame.tail(5))
# print(data_frame.dtypes)

# Columns: [Make, Model, Year, Engine Fuel Type, Engine HP, Engine Cylinders, Transmission Type, Driven_Wheels, 
#           Number of Doors, Market Category, Vehicle Size, Vehicle Style, highway MPG, city mpg, Popularity, MSRP]

data_frame = data_frame.drop(['Engine Fuel Type', 'Driven_Wheels', 'Number of Doors', 'Market Category', 'Vehicle Size', 'Vehicle Style'], axis = 1)
# print(data_frame.head(5))
data_frame = data_frame.rename(columns = {"Engine Cylinders": "Cylinders", "Transmission Type": "Transmission", 
                                          "Engine HP": "HP", "MSRP": "Price"})
# print(data_frame.head(5))
print("Number of rows: ", data_frame.shape)
# print(data_frame.count)
duplicate_rows_df = data_frame[data_frame.duplicated()]
print("Number of duplicate rows: ", duplicate_rows_df.shape)
# print(data_frame.count)
data_frame = data_frame.drop_duplicates()
# print(data_frame.head(5))
# print(data_frame.count)
print("Number of rows after dropping duplicates: ", data_frame.shape)
null_counts = data_frame.isnull().sum()
print("Number of null values: ", null_counts)
data_frame = data_frame.dropna()
null_counts_after = data_frame.isnull().sum()
print("Number of null values after dropping null values: ", null_counts_after)

# sns.boxplot(x = data_frame['Model'], y = data_frame["Year"])
# sns.boxplot(y = "HP", data = data_frame)
# sns.boxplot(x = data_frame['Cylinders'])
# plt.show()

# Histogram
# data_frame.Make.value_counts().nlargest(35).plot(kind = 'bar', figsize = (10, 5))
# plt.title("Number of cars by Make")
# plt.xlabel("Make")
# plt.ylabel("Number of cars")
# # plt.xticks(rotation = 60)
# plt.tight_layout()
# plt.show()

# scatter plot
# fig, axis = plt.subplots(figsize = (10, 5))
# axis.scatter(data_frame['MSRP'], data_frame['HP'])
# axis.set_xlabel("MSRP")
# axis.set_ylabel("HP")
# plt.tight_layout()
# plt.show()

# finding the relations between the variables
plt.figure(figsize = (10, 5))
co_r = data_frame.select_dtypes(include = "number").corr()
# mask = np.triu(np.ones_like(co_r, dtype = bool))
sns.heatmap(co_r, cmap = "BrBG", annot = True)
plt.tight_layout()
plt.show()