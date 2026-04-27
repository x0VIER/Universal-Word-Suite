# Troubleshooting

Common issues and solutions for Raw Capture YT.

## 1. Extension Not Loading
- **Issue**: "Load unpacked" fails.
- **Solution**: Ensure you selected the folder containing `manifest.json`. Check for syntax errors in the manifest.

## 2. No Captions Found
- **Issue**: The tool reports "No valid transcript entries found."
- **Solution**: Ensure the video actually has captions. Some videos only have auto-generated captions; ensure they are enabled in the YouTube player before capturing.

## 3. Python Errors
- **Issue**: `ModuleNotFoundError: No module named '...'`
- **Solution**: Run `pip install -r requirements.txt` to install missing dependencies.

## 4. Permission Errors
- **Issue**: PowerShell script fails to run due to execution policy.
- **Solution**: Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` in PowerShell.
