from operator import ne
from re import sub
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib



netflix_df=pd.read_csv('netflix_titles.csv')
#print(netflix_df)

#print(netflix_df.head())


#Data Preparation and Cleaning 

#print(netflix_df.info())

#print(netflix_df.nunique())



#Handling Null Values 

#print(netflix_df.isnull().values.any())

#print(netflix_df.isnull().sum())
#print(netflix_df.isnull().sum().sum())


#sns.heatmap(netflix_df.isnull(),cbar=False)
#plt.title("Null Value Heatmap")
#plt.show()



netflix_df['director'].fillna("No Director",inplace=True)
netflix_df['cast'].fillna("No Cast",inplace=True)
netflix_df['country'].fillna("Country Unavailable",inplace=True)
netflix_df.dropna(subset=['date_added','rating'],inplace=True)


#print(netflix_df.isnull().any())



#spliting the Dataset 

#netflix_df=netflix_df[netflix_df['type']=='Movie'].copy()
#print(netflix_df.head(2))


#netflix_shows_df=netflix_df[netflix_df['type']=='TV Show'].copy()
#print(netflix_shows_df)

#Exploratory analysis and visualization
plt.figure(figsize=(7,5))
g=sns.countplot(netflix_df.type,palette="pastel")
plt.title("Count of Movies and TV Shows")
plt.xlabel("Type(Movie/TV Show)")
plt.ylabel("Total Count")
plt.show()


plt.figure(figsize=(12,6))
plt.title("% of Netflix Titles that are either Movies or TV Shows")
g = plt.pie(netflix_df.type.value_counts(), explode=(0.025,0.025), labels=netflix_df.type.value_counts().index, colors=['skyblue','navajowhite'],autopct='%1.1f%%', startangle=180);
plt.legend()
plt.show()



order =  ['G', 'TV-Y', 'TV-G', 'PG', 'TV-Y7', 'TV-Y7-FV', 'TV-PG', 'PG-13', 'TV-14', 'R', 'NC-17', 'TV-MA']
plt.figure(figsize=(15,7))
g = sns.countplot(netflix_df.rating, hue=netflix_df.type, order=order, palette="pastel");
plt.title("Ratings for Movies & TV Shows")
plt.xlabel("Rating")
plt.ylabel("Total Count")
plt.show()







