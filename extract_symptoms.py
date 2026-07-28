#!/usr/bin/env python3
"""
Extract symptoms from Cleveland Clinic website.
Since the site is JavaScript-heavy, we'll use multiple approaches.
"""
import requests
from bs4 import BeautifulSoup
import json
import re

def fetch_page(url):
    """Fetch a webpage with proper headers."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_symptoms_from_html(html):
    """Try to extract symptom names from HTML."""
    soup = BeautifulSoup(html, 'html.parser')
    
    # Look for common patterns of symptom lists
    symptoms = set()
    
    # Find all links that might be symptom pages
    for link in soup.find_all('a', href=True):
        href = link['href']
        text = link.get_text(strip=True)
        if '/health/symptoms/' in href.lower() or ('symptom' in href.lower()):
            if text and len(text) > 2:
                symptoms.add(text)
    
    # Also check for list items with symptom-like content
    for li in soup.find_all('li'):
        text = li.get_text(strip=True)
        if text and len(text) > 2:
            # Simple heuristic: if it looks like a single condition or symptom term
            symptoms.add(text)
    
    return sorted(symptoms)

def main():
    url = "https://my.clevelandclinic.org/health/symptoms"
    html = fetch_page(url)
    
    if html:
        # Try to find any data in scripts
        soup = BeautifulSoup(html, 'html.parser')
        scripts = soup.find_all('script')
        for script in scripts:
            src = script.get('src')
            if src and any(kw in src.lower() for kw in ['api', 'data', 'symptom']):
                print(f"Potential API/script: {src}")
        
        # Extract symptoms from HTML
        symptoms = extract_symptoms_from_html(html)
        print(f"Found {len(symptoms)} potential symptom entries:")
        for s in symptoms[:50]:
            print(f"  - {s}")
        
        # Save to file
        with open('/Users/csv610/Projects/MyBooks/MedSymptoms/symptoms_list.txt', 'w') as f:
            for s in symptoms:
                f.write(s + '\n')
        print("\nSaved to symptoms_list.txt")
    else:
        print("Could not fetch page")

if __name__ == '__main__':
    main()
