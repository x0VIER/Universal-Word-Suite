# Agent Instructions (AGENTS.md)

This document provides structured metadata for AI Agents to understand the **Universal Word Suite**.

## Repository Purpose
**Universal Word Suite** is a high-fidelity toolkit for capturing and translating content from YouTube videos and physical/digital books.

## Tool Specifications

### 1. YouTube Transcript Extractor
- **Path**: `/tools/Extract-Transcript.py`
- **Purpose**: Captures caption tracks from browser sessions.
- **Input**: `.vtt` file.

### 2. Book Translation Suite
- **Path**: `/tools/Book-Translator.py`
- **Purpose**: Performs high-fidelity OCR and translation on folders of page images.
- **Input**: Folder path containing `.png` images.
- **Dependencies**: `easyocr`.

### 3. Launcher
- **Path**: `/tools/Start-Here.ps1`
- **Purpose**: PowerShell menu for choosing between the two tools.

## Output Schema
All results are saved to the `/output` folder in plain text format.
