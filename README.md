# HEIC2JPG

A simple Python tool to convert HEIC images to JPG format.

## Description

This tool allows you to convert HEIC (High Efficiency Image Container) images to JPG format. It supports both single file conversion and batch conversion of entire directories.

## Requirements

- uv (Python package manager)

## How to Use

### Convert a single file:
```bash
uv run main.py input.heic output_directory
```

### Convert all HEIC files in a directory:
```bash
uv run main.py input_directory output_directory
```

The tool will:
- Automatically create the output directory if it doesn't exist (with your confirmation)
- Convert all `.heic` files to `.jpg` format
- Preserve the original filename while changing the extension
