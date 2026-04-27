# Usage Guide

This guide explains how to capture and extract transcripts using Raw Capture YT.

## 1. Capturing Data
1. Navigate to a YouTube video in your browser.
2. Ensure you are signed in if the video has restricted access.
3. Click the **Raw Capture Bridge** icon in your browser toolbar.
4. Click **Capture Transcript**.
5. The extension will save a `.vtt` file to your default downloads folder or a specified temporary location.

## 2. Extracting the Transcript
Once you have the `.vtt` file, use the provided tools to clean it up.

### Using PowerShell (Recommended)
1. Open PowerShell.
2. Run the wrapper script:
   ```powershell
   ./tools/Start-Here.ps1 -InputFile "C:\path\to\captions.vtt" -Name "MyVideoTranscript"
```

### Using Python Directly
1. Open a terminal.
2. Run the script:
   ```bash
   python ./tools/Extract-Transcript.py "C:\path\to\captions.vtt" --name "MyVideoTranscript"
   ```

## 3. Reviewing Results
The final cleaned transcript will be saved in the `output/` folder as a `.txt` file. This file is formatted for easy reading and is compatible with browser "Read Aloud" features.
