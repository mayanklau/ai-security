import os
import requests
from bs4 import BeautifulSoup

# Set the dummy website URL
url = "http://demo.testfire.net"

try:
    # Fetch the website content with a 30-second timeout
    response = requests.get(url, timeout=30)
    response.raise_for_status()  # Raise an error for bad responses
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Delete the old file if it exists
    if os.path.exists("site_content.txt"):
        os.remove("site_content.txt")
    
    # Write the new content to the file
    with open("site_content.txt", "w") as f:
        f.write(soup.get_text())
    
    print("Website content from", url, "saved successfully.")
except requests.exceptions.RequestException as e:
    print(f"Error fetching website: {e}")
