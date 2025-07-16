#!/usr/bin/env python3
import csv
import sys
from datetime import datetime
from update_broadcasts import BroadcastManager

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

def import_csv(csv_path):
    """Import data from CSV file into broadcasts.json."""
    manager = BroadcastManager()
    
    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            title = clean_title(row['Title'])
            tags = extract_tags(title)
            
            # Determine file type and format from the title
            file_type = "audio"
            format = "mp3"
            if ".mp4" in title.lower():
                file_type = "video"
                format = "mp4"
            
            success = manager.add_broadcast(
                title=title,
                cid=row['CID'],
                file_size=row['File Size'],
                date_uploaded=parse_date(row['Date']),
                file_type=file_type,
                format=format,
                tags=tags
            )
            
            if success:
                print(f"Added: {title}")
            else:
                print(f"Skipped or failed: {title}")
    
    manager.save()
    print("\nImport completed!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python import_csv.py <path_to_csv>")
        sys.exit(1)
    
    import_csv(sys.argv[1]) 