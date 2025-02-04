from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
import mysql.connector

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",       
    user="root",    
    password="password",  
    database="company_data"
)
cursor = db.cursor()

# Func to insert data into DB
def insert_into_db(name, location, phone, website):
    sql = """INSERT INTO companies (name, location, phone, website) VALUES (%s, %s, %s, %s)"""
    values = (name, location, phone, website)
    cursor.execute(sql, values)
    db.commit()

chrome_options = Options()
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--window-size=1920,1080")

BASE_URL = r'https://www.gelbeseiten.de/suche/geb%c3%a4udereinigung/bundesweit'
driver = webdriver.Chrome(options=chrome_options)
driver.get(BASE_URL)
sleep(1)

try:
    element = driver.find_element(By.ID, 'cmpbntyestxt')
    sleep(1)
    element.click()
    print('Clicked on accept cookies button!')
    
except Exception as e:
    print('Can not locate element: ', e)

for _ in range(40):
    load_more = driver.find_element(By.ID, 'mod-LoadMore--button')
    load_more.click()
    sleep(2)
    
print('Done scrolling.')
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
driver.quit()

companies = soup.findAll('article', {'class':'mod mod-Treffer'})
print(f'Number of companies: {len(companies)}')
print()

names = []
locations = []
numbers = []
urls = []
for index, company in enumerate(companies, start=1):
    # Extract company name
    company_name = company.find('h2', {'class': 'mod-Treffer__name'})
    name_text = company_name.get_text(strip=True) if company_name else 'N/A'
    names.append(name_text)

    # Extract location
    location = company.find('div', {'class': 'mod-AdresseKompakt__adress-text'})
    location_text = location.get_text(strip=True).replace('(', ' (') if location else 'N/A'
    locations.append(location_text)

    # Extract phone number
    phone_number = company.find('div', {'class': 'mod-TelefonnummerKompakt'})
    phone_text = phone_number.get_text(strip=True).replace(' ', '') if phone_number else 'N/A'
    numbers.append(phone_text)

    # Extract website URL
    url_tag = company.find('a')
    url_text = url_tag.get('href', 'N/A') if url_tag else 'N/A'
    urls.append(url_text)

    # Insert data into DB
    insert_into_db(name_text, location_text, phone_text, url_text)

    # Print company details
    print(f'--- Company {index} Details ---')
    print(f'Name: {name_text}')
    print(f'Location: {location_text}')
    print(f'Phone: {phone_text}')
    print(f'Website URL: {url_text}\n')
