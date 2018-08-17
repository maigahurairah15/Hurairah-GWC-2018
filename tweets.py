'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()


# Continue your program below!
polarity = []
subjectivity = []
# Textblob sample:
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)

for i in tweetData:
    text1= TextBlob(i["text"])
    subj = text1.sentiment.subjectivity
    subjectivity.append(subj)
    pol = text1.sentiment.polarity
    polarity.append(pol)
    print(polarity)
    print(subjectivity)
var1 = sum(polarity)
avg_1 = var1/len(polarity)
var2 = sum(subjectivity)
avg_2 = var2/len(subjectivity)
print(avg_1)
print(avg_2)

import matplotlib.pyplot as plt


plt.hist(polarity, bins=[-1, -0.5, 0.0, 0.5, 1])
plt.xlabel('polarity')
plt.ylabel('Number of tweets')
plt.title('Histogram of Numbers')
plt.axis([0, 1, 0, 100])
plt.grid(True)
plt.show()


plt.hist(subjectivity, bins=[-1, -0.5, 0.0, 0.5, 1])
plt.xlabel('subjectivity')
plt.ylabel('Number of tweets')
plt.title('Histogram of Numbers')
plt.axis([0, 1, 0, 100])
plt.grid(True)
plt.show()
