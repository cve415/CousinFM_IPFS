#!/usr/bin/env python3
import json
import os
import sys
import requests
from datetime import datetime
from typing import Dict, List, Optional

class BroadcastManager:
    def __init__(self, data_file: str = "../data/broadcasts.json"):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self) -> Dict:
        """Load the existing broadcast data."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {
            "project": "CousinFM Community Data Hub",
            "description": "Archive of CousinFM radio broadcasts and related media",
            "version": "1.0.0",
            "lastUpdated": datetime.now().strftime("%Y-%m-%d"),
            "broadcasts": []
        }

    def validate_cid(self, cid: str) -> bool:
        """Validate CID by checking gateway accessibility."""
        gateway_url = f"https://ipfs.io/ipfs/{cid}"
        try:
            response = requests.head(gateway_url, timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def add_broadcast(self, title: str, cid: str, file_size: str, 
                     date_uploaded: str, file_type: str = "audio", 
                     format: str = "mp3", tags: Optional[List[str]] = None) -> bool:
        """Add a new broadcast entry."""
        if not self.validate_cid(cid):
            print(f"Warning: CID {cid} validation failed")
            return False

        broadcast = {
            "cid": cid,
            "title": title,
            "fileSize": file_size,
            "dateUploaded": date_uploaded,
            "type": file_type,
            "format": format,
            "tags": tags or [],
            "gateway": {
                "ipfs": f"https://ipfs.io/ipfs/{cid}",
                "dweb": f"dweb:/ipfs/{cid}"
            }
        }

        # Check for duplicates
        if not any(b["cid"] == cid for b in self.data["broadcasts"]):
            self.data["broadcasts"].append(broadcast)
            self.data["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")
            return True
        return False

    def save(self):
        """Save the current data to file."""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)

def main():
    manager = BroadcastManager()
    
    # Example usage:
    # manager.add_broadcast(
    #     title="New Broadcast",
    #     cid="QmExample...",
    #     file_size="100 MB",
    #     date_uploaded="2024-03-29"
    # )
    
    manager.save()

if __name__ == "__main__":
    main() 