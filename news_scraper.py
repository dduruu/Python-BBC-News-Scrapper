import requests
from bs4 import BeautifulSoup

# Target website (You can change this)
url = "https://www.bbc.com/news"

# Using a User-Agent to access the website & avoid getting blocked
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

# Making the HTML code readable
soup = BeautifulSoup(response.text, 'html.parser')

# Finding all headlines tagged with <h2>
headlines = soup.find_all('h2')

# Printing the top 5 titles
print("--- CURRENT BBC TOP HEADLINES ---")
for headline in headlines[:5]:
    print(f"- {headline.text.strip()}")