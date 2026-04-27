<#
.SYNOPSIS
    Raw Capture YT - PowerShell Wrapper
.DESCRIPTION
    Simplifies the execution of the transcript extraction tool.
#>

param (
    [Parameter(Mandatory=$true)]
    [string]$InputFile,

    [Parameter(Mandatory=$false)]
    [string]$Name = "transcript_output"
)

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$PythonScript = Join-Path $ScriptDir "run-capture.py"

if (-not (Test-Path $InputFile)) {
    Write-Error "Input file not found: $InputFile"
    exit 1
}

Write-Host "--- Raw Capture YT ---" -ForegroundColor Cyan
Write-Host "Input: $InputFile"
Write-Host "Running Python extractor..."

python $PythonScript $InputFile --name $Name

if ($LASTEXITCODE -eq 0) {
    Write-Host "Done." -ForegroundColor Green
} else {
    Write-Host "Error occurred during extraction." -ForegroundColor Red
}
