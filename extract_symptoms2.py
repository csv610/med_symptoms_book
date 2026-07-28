#!/usr/bin/env python3
"""Extract symptoms from Cleveland Clinic - alternative approach."""
import requests
from bs4 import BeautifulSoup
import re

def fetch_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    }
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print('Error: {}'.format(e))
        return None

url = 'https://my.clevelandclinic.org/health/symptoms'
html = fetch_page(url)

if html:
    with open('/tmp/cleveland_symptoms.html', 'w') as f:
        f.write(html)
    print('Page fetched, length: {}'.format(len(html)))
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Look for any script tags with possible data
    scripts = soup.find_all('script')
    print('Found {} script tags'.format(len(scripts)))
    
    # Print content of first few scripts that might contain data
    for i, script in enumerate(scripts[:5]):
        text = str(script.get_text())
        if len(text) > 100:
            print('Script {} (first 500 chars):'.format(i))
            print(text[:500])
else:
    print('Failed to fetch page')
