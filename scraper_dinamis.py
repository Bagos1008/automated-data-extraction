from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("http://quotes.toscrape.com/")

# Menyiapkan list untuk menampung dictionary data
semua_data = []

for page in range(1, 4):
    print(f"Mengekstrak Halaman {page}...")
    time.sleep(2) 
    
    quotes = driver.find_elements(By.CLASS_NAME, "quote")
    for q in quotes:
        text = q.find_element(By.CLASS_NAME, "text").text
        author = q.find_element(By.CLASS_NAME, "author").text
        
        # Menyimpan tiap baris data ke dalam list
        semua_data.append({
            "Penulis": author,
            "Kutipan": text
        })
    
    try:
        driver.find_element(By.PARTIAL_LINK_TEXT, "Next").click()
    except:
        break

driver.quit()

# --- FASE PANDAS DIMULAI DI SINI ---

# 1. Mengonversi list data menjadi DataFrame (Tabel Pandas)
df = pd.DataFrame(semua_data)

# 2. Contoh Pembersihan: Mengubah semua nama penulis menjadi huruf kapital
df['Penulis'] = df['Penulis'].str.upper()

# 3. Mengekspor langsung ke format Excel (.xlsx) tanpa masalah delimiter CSV
df.to_excel('hasil_kutipan_bersih.xlsx', index=False)

print("\nSukses! Data telah dibersihkan dan disimpan sebagai hasil_kutipan_bersih.xlsx")