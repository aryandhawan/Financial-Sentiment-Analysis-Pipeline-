import pandas as pd
import numpy as np
import json
tickers = ["RELIANCE.BSE", "TCS.BSE", "HDFCBANK.BSE", "TATAMOTORS.BSE",'SUNPHARMA.BSE']
data_to_extract='Weekly Time Series'
all_dfs=[]

for tick in tickers:
    filename=f'{tick}_weekly_data.json'

    with open(filename,'r') as f:
        data = json.load(f)

    raw_data=data[data_to_extract]

    tick_dataframe=pd.DataFrame.from_dict(raw_data,orient='index')
    tick_dataframe['ticker']=tick
    all_dfs.append(tick_dataframe)

print("Done for stock data!")


master_df = pd.concat(all_dfs)

master_df.index = pd.to_datetime(master_df.index)
master_df_numerical = master_df.astype({'1. open': float, '2. high': float, '3. low': float, '4. close': float, '5. volume': float})



print("------------Now we work to combine news data------------")

tickers_news = ["RELIANCE.BSE", "TCS.BSE", "HDFCBANK.BSE"]

for tick in tickers_news:
    filename=f'{tick}_news_raw.json'

    with open(filename,'r') as f:
        data=json.load(f)

    raw_data=data['feed'] # main key for news data
    news_list=[]
    for news_item in raw_data:
        news_dict={}
        news_dict['ticker']=tick
        news_dict['title']=news_item['title']
        news_dict['summary']=news_item['summary']
        news_dict['time_published']=news_item['time_published'][:8]
        news_dict["overall_sentiment_score"]=news_item['overall_sentiment_score']
        news_dict['overall_sentiment_label']=news_item['overall_sentiment_label']
        news_list.append(news_dict)

    news_df=pd.DataFrame(news_list)
    news_df['time_published']=pd.to_datetime(news_df['time_published'])

print('Done for news data!')

master_df_numerical.to_csv("master_df_numerical.csv",index=True)

news_df.to_csv("master_df_news.csv",index=False)

print("Done saving the data!")