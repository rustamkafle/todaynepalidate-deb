# /etc/nepali-date/cache_writer.py

import requests
from bs4 import BeautifulSoup
from datetime import date

result = requests.get("https://www.hamropatro.com/")
soup = BeautifulSoup(result.content, "html.parser")
nep = soup.find_all(class_="nep")
cleaned = ' '.join(nep[0].text.split())

with open("/etc/nepali-date/today_date.txt", "w") as f:
    f.write(f"{date.today().isoformat()}\n")
    f.write(f"{cleaned}\n")
