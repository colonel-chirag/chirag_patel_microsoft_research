from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Initialize the Chrome WebDriver service
driver_service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=driver_service)

# Lists to store scraped data and report success/failure
news_articles = []
success = []
failure = []
scrapers_report = []
link = []

# Define a function to scrape a specific website
def scrape_website(url, base_url, name):
    try:
        # Visit the URL
        driver.get(url)
        time.sleep(3)
        
        # Parse HTML content
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Find all links within the specified class
        results = soup.find(class_='arrow_list').find_all('a')
        
        # Iterate through found links
        for i in results:
            headline = i.text.strip()  # Extract headline
            link = i['href']  # Extract link
            
            # Check if the link is relative, if so, make it absolute
            if "http" not in link:
                link = base_url + link
            
            # Append extracted data to news_articles list
            news_articles.append((name, headline, link))
        
        # If successful, append to success list
        success.append(name)
    
    except Exception as e:
        # If an exception occurs, append the name and exception to failure list
        failure.append((name, e))
        pass

# Define the URL, base URL, and name of the website to be scraped
url = "https://hnbgu.ac.in"
base_url = url
name = 'HNBGU'
scrapers_report.append([url, base_url, name])

# Call the scraping function for HNBGU website
scrape_website(url, base_url, name)

# Quit the WebDriver
driver.quit()

# Print the scraped news articles and the count of articles
print(news_articles)
print(len(news_articles))
