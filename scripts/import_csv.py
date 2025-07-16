#!/usr/bin/env python3
import csv
import json
import sys
import os
from datetime import datetime

def parse_date(date_str):
    """Convert date string to YYYY-MM-DD format."""
    try:
        date_obj = datetime.strptime(date_str.strip(), "%m/%d/%Y")
        return date_obj.strftime("%Y-%m-%d")
    except ValueError:
        return date_str

def clean_title(title):
    """Clean up title string by removing extra whitespace and newlines."""
    return " ".join(title.replace("\n", " ").split())

def extract_tags(title):
    """Extract potential tags from the title."""
    tags = []
    
    # Common keywords to look for
    keywords = {
        "vinyl": ["vinyl"],
        "mix": ["mix"],
        "broadcast": ["broadcast"],
        "test": ["test"],
        "live": ["live"],
        "special": ["special"],
        "revisited": ["revisited", "revised"],
        "collaboration": ["w/", "with", "feat", "featuring"]
    }
    
    title_lower = title.lower()
    
    for category, words in keywords.items():
        if any(word in title_lower for word in words):
            tags.append(category)
    
    return tags

def import_csv(csv_path, json_path='../data/broadcasts.json'):
    """Import data from CSV file into broadcasts.json."""
    # Initialize the JSON structure
    data = {
        "project": "CousinFM Community Data Hub",
        "description": "Archive of CousinFM radio broadcasts and related media",
        "version": "1.0.0",
        "lastUpdated": datetime.now().strftime("%Y-%m-%d"),
        "broadcasts": []
    }
    
    # Read existing data if file exists
    if os.path.exists(json_path):
        with open(json_path, 'r') as jsonfile:
            data = json.load(jsonfile)
    
    # Track existing CIDs to avoid duplicates
    existing_cids = {broadcast["cid"] for broadcast in data["broadcasts"]}
    
    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cid = row['CID'].strip()
            if not cid or cid in existing_cids:
                continue
                
            title = clean_title(row['Title'])
            tags = extract_tags(title)
            
            # Determine file type and format from the title
            file_type = "audio"
            format = "mp3"
            if ".mp4" in title.lower():
                file_type = "video"
                format = "mp4"
            
            broadcast = {
                "cid": cid,
                "title": title,
                "fileSize": row['File Size'],
                "dateUploaded": parse_date(row['Date']),
                "type": file_type,
                "format": format,
                "tags": tags,
                "gateway": {
                    "ipfs": f"https://ipfs.io/ipfs/{cid}",
                    "dweb": f"dweb:/ipfs/{cid}"
                }
            }
            
            data["broadcasts"].append(broadcast)
            existing_cids.add(cid)
            print(f"Added: {title}")
    
    # Sort broadcasts by date
    data["broadcasts"].sort(key=lambda x: x["dateUploaded"], reverse=True)
    
    # Save the updated data
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)
    
    print(f"\nImport completed! Total broadcasts: {len(data['broadcasts'])}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python import_csv.py <path_to_csv>")
        sys.exit(1)
    
    import_csv(sys.argv[1]) 