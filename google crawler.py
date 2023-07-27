#forty by croc100
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def google_search_crawler(keyword):
    # Calculate the date range for the last 5 days.
    today = datetime.now()
    five_days_ago = today - timedelta(days=5)
    formatted_today = today.strftime('%Y-%m-%d')
    formatted_five_days_ago = five_days_ago.strftime('%Y-%m-%d')

    # Construct the Google search results page URL.
    search_url = f'https://www.google.com/search?q={keyword}&tbs=qdr:d,sbd:1&source=lnt&sa=X&ved=0ahUKEwiNh_eTzZPnAhXMUd4KHd3rDp0QpwUIIw&biw=1366&bih=657'

    # Send an HTTP request to get the search results page.
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract links, titles, and dates from the search results.
    results = soup.find_all('div', class_='tF2Cxc')
    for result in results:
        link = result.a['href']
        title = result.a.text
        date_str = result.find('span', class_='f').text

        # Check if the date is within the last 5 days.
        date = datetime.strptime(date_str, '%b %d, %Y')
        if date >= five_days_ago:
            print(f'Title: {title}')
            print(f'Link: {link}')
            print(f'Date: {date.strftime("%Y-%m-%d")}')
            print('-' * 50)

# Prompt the user to enter the search keyword and start crawling.
search_keyword = input("Enter the keyword to search: ")
google_search_crawler(search_keyword)
