import sys
from textblob import TextBlob

if __name__ == '__main__':
    for line in sys.stdin:
        blob = TextBlob(line)
        print(blob.sentiment.polarity, file=sys.stdout)
