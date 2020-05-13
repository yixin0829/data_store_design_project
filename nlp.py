import nltk
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np

address = "D:/data_store_design_project/youtube_comments.csv"
df = pd.read_csv(filepath_or_buffer=address, header=None)

#Previewing the dataframe created 
print(df.head())
#Converting dataframe to a python list
comments_list = df.values.tolist()
print(comments_list)

#Word Tokenizing (further sperate each element in the comments_list array into words)

#Removing stop words

#Stemming

#Lemmatizing

#Logistic regression
