# Troubleshooting

Common issues and solutions for Raw Capture YT.

## 1. Extension Not Loading
- **Issue**: "Load unpacked" fails.
- **Solution**: Ensure you selected the folder containing `manifest.json`. Check for syntax errors in the manifest.

## 2. No Captions? No Problem.
- **Issue**: The video you want to translate does not have a caption track.
- **Solution**: I designed this tool to work even without captions! Simply use the **Audio Mode** to run a local AI transcription. This will listen to the video audio and create a perfect transcript from scratch. Ensure you have `faster-whisper` installed.
- **Command**: `python tools/Extract-Transcript.py "video.mp4" --mode audio`

## 3. Python Errors
- **Issue**: `ModuleNotFoundError: No module named '...'`
- **Solution**: Run `pip install -r requirements.txt` to install missing dependencies.

## 4. Permission Errors
- **Issue**: PowerShell script fails to run due to execution policy.
- **Solution**: Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` in PowerShell.
