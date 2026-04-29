# Test Automation UI

This repository contains a Playwright test script for automating a test scenario to verify the preview functionality of image format conversion on [pixelssuite.com](https://www.pixelssuite.com/convert-to-png).

## Prerequisites

1. **Python 3.8+**
2. **pip** (Python package installer)

## Installation

1. Install required dependencies:
   ```bash
   pip install playwright
   ```
2. Install Playwright browsers:
   ```bash
   playwright install chromium
   ```

## Running the Tests

To run the automated script and generate the execution results:
```bash
python image_preview_test.py
```
To run the script in headless mode (no browser UI):
```bash
python image_preview_test.py --headless
```

## Results
The test will execute and append its results to `execution_results.csv` and any generated screenshots will be saved in the `results/` folder.
