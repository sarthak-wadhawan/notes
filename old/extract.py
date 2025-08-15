from bs4 import BeautifulSoup
import json
import re

# Function to clean special characters
def clean_text(text):
    # Replace non-ASCII characters with empty string
    return re.sub(r'[^\x00-\x7F]+', '', text)

# Load the HTML file
with open("Weekly Knowledge Sheets .html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

sheets = []

# Find all outer tables (each weekly knowledge block)
outer_tables = soup.find_all("table", attrs={"border": "2"})

for outer_table in outer_tables:
    # Location, date, country
    location = date = country = None
    try:
        inner_table = outer_table.find("table", border="0")
        rows = inner_table.find_all("tr")
        location = rows[0].find_all("td")[1].get_text(strip=True) if len(rows[0].find_all("td")) > 1 else rows[0].get_text(strip=True)
        date = rows[1].find_all("td")[0].get_text(strip=True)
        country = rows[1].find_all("td")[1].get_text(strip=True) if len(rows[1].find_all("td")) > 1 else ""
    except:
        pass

    content_tds = outer_table.find_all('td', colspan="2")
    title = None
    text_lines = []

    for td in content_tds:
        # Find the title
        b_tag = td.find('b')
        if b_tag:
            b_text = b_tag.get_text(strip=True)
            if b_text.upper() != "JAI GURU DEV":
                title = clean_text(b_text)

        for p in td.find_all('p'):
            p_text = p.get_text(strip=True)
            if not p_text:
                continue

            # Skip repeated title or JAI GURU DEV
            if title and p_text == title:
                continue
            if "JAI GURU DEV" in p_text.upper():
                continue

            # Normal text
            clean_line = clean_text(p_text)
            if clean_line:
                text_lines.append(clean_line)

    sheet = {
        "location": clean_text(location) if location else None,
        "date": clean_text(date) if date else None,
        "country": clean_text(country) if country else None,
        "title": title if title else None,
        "text": "\n".join(text_lines) if text_lines else None
    }

    sheets.append(sheet)

# Save to JSON
with open("knowledge_sheets.json", "w", encoding="utf-8") as f:
    json.dump(sheets, f, ensure_ascii=False, indent=4)

print(f"Extracted {len(sheets)} knowledge sheets into knowledge_sheets.json")
