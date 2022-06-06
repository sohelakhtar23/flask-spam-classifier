from socket import MsgFlag
import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import recall_score, precision_score, f1_score


DATA_JSON_FILE = 'email-text-data.json'
data = pd.read_json(DATA_JSON_FILE)

global vectorizer
global classifier

vectorizer = CountVectorizer(stop_words='english')

all_features = vectorizer.fit_transform(data.MESSAGE)

X_train, X_test, y_train, y_test = train_test_split(all_features, data.CATEGORY, 
                                                   test_size=0.3, random_state=88)
classifier = MultinomialNB()        
classifier.fit(X_train, y_train)

# example = ['get viagra for free now!', 
#           'need a mortgage? Reply to arrange a call with a specialist and get a quote', 
#           'Could you please help me with the project for tomorrow?', 
#           'Hello Jonathan, how about a game of golf tomorrow?', 
#           'Ski jumping is a winter sport in which competitors aim to achieve the longest jump after descending from a specially designed ramp on their skis. Along with jump length, competitor\'s style and other factors affect the final score. Ski jumping was first contested in Norway in the late 19th century, and later spread through Europe and North America in the early 20th century. Along with cross-country skiing, it constitutes the traditional group of Nordic skiing disciplines.'
#           ]
# matrix = vectorizer.transform(example)
# print(classifier.predict(matrix))

msg = 'get viagra for free now!'

def email_prediction(msg):
    matrix = vectorizer.transform([msg])

    return classifier.predict(matrix)[0]

print(email_prediction(msg))