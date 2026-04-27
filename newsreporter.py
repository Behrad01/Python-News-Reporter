# importing modules
import requests
from bs4 import BeautifulSoup

scrape_range = 50   # variable for the number of reports to print

# adding headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

url = 'https://www.bbc.com/news'   # bbc news url
response = requests.get(url=url, headers=headers)   # sending connection request to url
soup = BeautifulSoup(response.text, 'html.parser')   # using BeautifulSoup to exctract texts from website

# validating connection
print('\n')
if response.status_code == 200: 
    print(' >  Response Successful' + '\n')   # announcing if connection was successful
else:
    print(' >  Response Unsuccessful' + '\n')

# declaring a variable for all news headers extracted from website
news = soup.find_all('h2')

# iterating over each news report
for index, news_report in enumerate(news, 1):
    # handling newsreports number limit
    if index > scrape_range:
        break

    try:
        article_url = news_report.find_parent('a')['href']   # variable for news article link
        full_url = 'https://www.bbc.com' + article_url   # adding article link to bbc news link to create a full url
    except TypeError:
        full_url = 'No link'   # 'No link' if there is no link to the article

    # changing article url to 'Live' if the article is a live broadcast
    if 'live' in full_url:   
        full_url = 'Live'

    # printing the number of each news report alongside with the full article url
    print(f'{index:2}. {news_report.text} ( {full_url} )\n')
