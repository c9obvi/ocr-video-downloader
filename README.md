# Video Text Extractor Using yt-dlp, OpenCV, and Tesseract OCR

This project demonstrates how to download videos using `yt-dlp` and then extract text from these videos using OpenCV and Tesseract OCR.

## Features

- **Video Download**: Download videos from various platforms using `yt-dlp`.
> [!NOTE]
> Specifically using another script I wrote [RepoHere](https://github.com/c9obvi/PyMP4-Downloader)
- **Text Extraction**: Extract text from the downloaded videos with Tesseract OCR.

## Requirements

- Python 3.x
- OpenCV (for video processing)
- pytesseract (Python wrapper for Tesseract OCR)
- yt-dlp (for downloading videos)
- Tesseract OCR engine

## Setup
run the following command to install these packages:

```bash
pip install -r requirements.txt
```

 ## Install Tesseract OCR:

   - **macOS**: Use Homebrew to install Tesseract:
     ```bash
     brew install tesseract
     ```
   - **Linux**: Use the package manager, e.g., for Debian/Ubuntu:
     ```bash
     sudo apt-get install tesseract-ocr
     ```
> [!IMPORTANT]  
> For Windows, installation instructions will vary.

## Usage Text Extraction from Video

This script extracts text from the downloaded video.

### Running the Application

1. **Download a Video**: Run `python mp4-dl.py` and enter the video URL when prompted.
2. **Extract Text**: Run `python main.py`. The extracted text will be saved in `OCR-OUTPUT.txt`.

> [!NOTE]
> Ensure Tesseract is correctly installed and available in your system's PATH.
 - The interval for frame extraction can be adjusted in the script.
 - Additional image preprocessing might be necessary for better OCR accuracy.


If you have any questions, please feel free to reach out here by opening an issue or via X [0xBerto](https://x.com/0xberto)