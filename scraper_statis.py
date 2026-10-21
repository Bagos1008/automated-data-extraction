import requests
from bs4 import BeautifulSoup
import csv  # 1. Import modul bawaan csv

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
books = soup.find_all('article', class_='product_pod')

# 2. Siapkan list kosong untuk menampung semua data
data_buku = []

for book in books[:5]:
    title = book.h3.a['title']
    
    # Menyesuaikan dengan pembersihan yang sudah kamu lakukan
    price = book.find('p', class_='price_color').text.replace('Â', '').strip()
    stok = book.find('p', class_='instock availability').text.strip()
    peringkat = book.p['class'][1]
    
    # 3. Kumpulkan data per buku ke dalam dictionary, lalu tambahkan ke list utama
    data_buku.append({
        'Judul': title,
        'Harga': price,
        'Stok': stok,
        'Peringkat': peringkat
    })

# 4. Buka (atau buat) file CSV dan tulis datanya
with open('hasil_scraping.csv', 'w', newline='', encoding='utf-8-sig') as file:
    
    writer = csv.DictWriter(file, fieldnames=['Judul', 'Harga', 'Stok', 'Peringkat'], delimiter=';')
    
    writer.writeheader() # Menulis baris judul kolom
    writer.writerows(data_buku) # Menulis seluruh isi data sekaligus
    
print("Proses selesai! Data berhasil disimpan ke hasil_scraping.csv")