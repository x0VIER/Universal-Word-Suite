# Raw Capture YT

Raw Capture YT is a local tool for capturing YouTube video text from your own browser session and preparing it for transcription, translation, and read-aloud workflows.

It is designed for users who want a cleaner transcript workflow than the default YouTube captions or browser translation tools provide.

## Safety and Legal Boundary
This tool is intended for personal use with videos you are allowed to access. It does not bypass paywalls, DRM, account restrictions, or platform security controls.

## Requirements

- Windows 10 or 11
- Google Chrome or Microsoft Edge
- PowerShell 7 or Windows PowerShell
- Python 3.10 or newer, if using the Python tools
- A browser session already signed in to YouTube

## Project Structure

```text
README.md             # Project overview
LICENSE               # MIT License
.gitignore            # Git exclusion rules
.env.example          # Template for environment variables
CHANGELOG.md          # Version history
SECURITY.md           # Security policy
CONTRIBUTING.md       # Contribution guidelines
docs/                 # Detailed documentation
extension/            # Browser extension source
tools/                # Capture and extraction scripts
examples/             # Sample output files
tests/                # Basic validation tests
.github/              # GitHub templates and actions
```

## Quick Start

1. **Install the Extension**:
   - Open Chrome/Edge and go to `chrome://extensions`.
   - Enable "Developer mode".
   - Click "Load unpacked" and select the `extension` folder.

2. **Capture Captions**:
   - Visit a YouTube video.
   - Use the extension to capture the `.vtt` file from your session.

3. **Run Extraction**:
   - Open PowerShell and navigate to the `tools` folder.
   - Run: `./run-capture.ps1 -InputFile "path/to/captions.vtt" -Name "my_transcript"`

## Documentation
For detailed setup and usage instructions, please refer to the [docs/](docs/) directory:
- [Setup Guide](docs/setup.md)
- [Usage Guide](docs/usage.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Browser Extension](docs/browser-extension.md)

## License
Distributed under the MIT License. See `LICENSE` for more information.
