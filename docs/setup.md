# Setup Guide

Follow these steps to set up Raw Capture YT on your Windows machine.

## 1. Prerequisites
Ensure you have the following installed:
- **Python 3.10+**: Download from [python.org](https://www.python.org/).
- **PowerShell**: Windows PowerShell (default) or PowerShell 7.
- **Chrome/Edge**: A modern Chromium-based browser.

## 2. Installation
1. Clone this repository or download the ZIP file.
2. Open a terminal in the project root.
3. Install Python dependencies (optional but recommended):
   ```powershell
   pip install -r requirements.txt
   ```

## 3. Browser Extension Setup
1. Open your browser and navigate to `chrome://extensions`.
2. Toggle **Developer mode** on.
3. Click **Load unpacked**.
4. Select the `extension/` folder from this project.

## 4. Native Messaging Host (Advanced)
If you intend to use the direct bridge, you must register the native messaging host. See [browser-extension.md](browser-extension.md) for details.
