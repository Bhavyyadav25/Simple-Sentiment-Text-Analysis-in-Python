from textblob import TextBlob
from newspaper import Article

# url = 'https://www.theguardian.com/media/2004/oct/12/pressandpublishing.broadcasting'
# article = Article(url)
#
# article.download()
# article.parse()
# article.nlp()
#
# text = article.summary
# print(text)

with open("mytest.txt", 'r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)
if sentiment > 0:
    print("It's a positive article.")
else:
    print("It's a negative article.")