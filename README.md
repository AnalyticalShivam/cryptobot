# Chart Analysis Code Documentation

## Overview
This code is designed to process a chart image, extract meaningful information like price ranges and timeframes, and analyze candlestick patterns to infer market trends. Below is a breakdown of its functionality, setup process, and pending improvements.

---

## Features

### 1. **Image Preprocessing**
- Reads and resizes the chart image provided in `image_path`.
- Converts the image to grayscale for easier processing.
- Applies thresholding to enhance text and other elements in the image.

### 2. **Text Extraction (OCR)**
- Uses Tesseract OCR to detect and extract text from the image.
- Breaks the extracted text into lines for analysis.
- Searches for numeric values with decimals to identify price ranges.
- Searches for time-related patterns to detect timeframes.

### 3. **Candlestick Detection**
- Identifies potential candlestick shapes by detecting edges and contours in the image.
- Filters shapes based on size and proportions to identify candlestick-like patterns.

### 4. **Insights Generation**
- Summarizes the price range (minimum and maximum prices detected).
- Summarizes the detected timeframes.
- Analyzes the number of candlesticks to infer trends:
  - Many candlesticks: Possible uptrend.
  - Few candlesticks: Possible sideways trend.

### 5. **Output**
- Prints observations such as price range, detected timeframes, number of candlesticks, and potential market trends.

---

## Example Output
**Input:** An image of a crypto chart.

**Output:**
```
Key Observations:
Price Range: 20000.50 - 45000.75
Timeframes: 1H, 1D

Insights:
Detected 12 candlesticks.
Possible uptrend detected.
```

---

## Pending Work

1. **Integration with Telegram**
   - Develop functionality to integrate the code with a Telegram bot to allow users to upload chart images and receive insights directly.

2. **Enhancements**
   - Improve OCR functionality to better extract price ranges and timeframes from complex images.
   - Refine candlestick detection to increase accuracy.

---

## Setup Instructions

### 1. **Prerequisites**
- Install **PyCharm IDE**.
- Install the following dependencies:
  - `opencv-python`
  - `pytesseract`

### 2. **Install Tesseract OCR**
- Download and install Tesseract OCR from [SourceForge](https://sourceforge.net/projects/tesseract-ocr.mirror/).
- Ensure that Tesseract is added to your system's PATH.

### 3. **Run the Code**
- Upload the chart image to the project directory or provide its path.
- Drag and drop the image into the PyCharm IDE project directory.
- Click the **Run** icon in the upper-right corner of PyCharm to execute the code.

---

## Notes
- Ensure all dependencies are installed before running the code.
- For best results, use high-quality images with clear text and candlestick patterns.

---

## Contribution
Feel free to contribute to this project by:
- Fixing the pending issues mentioned above.
- Optimizing the code for better performance.
- Extending functionality, such as integrating additional chart analysis features.

---

## License
This project is open-source and available for use and modification.

---

## Contact
For any queries or contributions, please raise an issue or submit a pull request on GitHub.

