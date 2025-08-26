

# Simple Web Scraper

A Python script that scrapes quotes from [http://quotes.toscrape.com](http://quotes.toscrape.com) and saves them to a CSV file.

## Features
- Scrapes quotes, authors, and tags from a public website
- Handles pagination to collect multiple pages of data
- Saves extracted data to a CSV file
- Includes error handling for network issues
- Respectful scraping with delays between requests

## Requirements
- Python 3.x
- Required libraries: `requests`, `beautifulsoup4`, `lxml`

## Installation
1. Install required packages:
```bash
pip install requests beautifulsoup4 lxml
```

2. Save the code to a file named `web_scraper.py`

## Usage
1. Run the script:
```bash
python web_scraper.py
```

2. The script will:
   - Scrape quotes from the website
   - Save them to `quotes.csv`
   - Display progress messages

3. After completion, you'll find a CSV file with the following columns:
   - Quote
   - Author
   - Tags
## Key Features Explained
1. **Web Scraping**:
   - Uses `requests` to fetch web pages
   - Parses HTML with `BeautifulSoup` and `lxml` parser
   - Extracts quotes, authors, and tags from structured HTML

2. **Pagination Handling**:
   - Automatically follows "Next" links to scrape multiple pages
   - Continues until no more pages are available

3. **Data Storage**:
   - Saves data to CSV file with proper formatting
   - Includes headers and handles special characters with UTF-8 encoding

4. **Error Handling**:
   - Catches network request errors
   - Handles general exceptions gracefully
   - Provides informative error messages

5. **Respectful Scraping**:
   - Adds random delays between requests (1-3 seconds)
   - Avoids overwhelming the target server

## Sample Output (quotes.csv)
```csv
Quote,Author,Tags
"The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.","Albert Einstein","change,deep-thoughts,thinking,world"
"It is our choices, Harry, that show what we truly are, far more than our abilities.","J.K. Rowling","abilities,choices,inspirational"
...
```

## Ethical Considerations
1. **Check robots.txt**: Always check a website's robots.txt file before scraping
2. **Rate Limiting**: Avoid sending too many requests in a short time
3. **Terms of Service**: Respect the website's terms of service
4. **Public Data Only**: Only scrape publicly available information
5. **Identify Yourself**: Set a proper User-Agent header if needed

## Future Enhancements
- Add command-line arguments for customization
- Implement proxy rotation for large-scale scraping
- Add data cleaning and processing features
- Support for multiple output formats (JSON, XML)
- Add progress bar for long scraping tasks
- Implement concurrent scraping with threading

