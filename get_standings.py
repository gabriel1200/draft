
import plotly.graph_objs as go
import plotly.io as pio
import pandas as pd
import string
from bs4 import BeautifulSoup
from pathlib import Path
import requests
import time
def pull_data(url):
    headers = {
                                    "Host": "stats.nba.com",
                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
                                    "Accept": "application/json, text/plain, */*",
                                    "Accept-Language": "en-US,en;q=0.5",
                                    "Accept-Encoding": "gzip, deflate, br",

                                    "Connection": "keep-alive",
                                    "Referer": "https://stats.nba.com/"
                                }
    json = requests.get(url,headers = headers).json()
    
    data = json["resultSets"][0]["rowSet"]
    columns = json["resultSets"][0]["headers"]
    df = pd.DataFrame.from_records(data, columns=columns)
    return df
url='https://stats.nba.com/stats/leaguestandingsv3?GroupBy=conf&LeagueID=00&Season=2024-25&SeasonType=Regular%20Season&Section=overall'

df = pull_data(url)
df.to_csv('2025_standings.csv')

small=df[['TeamID','WINS','LOSSES','TeamName','Conference','WinPCT' ]]
small.to_csv('2025_standings_small.csv')