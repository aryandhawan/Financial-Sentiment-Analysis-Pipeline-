import pandas as pd
from transformers import pipeline
from tqdm import tqdm
model_name='ProsusAI/finbert'

print(f"loading {model_name}")


sentiment_pipe=pipeline("sentiment-analysis",model=model_name)

print("model ready!")

try:
    df=pd.read_csv("master_df_news.csv")
    print("News DF loaded!")
except FileNotFoundError:
    print("No new news data")
    exit()

df=df.dropna(subset=['summary'])

ai_labels=[]
ai_scores=[]

# now we will anaylise the summary via this pre-trained model

print("Starting inference")

for text in tqdm(df["summary"]):
    try:
        result=sentiment_pipe(text,truncation=True,max_length=512)[0]
        ai_labels.append(result["label"])
        ai_scores.append(result["score"])
    except Exception as e:
        print(f"Error processing text{e}")
        ai_labels.append(None)
        ai_scores.append(0.00)

df['finbert_label']=ai_labels
df['finbert_score']=ai_scores

output_file="master_news_analysed.csv"
df.to_csv(output_file,index=False)

print(f"\n✅ Analysis Complete! Saved to {output_file}")

print("\n--- Reality Check (First 5 Rows) ---")
print(df[['ticker', 'overall_sentiment_label', 'finbert_label', 'finbert_score']].head())