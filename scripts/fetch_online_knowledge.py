import os
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime

INBOX_DIR = "inbox"
os.makedirs(INBOX_DIR, exist_ok=True)

# Fetch latest Computer Science & AI preprints from arXiv API
ARXIV_RSS_URL = "https://rss.arxiv.org/rss/cs.AI"

def fetch_arxiv_updates():
    print("Fetching latest online research updates...")
    req = urllib.request.Request(ARXIV_RSS_URL, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            
            # Parse RSS feed items
            items = root.findall('./channel/item')[:3] # Grab top 3 latest items
            
            for idx, item in enumerate(items):
                title = item.find('title').text if item.find('title') is not None else "Untitled"
                description = item.find('description').text if item.find('description') is not None else ""
                link = item.find('link').text if item.find('link') is not None else ""
                
                # Format raw file for the inbox
                content = f"Source: {link}\nTitle: {title}\n\nSummary:\n{description}"
                
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = os.path.join(INBOX_DIR, f"online_feed_{timestamp}_{idx}.txt")
                
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Saved online knowledge item: {filename}")

    except Exception as e:
        print(f"Failed to fetch online feed: {e}")

if __name__ == "__main__":
    fetch_arxiv_updates()
