# Browser Extension Details

The **Raw Capture Bridge** is a lightweight extension that interacts with the YouTube player to extract caption data using your active browser session.

## Features
- **Session Auth**: Uses your cookies and logged-in state to access authorized content.
- **VTT Extraction**: Pulls the raw WebVTT data directly from the network or player state.
- **Privacy**: Does not store your history or personal data; it only passes session-specific caption URLs to the local tool.

## Manifest Configuration
The extension uses Manifest V3. Key permissions include:
- `cookies`: To handle authenticated requests.
- `activeTab`: To interact with the current YouTube page.
- `storage`: To save temporary session state.

## Security
This extension is designed to run locally. It does not send your data to any external servers. All processing happens on your machine.
