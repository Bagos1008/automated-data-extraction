import requests
import pandas as pd
import time

semua_data = []

# Mengambil data dari halaman 1 sampai 5 secara otomatis
for page in range(1, 6):
    print(f"Menyedot data dari API Halaman {page}...")
    
    # URL dibuat dinamis menggunakan f-string
    api_url = f"http://quotes.toscrape.com/api/quotes?page={page}"
    
    response = requests.get(api_url)
    data_json = response.json()
    
    # Mengamankan loop: Jika array 'quotes' kosong (halaman habis), hentikan proses
    if not data_json.get('quotes'):
        print("Data sudah habis.")
        break
        
    for item in data_json['quotes']:
        semua_data.append({
            "Penulis": item['author']['name'], 
            "Kutipan": item['text']
        })
    
    # Etika Scraping: Beri jeda kecil agar server target tidak kelebihan beban
    time.sleep(1)

# Mengonversi dan menyimpan keseluruhan data yang terkumpul
df = pd.DataFrame(semua_data)
df.to_excel('ekstraksi_api_massal.xlsx', index=False)

print(f"\nSelesai! Total {len(df)} kutipan berhasil disimpan ke ekstraksi_api_massal.xlsx")