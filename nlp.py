import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer

import pandas as pd
import numpy as np

address = "D:/data_store_design_project/youtube_comments.csv"
df = pd.read_csv(filepath_or_buffer=address, header=None)

#Previewing the dataframe created 
print(df.head())
#Converting dataframe to a python list that can be loop through
comments_list = df.values.tolist()
#print(comments_list)




""" Since the .csv file contains 100 same comments I'll use one comment as a example """

comment = "Hate speech is usually thought to include communications of animosity or disparagement of an individual or a group on account of a group characteristic such as race  color  national origin  sex  disability  religion  or sexual orientation."

#Word Tokenizing (further sperate each element in the comments_list array into words)
comment_tk = word_tokenize(comment)
print(comment_tk, "\n")

#Removing stop words
sw = set(stopwords.words("english"))

#Loop through all words in the list, append to comment_tk_sw_removed if the word is not in sw list
comment_tk_sw_removed = [w for w in comment_tk if not w in sw]
print("The text after removing stop words: \n")
print(comment_tk_sw_removed, '\n')

#Stemming (Unify)
port_stem = PorterStemmer()
comment_tk_sw_removed_stemmed = []

for w in comment_tk_sw_removed:
    #Append to the list 
    comment_tk_sw_removed_stemmed.append(port_stem.stem(w))

print("Stemmed sentence: \n", comment_tk_sw_removed_stemmed, "\n")


#Lemmatizing (Simplify)
lem = WordNetLemmatizer()
comment_tk_sw_removed_stemmed_lem = []

for i in range(len(comment_tk_sw_removed_stemmed)):
    comment_tk_sw_removed_stemmed_lem.append(lem.lemmatize(comment_tk_sw_removed_stemmed[i]))

print("Lemmatized comment: \n" , comment_tk_sw_removed_stemmed_lem)


