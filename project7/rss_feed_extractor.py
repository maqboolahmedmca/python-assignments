import os
import threading
import time
from tkinter import SEPARATOR
import requests
import feedparser
from concurrent.futures import ThreadPoolExecutor, as_completed
import bs4

RSS_FEED_URL = "https://feeds.bbci.co.uk/news/rss.xml"
OUTPUT_FOLDER = "output"
OUTPUT_FILE = "bbc_topstory_{}.txt"
MAX_WORKERS = 5

def load_rss_from_url(url):
    """Fetch and parse the RSS feed from a URL."""
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        raise RuntimeError(f"Error fetching RSS feed: {e}")

    content = resp.content
    if not content:
        raise ValueError("RSS feed content is empty")
    
    feed = feedparser.parse(content)
    if (feed.bozo):
        raise ValueError(f"RSS feed failed: {feed.bozo_exception}")
    if not feed.entries:
        raise ValueError("RSS feed has no entries")

    return feed

def fetch_page_content(url):
    """Fetch the content of a page from a URL."""
    try:
        print(f"🔹 Starting {url} in thread {threading.current_thread().name}")
        resp = requests.get(url, timeout=10)
        time.sleep(1)
        print(f"✅ Finished {url} in thread {threading.current_thread().name}")
    except Exception as e:
        raise RuntimeError(f"Error fetching page content: {e}")

    return resp.content

def main():
    try:
        feed = load_rss_from_url(RSS_FEED_URL)
    except Exception as e:
        print(f"Failed to load RSS feed: {e}")
        return

    links = [entry.link for entry in feed.entries]
    print(f"Found {len(links)} entries in the feed")

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(fetch_page_content, link): link for link in links}

        for i, future in enumerate(as_completed(futures)):
            link = futures[future]
            try:
                content = future.result()
                soup = bs4.BeautifulSoup(content, "lxml")
                output_file = OUTPUT_FOLDER + '/' + OUTPUT_FILE.format(i + 1)
                with open(output_file, "w") as f:
                    SEPARATOR = ("*" * 100)
                    f.write(f"{i+1}). {link} \n {SEPARATOR} \n\n{soup.text}")
                    print(f"{link}'s text is successfully written to {output_file}")

            except Exception as e:
                print(f"Error fetching page content: {e}")

main()
