# import os
# os.system('cls')

from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # sentiment = blob.sentiment
    # polarity = sentiment.polarity

    if polarity > 0:
        sentiment_category = 'Positive'
        color = 'green'
    elif polarity < 0:
        sentiment_category = 'Negative'
        color = 'red'
    else:
        sentiment_category = 'Natural'
        color = 'yellow'

    return sentiment_category, color

@app.route('/', methods=['get', 'Post'])
def index():
    sentiment = None
    color = None

    if request.method == 'Post':
        text = request.form['text']
        sentiment = analyze_sentiment(text)
    return render_template('index.html', sentiment = sentiment, color = color)

if __name__ == '__main__':
    app.run(debug=True)
