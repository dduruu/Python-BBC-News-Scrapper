# Python-BBC-News-Scrapper
A Python automation tool that extracts real-time headlines from BBC News using BeautifulSoup and Requests.

# About
This project is a basic web scraper designed to practice Python automation. It connects to BBC News and retrieves the latest 5 headlines directly to the console.

The application utilizes the **Requests** library for data retrieval and **BeautifulSoup** for parsing and extracting headlines from the HTML structure.

## How it works
1. Sends a request to BBC News with a User-Agent header.
2. Parses the HTML content of the page.
3. Identifies and extracts all `<h2>` tagged titles.
4. Filters and displays the top 5 results.

## Requirements
* Python 3
* `pip install beautifulsoup4 requests`
