from bs4 import BeautifulSoup
import json
import re

html_file = "sheets.html"

with open(html_file, "r", encoding="windows-1252") as f:
    soup = BeautifulSoup(f, "html.parser")

sheets = []

for anchor in soup.find_all('a', attrs={'name': True}):
    try:
        outer_table = anchor.find_next('table', attrs={'border': '2'})
        if not outer_table:
            continue

        # Metadata table
        nested_table = outer_table.find('table')
        rows = nested_table.find_all('tr')
        location = rows[0].find_all('td')[1].get_text(strip=True)
        date = rows[1].find_all('td')[0].get_text(strip=True)
        country = rows[1].find_all('td')[1].get_text(strip=True)

        # Main content td
        content_td = outer_table.find('td', colspan="2")
        if not content_td:
            continue

        # Title
        title_tag = content_td.find('b')
        title = title_tag.get_text(strip=True) if title_tag else ""

        # Text
        text_lines = []
        for p in content_td.find_all('p'):
            if p.find('b'):  # skip title
                continue
            line = p.get_text(strip=True)
            if line:
                text_lines.append(line)

        # Separate NEWS FLASH and main text
        news_flash_lines = []
        final_text = []
        news_flag = False
        for line in text_lines:
            if re.search(r'\bNEWS\s*FLASH\b', line, re.IGNORECASE):
                news_flag = True
                continue
            if news_flag:
                news_flash_lines.append(line)
            else:
                # Avoid repeating title at start of text
                if line != title:
                    final_text.append(line)

        sheet = {
            "location": location if location else None,
            "date": date if date else None,
            "country": country if country else None,
            "title": title if title else None,
            "text": "\n".join(final_text) if final_text else None,
            "news_flash": "\n".join(news_flash_lines) if news_flash_lines else None
        }

        sheets.append(sheet)

    except Exception as e:
        print(f"Skipping a sheet due to parsing issue: {e}")

with open("knowledge_sheets.json", "w", encoding="utf-8") as f:
    json.dump(sheets, f, ensure_ascii=False, indent=4)

print(f"Extracted {len(sheets)} knowledge sheets into knowledge_sheets.json")
