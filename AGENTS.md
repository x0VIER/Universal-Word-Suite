# Agent Instructions (AGENTS.md)

This document provides structured metadata and instructions for AI Agents (LLMs, Coding Assistants, and Automators) to understand and execute the **Raw Capture YT** toolchain.

## Repository Purpose
**Raw Capture YT** is a high-fidelity YouTube transcript extraction tool. It bypasses the limitations of external APIs by using the user's active browser session to capture caption tracks.

## Tool Specifications

### 1. Browser Bridge (Extension)
- **Path**: `/extension`
- **Mechanism**: Manifest V3 extension. Uses `chrome.cookies` and `activeTab`.
- **Agent Action**: If asked to help with the extension, focus on `background.js` for session handling and `popup.js` for status reporting.

### 2. Transcript Extractor (Python)
- **Path**: `/tools/Extract-Transcript.py`
- **Input**: A `.vtt` file (WebVTT format).
- **Execution Command**: `python Extract-Transcript.py <input_path> --name <output_name>`
- **Logic**: 
  - Parses VTT using `TIMING_RE` and `TAG_RE`.
  - Dedupes repetitive caption lines.
  - Groups entries into readable paragraphs based on 3-minute intervals or 900-character limits.
- **Output**: A plain text file in `/output`.

### 3. PowerShell Wrapper
- **Path**: `/tools/Start-Here.ps1`
- **Execution**: `./Start-Here.ps1 -InputFile <path> -Name <name>`
- **Purpose**: A simplified entry point for Windows users that handles environment checks and triggers the Python script.

## Input/Output Schema
- **Input Format**: WebVTT (standard YouTube caption download).
- **Output Format**: UTF-8 Plain Text with timestamp headers.

## Constraints for Agents
- **Privacy**: Never suggest code that uploads session cookies or data to external servers.
- **Paths**: Always use relative paths or `Path(__file__)`. Do not assume absolute paths (e.g., `C:\Users`).
- **Context**: This tool is for *local* extraction. Do not attempt to integrate with cloud transcription services unless explicitly asked.
