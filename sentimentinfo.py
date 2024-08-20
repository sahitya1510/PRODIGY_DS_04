import pandas as pd
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Post': [
        'I love the new product! Absolutely fantastic experience.',
        'The service was terrible. I will never come back!',
        'I am not sure how I feel about the update.',
        'Great customer service and friendly staff!',
        'This product is not worth the price.',
        'I had an okay experience, nothing special.',
        'Amazing quality! Will definitely recommend.',
        'Worst purchase ever. Totally disappointed.',
        'I am so happy with the new features!',
        'The product is just average. Could be better.',
    ]
}

df = pd.DataFrame(data)

def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

df['Sentiment'] = df['Post'].apply(get_sentiment)

sns.countplot(x='Sentiment', data=df, palette='viridis')
plt.title('Sentiment Distribution in Social Media Posts')
plt.xlabel('Sentiment')
plt.ylabel('Number of Posts')
plt.show()

df['Date'] = pd.date_range(start='2024-08-01', periods=len(df), freq='D')
df['Sentiment Score'] = df['Post'].apply(lambda text: TextBlob(text).sentiment.polarity)

plt.figure(figsize=(10, 5))
sns.lineplot(x='Date', y='Sentiment Score', data=df, marker='o')
plt.title('Sentiment Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sentiment Score')
plt.show()
