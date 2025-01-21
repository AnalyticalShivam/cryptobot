import cv2
import pytesseract
#import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# Function to analyze chart with price and timeframe detection
def analyze_crypto_chart_with_price_and_time(image_path):
    """
    Analyze a crypto chart, detect price, timeframe, and provide key insights.
    """
    # Load the image
    image = cv2.imread(image_path)

    # Resize for better readability if needed
    image = cv2.resize(image, (800, 600))

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Denoise and threshold for OCR
    processed = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )

    # Extract text using OCR
    ocr_result = pytesseract.image_to_string(processed)

    # Split OCR result into lines
    ocr_lines = ocr_result.splitlines()

    # Initialize variables for price and timeframe
    price_range = []
    timeframes = []

    # Parse text for potential price and timeframe labels
    for line in ocr_lines:
        line = line.strip()
        if line:
            # Detect price range (numbers with decimals, e.g., 0.12345 or 40000.5)
            if any(c.isdigit() for c in line) and '.' in line:
                try:
                    price_range.append(float(line))
                except ValueError:
                    pass

            # Detect timeframes (common crypto chart formats like "15:30", "1H", "1D")
            if any(char.isdigit() for char in line) and any(char in ":DH" for char in line):
                timeframes.append(line)

    # Analyze price range
    if price_range:
        min_price = min(price_range)
        max_price = max(price_range)
    else:
        min_price = max_price = None

    # Analyze timeframes
    timeframe_summary = ", ".join(set(timeframes)) if timeframes else "Not detected"

    # Detect candlestick patterns for insights
    edges = cv2.Canny(gray, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    candlesticks = [
        cv2.boundingRect(c)  # Extract bounding box (x, y, width, height)
        for c in contours
        if len(c) > 0  # Make sure the contour has valid points
    ]

    # Filter candlestick-like shapes based on aspect ratio and height
    candlesticks = [
        (x, y, w, h) for (x, y, w, h) in candlesticks
        if 0.1 < (w / h) < 0.5 and h > 10  # Filter based on aspect ratio and height
    ]

    # Insights
    insights = []
    if min_price and max_price:
        insights.append(f"Price range: {min_price:.2f} to {max_price:.2f}")
    if candlesticks:
        insights.append(f"Detected {len(candlesticks)} candlesticks.")
        insights.append(
            "Possible uptrend detected." if len(candlesticks) > 10 else "Sideways trend detected."
        )
    else:
        insights.append("No significant candlesticks detected.")

    # Results
    results = {
        "Key Observations": {
            "Price Range": f"{min_price:.2f} - {max_price:.2f}" if min_price and max_price else "Not detected",
            "Timeframes": timeframe_summary,
        },
        "Insights": insights,
    }

    return results


# Example usage
image_path = "tradingcharts.jpg"
results = analyze_crypto_chart_with_price_and_time(image_path)

# Print results
print("Key Observations:")
for key, value in results["Key Observations"].items():
    print(f"- {key}: {value}")

print("\nInsights:")
for insight in results["Insights"]:
    print(f"- {insight}")
