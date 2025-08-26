import requests
from bs4 import BeautifulSoup
import csv
import time
import random

def scrape_quotes(url):
    """Scrape quotes from a given URL"""
    quotes_data = []
    
    while url:
        try:
            # Add random delay to be respectful to the server
            time.sleep(random.uniform(1, 3))
            
            # Send HTTP request
            response = requests.get(url)
            response.raise_for_status()  # Raise exception for bad status codes
            
            # Parse HTML content
            soup = BeautifulSoup(response.text, 'lxml')
            
            # Find all quote containers
            quotes = soup.find_all('div', class_='quote')
            
            for quote in quotes:
                # Extract quote text
                text = quote.find('span', class_='text').get_text(strip=True)
                
                # Extract author
                author = quote.find('small', class_='author').get_text(strip=True)
                
                # Extract tags
                tags = [tag.get_text(strip=True) for tag in quote.find_all('a', class_='tag')]
                tags_str = ', '.join(tags)  # Convert list to comma-separated string
                
                # Store data
                quotes_data.append({
                    'Quote': text,
                    'Author': author,
                    'Tags': tags_str
                })
            
            # Check for next page
            next_page = soup.find('li', class_='next')
            url = f"http://quotes.toscrape.com{next_page.find('a')['href']}" if next_page else None
            
            print(f"Scraped {len(quotes)} quotes from current page")
            
        except requests.exceptions.RequestException as e:
            print(f"Error during requests: {e}")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break
    
    return quotes_data

def save_to_csv(data, filename):
    """Save scraped data to CSV file"""
    if not data:
        print("No data to save")
        return
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Quote', 'Author', 'Tags']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for item in data:
                writer.writerow(item)
        
        print(f"Successfully saved {len(data)} quotes to {filename}")
    
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def main():
    """Main function to run the scraper"""
    base_url = "http://quotes.toscrape.com"
    output_file = "quotes.csv"
    
    print("Starting web scraper...")
    print(f"Target URL: {base_url}")
    print(f"Output file: {output_file}")
    
    quotes_data = scrape_quotes(base_url)
    
    if quotes_data:
        save_to_csv(quotes_data, output_file)
    else:
        print("No quotes were scraped")
    
    print("Scraping completed")

if __name__ == "__main__":
    main()
