import csv
import json

# Ganti 'data.csv' dengan nama file CSV Anda
csv_file = 'data.csv'
json_file = 'data.json'

# Membaca file CSV dan mengonversinya ke JSON
data = []
with open(csv_file, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Ambil nama instansi dari kolom pertama (asumsi kolom pertama adalah nama instansi)
        instansi_name = list(row.values())[0]
        data.append({
            "instansi": instansi_name
        })

# Menyimpan data ke file JSON
with open(json_file, mode='w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print(f"Data berhasil dikonversi ke {json_file}")
