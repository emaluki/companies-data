# Web Scraper for Company Data (Selenium + BeautifulSoup + MySQL)

## Overview
This project is a web scraper that extracts company details such as **name, location, phone number, and website URL** from [GelbeSeiten](https://www.gelbeseiten.de). The extracted data is then stored in a **MySQL database**.

## Features
✅ **Automated Web Scraping** using **Selenium** and **BeautifulSoup**
✅ **Headless Mode** for faster and background execution
✅ **MySQL Integration** to store extracted data
✅ **Error Handling** for missing elements and database failures
✅ **Efficient Scrolling** to load more data dynamically

## Prerequisites
Before running the script, ensure you have the following installed:

### 1. Install Python Packages
```sh
pip install selenium beautifulsoup4 mysql-connector-python
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

## Running the Script
To start the scraper, run:
```sh
python scraper.py
```

## Expected Output
The script will:
1. Open the website in **headless Chrome**
2. Accept cookies if required
3. Scroll and **click 'Load More'** to extract more data
4. Parse and store company details in **MySQL**
5. Print extracted details in the console

Example output:
```sh
--- Company 1 Details ---
Name: ABC Cleaning Services
Location: 123 Main St, Berlin
Phone: +49123456789
Website URL: https://abc-cleaning.de

Number of companies found: 40
Script execution completed.
```

## Troubleshooting
- **Chromedriver Version Mismatch**: Ensure your **ChromeDriver version matches your browser version**.
- **MySQL Connection Error**: Verify your **username, password, and database name**.
- **Website Changes**: If the website structure changes, update the **CSS selectors** accordingly.

## License
This project is **MIT licensed**. Feel free to modify and improve it!

---
🚀 Happy Scraping!
