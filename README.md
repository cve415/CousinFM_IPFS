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

## 
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
