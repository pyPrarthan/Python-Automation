"""
This script automates the task of opening a webpage using Selenium WebDriver with Google Chrome.

## Components:
- **Website URL**: The URL to be opened (`https://www.thesun.co.uk/sport/football/`).
- **ChromeDriver Path**: Path to the `chromedriver.exe` file used to control the Chrome browser.

## Flow:
1. Import necessary modules.
2. Set the URL and ChromeDriver path.
3. Initialize the WebDriver and open the specified webpage.

Ensure `chromedriver.exe` is compatible with your Chrome version and correctly referenced in the path.
"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.thesun.co.uk/sport/football/"
path = r"C:\Users\anujc\Desktop\chromedriver-win64 (1)\chromedriver-win64/chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

containers = driver.find_elemenst(by="xpath", value='//div[@class="teaser__copy-container"]')

for container in containers:
    title = container.find_elemnt(by="xpath", value='./a/h3').text
    subtitle = container.find_elemnt(by="xpath", value='./a/p').text
    link = container.find_element(by='xpath', value='./a').get_attribute("href")