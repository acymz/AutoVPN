import os
import requests
import base64
from datetime import datetime

# Function to fetch and decode URLs
def fetch_and_decode(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        decoded_content = base64.b64decode(content).decode('utf-8')
        return decoded_content
    else:
        print(f"Failed to fetch {url}")
        return ""

# URLs to fetch
urls = [
    "https://www.xrayvip.com/free.txt",
    "https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/v2",
    "https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub",
    "https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.txt"
]

# Fetch, decode, and filter the contents
filtered_contents = []
for url in urls:
    decoded_content = fetch_and_decode(url)
    filtered_lines = [line for line in decoded_content.splitlines() if not line.startswith("http")]
    filtered_contents.extend(filtered_lines)

# Combine and encode the contents
combined_content = "\n".join(filtered_contents)
encoded_content = base64.b64encode(combined_content.encode('utf-8')).decode('utf-8')

# Save the encoded content to files
data_dir = "data"
history_dir = "history"
v2_filename = "V2.txt"
timestamp = datetime.now().strftime("%Y%m%d%H%M")

# Create directories if they don't exist
os.makedirs(data_dir, exist_ok=True)
os.makedirs(history_dir, exist_ok=True)

# Save to data/V2.txt
with open(os.path.join(data_dir, v2_filename), "w") as f:
    f.write(encoded_content)

# Save to history/V2_TIMESTAMP.txt
with open(os.path.join(history_dir, f"V2_{timestamp}.txt"), "w") as f:
    f.write(encoded_content)
