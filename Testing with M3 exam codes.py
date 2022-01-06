# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 21:26:34 2021

@author: Kestra
"""

#%%
#Importing relevant libraries for exploration
import pandas as pd
#%%
#Downloading dataset

review = pd.read_csv(r"C:\Users\kesut\Desktop\fake.csv")

#%%
#Exploring the dataset
review

#%%
#Checking the number of entries by label (OR: real reviews, CG: computer-generated fake reviews)
review["label"].value_counts()

#%%
#Checking the categories of reviews
review["category"].value_counts()

#%%
#Looking for missing values in every column
review.isnull().sum(axis = 0)

#%%
#Making them all lower-case
review["text_clean"] = review["text_"].str.lower()

#%%
#Using gensim library to remove punctuation, extra white spaces, stopwords, etc.
from gensim.parsing.preprocessing import remove_stopwords

#%%
#Defining the function for removing stopwords
def stopword_removal(row):
  text = row["text_clean"]
  text = remove_stopwords(text)
  return text

#%%
#Removing all stopwords from text_clean
review["text_clean"] = review.apply(stopword_removal, axis=1)

#%%
#Removing extra punctuation (! comma period)
review["text_clean"] = review["text_clean"].str.replace("!", "").str.replace(",", "").str.replace(".", "")

#%%
#Renaming the labels with 0: Original Review and 1: Computer-generated review
review["label"].replace({"OR": "0", "CG": "1"}, inplace=True)

#%%
#Importing library for lemmatization
import spacy
nlp = spacy.load("en_core_web_sm")

#%%
#Creating a new column with the lemmatized text
#NOTE: takes about 7 minutes
review["lemmatized"] = review["text_clean"].apply(lambda x: " ".join(
    [y.lemma_ for y in nlp(x)]))

#%%
#Creating token from the cleaned text
#NOTE: Takes about 3 minutes
tokens = []

for lemmatized in nlp.pipe(review["lemmatized"]):
  tokenized = [token.lemma_.lower() for token in lemmatized if token.pos_ in 
               ["NOUN", "PROPN", "ADJ", "ADV"] and not token.is_stop]
  tokens.extend(tokenized)
  
#%%
#Creating a dictionary of the tokens (creating a list of words that are used in the text)
dictionary = list(set(tokens))

#%% 
#Showing a sample of the tokens
tokens[:20]

#%%
#Using TF-IDF vectorizer 
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(vocabulary=dictionary) 
 
X = vectorizer.fit_transform(review["lemmatized"])

#%%
#To split the dataset into the test and training
from sklearn.model_selection import train_test_split 

#Metrics to see the accuracy of the models
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer

#SML classification models
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

#%%
#Setting the X and y values
#NOTE: X is the vectorized reviews in the previous section
#y = the labels (real or fake review)

y = review["label"]

#%%
#Splitting the test data and the training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 21)

#%%
# Decision Tree Classifier
classifier_dt = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier_dt.fit(X_train, y_train)

#%%
# Overall score of Decision tree
classifier_dt.score(X_test, y_test)

#%%

