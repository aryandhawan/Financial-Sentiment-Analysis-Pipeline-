import pandas as pd
from sklearn.metrics import classification_report


df_analysed = pd.read_csv("master_news_analysed.csv") 


label_mapping = {
    "Bullish": "positive",
    "Somewhat-Bullish": "positive",
    "Somewhat-Bearish": "negative",
    "Bearish": "negative",
    "Neutral": "neutral",
}

df_analysed['alpha_vantage_normalized'] = df_analysed['overall_sentiment_label'].map(label_mapping)

df_analysed = df_analysed.dropna(subset=['alpha_vantage_normalized', 'finbert_label'])


df_analysed['match'] = df_analysed['alpha_vantage_normalized'] == df_analysed['finbert_label']


accuracy = df_analysed['match'].mean()
print(f"--- Agreement Rate: {accuracy:.2%} ---\n")

print("--- Detailed Report ---")
print(classification_report(df_analysed['alpha_vantage_normalized'], df_analysed['finbert_label']))

print("\n--- Top Disagreements ---")
disagreements = df_analysed[~df_analysed['match']]
if not disagreements.empty:
    print(disagreements[['summary', 'alpha_vantage_normalized', 'finbert_label']].head(3))
else:
    print("Incredible! They agree on everything.")