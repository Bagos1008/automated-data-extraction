# Automated Web Scraping & Data Extraction Pipeline

This repository contains a collection of Python automation scripts designed to extract, clean, and format web data efficiently. It demonstrates capabilities ranging from static HTML parsing to full browser automation and hidden API interception.

## 🛠️ Tech Stack
* **Python** (Core Logic)
* **BeautifulSoup & Requests** (Static DOM Parsing)
* **Selenium WebDriver** (Dynamic Web / SPA / Automation)
* **Pandas** (Data Cleansing, Transformation, & Excel Export)

## 📂 Project Showcase

### 1. API Interception & Mass Extraction (`scraper_api.py`)
Bypasses visual browser rendering to directly intercept hidden backend APIs (JSON endpoints). 
* **Key Feature:** Capable of extracting hundreds of pages in seconds.
* **Data Cleansing:** Implements Pandas to clean null values and format text.
* **Output:** Directly writes clean, structured data to `.xlsx` format.

### 2. Dynamic Browser Automation (`scraper_dinamis.py`)
Controls a real Chrome browser instance to interact with JavaScript-heavy websites.
* **Key Feature:** Automates clicking (e.g., "Next Page" pagination), form filling, and waiting for dynamic elements to load.

### 3. Static Directory Extraction (`scraper_statis.py`)
Parses and traverses complex DOM structures to locate specific targets (Classes, IDs, nested Tags).

## 📊 Sample Output
The extraction scripts are configured to generate ready-to-use business data. Check `ekstraksi_api_massal.xlsx` for a sample output where raw web data has been converted into a structured tabular format.

---
*Open for freelance data extraction and processing opportunities. The scripts can be customized to target e-commerce directories, business contacts, or property listings.*