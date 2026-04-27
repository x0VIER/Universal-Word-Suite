<#
.SYNOPSIS
    Universal Word Suite - Easy Start Wrapper
.DESCRIPTION
    Launcher for YouTube Transcript Extraction and Book Translation tools.
#>

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$ExtractorScript = Join-Path $ScriptDir "Extract-Transcript.py"
$BookScript = Join-Path $ScriptDir "Book-Translator.py"

Write-Host "==============================" -ForegroundColor Red
Write-Host "    UNIVERSAL WORD SUITE" -ForegroundColor White
Write-Host "==============================" -ForegroundColor Red
Write-Host ""
Write-Host "Select the tool you want to run:"
Write-Host "1) YouTube Transcript Extractor"
Write-Host "2) Book Translator (OCR)"
Write-Host ""

$Choice = Read-Host "Choice (1 or 2)"

if ($Choice -eq "1") {
    $InputFile = Read-Host "Drag and drop your .vtt file here"
    $InputFile = $InputFile.Trim('"')
    $Name = Read-Host "Enter output name (optional)"
    if ([string]::IsNullOrWhiteSpace($Name)) { $Name = "transcript_output" }
    
    Write-Host "`nRunning YouTube Extractor..." -ForegroundColor Cyan
    python $ExtractorScript $InputFile --name $Name
}
elseif ($Choice -eq "2") {
    $InputFolder = Read-Host "Drag and drop the folder containing page images here"
    $InputFolder = $InputFolder.Trim('"')
    $Name = Read-Host "Enter output name (optional)"
    if ([string]::IsNullOrWhiteSpace($Name)) { $Name = "book_output" }
    $Src = Read-Host "Source language code (default: es)"
    if ([string]::IsNullOrWhiteSpace($Src)) { $Src = "es" }
    $Dest = Read-Host "Target language code (default: en)"
    if ([string]::IsNullOrWhiteSpace($Dest)) { $Dest = "en" }

    Write-Host "`nRunning Book Translator (This may take a minute)..." -ForegroundColor Cyan
    python $BookScript $InputFolder --name $Name --src $Src --dest $Dest
}
else {
    Write-Host "Invalid choice. Exiting." -ForegroundColor Red
}

Write-Host "`nPress any key to close..."
$null = [Console]::ReadKey()
