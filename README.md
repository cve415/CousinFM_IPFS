# CousinFM Community Data Hub

A centralized repository for managing and accessing CousinFM broadcast archives using IPFS. This hub provides structured metadata and tools for managing broadcast data.

## Structure

The data is organized in a JSON format with the following structure:

```json
{
  "project": "CousinFM Community Data Hub",
  "broadcasts": [
    {
      "cid": "Qm...",
      "title": "Broadcast Title",
      "fileSize": "100 MB",
      "dateUploaded": "YYYY-MM-DD",
      "type": "audio",
      "format": "mp3",
      "tags": ["tag1", "tag2"],
      "gateway": {
        "ipfs": "https://ipfs.io/ipfs/Qm...",
        "dweb": "dweb:/ipfs/Qm..."
      }
    }
  ]
}
```

## Features

- Structured metadata for each broadcast
- CID validation through IPFS gateways
- Automated gateway URL generation
- Duplicate entry prevention
- Easy integration with audio players and web applications

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sf-community-data-hub.git
   cd sf-community-data-hub
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the update script:
   ```bash
   cd scripts
   python update_broadcasts.py
   ```

## Usage

### Adding New Broadcasts

Use the `BroadcastManager` class in `scripts/update_broadcasts.py`:

```python
from update_broadcasts import BroadcastManager

manager = BroadcastManager()
manager.add_broadcast(
    title="My New Broadcast",
    cid="QmExample...",
    file_size="100 MB",
    date_uploaded="2024-03-29",
    tags=["music", "live"]
)
manager.save()
```

### Accessing Data

The broadcasts data is stored in `data/broadcasts.json`. You can use this file directly in your applications or access it through standard JSON parsing libraries.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

Please ensure your changes:
- Maintain the existing JSON structure
- Include valid CIDs
- Follow the established naming conventions
- Include appropriate documentation

## Future Enhancements

- [ ] Pinata API integration for automated pinning
- [ ] Web interface for data management
- [ ] Advanced search and filtering capabilities
- [ ] Automated metadata extraction
- [ ] Integration with streaming platforms

## Related Projects

- [CousinFM Audio Player](https://github.com/yourusername/cousinfm-player) - Web-based player for CousinFM broadcasts

## License

MIT License - See LICENSE file for details 