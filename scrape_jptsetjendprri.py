import requests
from bs4 import BeautifulSoup
import json

def scrape_jptsetjendprri():
    url = "https://rosetpim.dpr.go.id/setjen/index/id/Sekretariat-BIRO-KESEKRETARIATAN-PIMPINAN"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "https://rosetpim.dpr.go.id/",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }

    session = requests.Session()
    response = session.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    data = []

    table = soup.find("table", class_="table")
    if not table:
        print("Could not find the data table on the page.")
        return

    tbody = table.find("tbody")
    if not tbody:
        print("Could not find the tbody element in the table.")
        return

    rows = tbody.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 2:
            name = cols[1].get_text(strip=True)
            data.append({"instansi": name})

    json_file = "jptsetjendprri.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Data successfully scraped and saved to {json_file}")

if __name__ == "__main__":
    scrape_jptsetjendprri()
