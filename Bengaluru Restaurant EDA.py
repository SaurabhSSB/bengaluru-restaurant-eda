# perform linear operations
import numpy as np
# Data manipulation
import pandas as pd
# Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns
# Remove warnings
import warnings
warnings.filterwarnings('ignore')

# Load the dataset
df = pd.read_csv(r"C:\Users\Lenovo\Documents\jupyter\DataSets\zomato.csv")
# Print top 5 rows
df.head()

# check for shape
df.shape

# Check info of each colummn
df.info()

# Checking null values
df.isnull().sum()

# check for duplicate
df.duplicated().sum()

df.columns

# Drop columns
df1 = df.drop(columns=['url', 'address', 'phone'])
df1.head()

# Rename Columns
df1.rename(columns={'approx_cost(for two people)': 'cost', 'listed_in(type)': 'service', 'listed_in(city)': 'city'}, inplace=True)
df1

# Check for null values
df1.isna().sum()

# create a threshold of our data
threshold = len(df1) * 0.05
threshold

cols_to_drop = df1.columns[df1.isna().sum() <= threshold]
cols_to_drop

# Dropping null values
df1.dropna(subset=cols_to_drop, inplace=True)

# again check for null values
df1.isna().sum()

df1.dish_liked.mode()
df1.dish_liked.fillna('Biryani', inplace=True)
df1.rate.unique()

df1['rate'] = df1['rate'].str.strip('-')
df1['rate'] = df1['rate'].str.strip('NEW')
df1['rate'] = df1['rate'].str.replace('/5', '')
df1['rate'] = df1['rate'].str.replace(' ', '')
df1['rate'].unique()

df1.rate = pd.to_numeric(df1.rate)
df1.rate.fillna(df1.rate.mean(), inplace=True)
df1.isna().sum()

df1.info()

df1.cost.unique()

df1.cost = df1.cost.str.replace(",", "")
df1.cost = df1.cost.astype(int)
df1.cost.unique()

df1.cost.dtype

df1.votes = pd.to_numeric(df1.votes)
df1.votes

df1
x = df1["online_order"].value_counts()
y = x.index
plt.pie(x=x, labels=y, colors=['lightcoral', 'lightskyblue'], autopct='%.0f%%', explode=(0, 0.1), shadow=True)
plt.title("Online order Percentage", color="black")

x = df1["book_table"].value_counts()
y = x.index
plt.pie(x=x, labels=y, colors=['#99ff99', '#ffcc99'], autopct='%.0f%%', explode=(0, 0.1), shadow=True)
plt.title("Table Booking ratio", color="black")

sns.set_style('darkgrid')
sns.barplot(data=df1, x='book_table', y='rate')
plt.show()

df1.location.unique()

x = df1.groupby('location')[['rate', 'votes']].mean()
x.sort_values(by=['rate', 'votes'], ascending=False)
x = x.head(10)
l = x.index.to_list()
x

sns.barplot(x=x.index, y=x.rate, data=x, palette='magma')
plt.xticks(rotation=90)
plt.title("Best location by rating")
plt.show()

sns.barplot(x=x.index, y=x.votes, data=x, palette='viridis')
plt.xticks(rotation=90)
plt.title("Best location by votes")
plt.show()

plt.figure(figsize=(15, 6))
sns.scatterplot(x=df1.location, y=df1.rate)
plt.xticks(rotation=90)
plt.show()

df1.head(2)
df1.rest_type.unique()

top_rest_by_rating = df1.groupby('rest_type')['rate'].max().sort_values(ascending=False).head(10)
top_rest_by_rating

plt.figure(figsize=(8, 6))
plt.barh(top_rest_by_rating.index, top_rest_by_rating, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
])
plt.title("Top 10 rest type by rating")
plt.xticks(rotation=90)
plt.show()

df1.service.unique()

sns.countplot(x="service", data=df1)
plt.title("Types of services")
plt.xticks(rotation=60)
plt.show()

service_type = df1.groupby('service')[['rate']].mean().sort_values(by=['rate'], ascending=False).head(10)
service_type

color = ['#d62728', '#9467bd', '#8c564b', '#17becf', '#e377c2', '#7f7f7f', '#bcbd22']
sns.set_palette(color)
sns.barplot(x=service_type.index, y='rate', data=service_type)
plt.xticks(rotation=90)
plt.title("Top services by rating")
plt.show()

df1.head(2)
df1.name.value_counts().sort_values(ascending=False)

df1.cost.unique()

expensive_restaurant = df1.groupby('name')['cost'].max().sort_values(ascending=False).head(10)
expensive_restaurant

sns.barplot(x=expensive_restaurant.index, y=expensive_restaurant)
plt.xticks(rotation=90)
plt.title("Top 10 expensive restaurant")
plt.show()

df1.head(2)
no_of_rest = df1.location.value_counts().head(10)
no_of_rest

sns.barplot(x=no_of_rest.index, y=no_of_rest, palette='colorblind')
plt.xticks(rotation=90)
plt.title("Top 10 location by number of restaurant")
plt.show()
