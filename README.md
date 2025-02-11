# Web Scraper & User Interface for Company Data (Selenium + BeautifulSoup + Django + MySQL)

## Overview
This project involves extracting business data from [GelbeSeiten](https://www.gelbeseiten.de/suche/geb%c3%a4udereinigung/bundesweit) to collect information on **2,000 cleaning companies across Germany**. The extracted data is stored in a **MySQL database** and can be accessed through a **Django-based web interface**.

## Data to be Collected
- **Company Name**
- **Location** (Address, City, Zip Code)
- **Phone Number**
- **Website URL** (if available)

## Features
✅ **Automated Web Scraping** using **Selenium** and **BeautifulSoup**

✅ **Headless Mode** for faster and background execution

✅ **MySQL Integration** to store extracted data

✅ **Django Web Interface** for viewing and managing company data

✅ **Django REST Framework API** for accessing data via endpoints

✅ **Bootstrap Styling** for a responsive UI

✅ **Error Handling** for missing elements and database failures

✅ **Pagination Handling** to navigate all pages and collect complete data

✅ **Duplicate Removal** to ensure data accuracy

✅ **Bypass Anti-Scraping Mechanisms** if necessary

## Prerequisites
Before running the script and UI, ensure you have the following installed:

### 1. Install Python Packages
```sh
pip install selenium beautifulsoup4 mysql-connector-python django djangorestframework
```

### 2. Download WebDriver
- **Google Chrome**: Download [Chromedriver](https://chromedriver.chromium.org/downloads) that matches your Chrome version.
- **Place the Chromedriver executable** in a known path and update the script if needed.

### 3. Setup MySQL Database
#### Create Database and Table
Run the following SQL commands in MySQL:
```sql
CREATE DATABASE IF NOT EXISTS company_data;

USE company_data;

CREATE TABLE IF NOT EXISTS companies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    phone VARCHAR(50),
    website VARCHAR(255)
);
```

## Configuration
Before running the script, update the **MySQL credentials** in the Python script:
```python
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="company_data"
)
```

## Running the Scraper
To start the scraper, run:
```sh
python scraper.py
```

## Running the Django Web Interface
### 1. Navigate to the Django Project Directory
```sh
cd your_django_project
```

### 2. Apply Migrations and Start the Server
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 3. Access the Web Interface
Open a browser and visit:
```
http://127.0.0.1:8000/
```

## API Endpoints (Django REST Framework)
The Django backend exposes RESTful endpoints:
- List all companies: `GET /api/companies/`
- Retrieve a specific company: `GET /api/companies/{id}/`

The script will:
1. Open the website in **headless Chrome**
2. Accept cookies if required
3. Scroll and **click 'Load More'** to extract more data
4. Navigate through **all pagination pages**
5. Parse and store company details in **MySQL**
6. Display the data in a **Django web interface**
7. Provide API access via Django REST Framework


## Troubleshooting
- **Chromedriver Version Mismatch**: Ensure your **ChromeDriver version matches your browser version**.
- **MySQL Connection Error**: Verify your **username, password, and database name**.
- **Website Changes**: If the website structure changes, update the **CSS selectors** accordingly.
- **Django Returns No Data**: Ensure the correct **table name** is set in `models.py`.

## Ideal Candidate for This Project
- **Proficient in Python** (Scrapy, BeautifulSoup, Selenium, or Requests)
- **Experience with Web Automation** and **bypassing bot protections**
- **Strong knowledge of Data Cleaning and Structuring**

---
🚀 Happy Scraping & Web Development!

