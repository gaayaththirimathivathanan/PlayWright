# PixelsSuite Test Automation

This repository contains Playwright test scripts for automating test scenarios for the [PixelsSuite](https://www.pixelssuite.com/) platform.

## 1. Image Resizer Automation

This script tests the image preview functionality of the [PixelsSuite Image Resizer](https://www.pixelssuite.com/image-resizer) tool. It verifies that when an image is uploaded, a preview image successfully renders on the webpage.

### Prerequisites
- Python 3.8+ installed on your system.

### Setup Instructions
1. **Navigate to the project directory**:
   ```bash
   cd path/to/your/folder
   ```
2. **Install Required Python Dependencies:**
   ```bash
   pip install playwright openpyxl
   ```
3. **Install Playwright Browsers:**
   ```bash
   playwright install chromium
   ```

### Running the Test
To execute the automation script, simply run:
```bash
python test_image_resizer.py
```

## 2. Image Format Conversion Automation (Convert to PNG)

This script verifies the preview functionality of image format conversion on [pixelssuite.com/convert-to-png](https://www.pixelssuite.com/convert-to-png).

### Running the Tests
To run the automated script and generate the execution results:
```bash
python image_preview_test.py
```
To run the script in headless mode (no browser UI):
```bash
python image_preview_test.py --headless
```

### Results
For both tests, execution summaries are logged directly into `execution_results.csv`, and any generated screenshots are saved in the `results/` folder.
