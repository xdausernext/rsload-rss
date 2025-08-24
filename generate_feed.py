import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
from urllib.parse import urljoin

# Target page
url = "https://rsload.net/soft/page/1/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

# ⚠️ Adjust selector depending on rsload.net layout
articles = soup.select("h2 a")

fg = FeedGenerator()
fg.title("RSLoad.net Custom Feed")
fg.link(href=url)
fg.description("Custom-generated RSS from rsload.net")

for a in articles:
    fe = fg.add_entry()
    fe.title(a.get_text(strip=True))
    href = a['href']
    if href.startswith("/"):
        href = urljoin(url, href)
    fe.link(href=href)

# Save output
with open("docs/feed.xml", "wb") as f:   # important: inside docs/ for Pages
    f.write(fg.rss_str(pretty=True))

print("✅ Feed generated: docs/feed.xml")
