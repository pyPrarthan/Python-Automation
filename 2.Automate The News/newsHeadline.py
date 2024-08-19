from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

website = "https://www.thesun.co.uk/sport/football/"
path = r"C:\Users\anujc\Desktop\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

try:
    driver.get(website)
    
    # Explicit wait to ensure elements are loaded
    wait = WebDriverWait(driver, 10)
    containers = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="teaser__copy-container"]')))
    
    titles = []
    subtitles = []
    links = []

    for container in containers:
        try:
            title = container.find_element(By.XPATH, './a/h3').text
            subtitle = container.find_element(By.XPATH, './a/p').text
            link = container.find_element(By.XPATH, './a').get_attribute("href")

            titles.append(title)
            subtitles.append(subtitle)
            links.append(link)
        except Exception as e:
            print(f"Error extracting data from container: {e}")

    my_dict = {'Titles': titles, 'Subtitles': subtitles, 'Links': links}
    df_headline = pd.DataFrame(my_dict)

    print("Current Working Directory:", os.getcwd())
    print("Saving to CSV...")
    df_headline.to_csv('headline.csv', index=False)
    print("CSV file saved.")
    
finally:
    driver.quit()
