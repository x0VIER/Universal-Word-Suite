<div align="center">

![Universal Word Suite Banner](universal_word_suite_banner.png)

# Universal Word Suite
**The ultimate high-fidelity capture and translation suite for Video & Print.**

[![Version](https://img.shields.io/badge/version-1.1.0-red.svg)](https://github.com/x0VIER/Universal-Word-Suite)
[![License: MIT](https://img.shields.io/badge/License-MIT-white.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/platform-Windows-black.svg)](https://www.microsoft.com/windows)
[![Python](https://img.shields.io/badge/python-3.10+-red.svg)](https://www.python.org/)

[YouTube Tool](#1-youtube-transcript-extractor) • [Book Tool](#2-book-translation-suite) • [Quick Start](#quick-start) • [Workflows](#workflows) • [Safety](#safety-and-privacy)

</div>

---

## Overview

**Universal Word Suite** is a professional-grade toolkit designed for high-fidelity extraction and translation across two major domains: **YouTube Video** and **Physical/Digital Books**. 

Whether you need to **get YouTube videos** and **download YouTube videos from members-only pages** or process a multi-hundred-page book with forensic OCR accuracy, this suite provides the raw, unfiltered truth without the overhead of cloud APIs or AI summarization.

---

## 📽️ 1. YouTube Transcript Extractor

Designed for researchers who need to **translate YouTube** content or **get a transcript for YouTube videos with no transcript**. 

- **Session-Based Capture**: Extracts caption tracks directly from your authenticated browser session.
- **Member-Only Access**: Seamlessly **download YouTube videos from members-only pages** by using your own cookies.
- **Raw Word-for-Word**: No summaries. Every word captured using **YouTube video audio to get transcripts** or direct caption streams.

## 📚 2. Book Translation Suite

A high-performance OCR engine that turns page images into professional translations.

- **High-Fidelity OCR**: Uses advanced local models to read text from physical or digital book scans.
- **Automated Workflow**: Processes entire folders of page images into a single, unified document.
- **Multi-Language Support**: Optimized for forensic translation across dozens of language pairs.

---

## Key Features

| Domain | Feature | Benefit |
| :--- | :--- | :--- |
| **YouTube** | **Get YouTube videos** as text | Instant access to searchable transcripts. |
| **YouTube** | **Download videos** from private pages | Captures data behind authentication walls. |
| **Books** | **Forensic OCR** Translation | Converts physical scans into editable, translated text. |
| **General** | **Translate YouTube** & Print | Consistent high-quality translation across media. |

---

## Quick Start

### 1. The Bridge (For YouTube)
- Open `chrome://extensions` and enable **Developer mode**.
- Click **Load unpacked** and select the `extension/` folder.
- Capture your transcript directly from the YouTube player.

### 2. The Extraction
- Open the `tools/` folder.
- Right-click `Start-Here.ps1` and select **Run with PowerShell**.
- Choose **(1)** for YouTube Transcripts or **(2)** for Book Translation.

<details>
<summary><b>🛠️ Advanced Setup & Manual Installation</b></summary>

### Prerequisites
- Windows 10/11
- Python 3.10+
- `pip install -r requirements.txt` (Required for Book OCR)

### Manual Command Line Usage
- **YouTube**: `python tools/Extract-Transcript.py <vtt_path> --name <output>`
- **Books**: `python tools/Book-Translator.py <folder_path> --src es --dest en`

</details>

---

## Workflows

I have created specialized guides for everyone, no matter your technical level:

- 👤 **[For Humans (Technical Guide)](docs/usage.md)**
- 👶 **[For Beginners (Simple Guide)](docs/simple-start.md)**
- 🤖 **[For AI Agents (AGENTS.md)](AGENTS.md)**

---

## Safety and Privacy

> [!NOTE]
> **Universal Word Suite** runs entirely on your local hardware. It does not send your session data, cookies, or book scans to any external servers. I designed this tool for personal use with content you have authorized access to. It does not bypass paywalls or DRM.

---

<div align="center">
I made this tool for researchers and developers.
</div>
