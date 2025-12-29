import requests
import json
API_Key='YOUR API KEY HERE'
#
# url_india=f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=RELIANCE.BSE&outputsize=full&apikey=f{API_Key}'
# response=requests.get(url=url_india)
#
#
tickers = ["RELIANCE.BSE", "TCS.BSE", "HDFCBANK.BSE", "TATAMOTORS.BSE",'SUNPHARMA.BSE','ITC.BSE']

for ticker in tickers:
    response = requests.get(f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&symbol={ticker}&outputsize=full&apikey=f{API_Key}')
    data = response.json()
    with open(f'{ticker}_news_raw.json', 'w') as f:
        json.dump(data, f, indent=4)

print("Done!")


