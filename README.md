# PixelsSuite Image Resizer Automation

This Playwright automation project is built to test the image preview functionality of the [PixelsSuite Image Resizer](https://www.pixelssuite.com/image-resizer) tool. It verifies that when an image is uploaded, a preview image successfully renders on the webpage.

## Prerequisites

- Python 3.8+ installed on your system.

## Setup Instructions

1. **Navigate to the project directory** where this file is located:
   ```bash
   cd path/to/your/folder
   ```

2. **Install Required Python Dependencies:**
   Install `playwright` (and optionally `openpyxl` if needed for your broader testing suite):
   ```bash
   pip install playwright openpyxl
   ```

3. **Install Playwright Browsers:**
   Playwright requires specific browser binaries to execute tasks. Install them by running:
   ```bash
   playwright install
   ```

## Running the Test

To execute the automation script, simply run:
```bash
python test_image_resizer.py
```

### What the script does:
1. Automatically creates a dummy `sample.png` file (if it isn't found).
2. Opens a visible Chromium browser instance and navigates to the image resizer.
3. Uploads the PNG file.
4. Waits up to 15 seconds for an image preview to appear dynamically.
5. Captures a screenshot to the `results/` folder (named `preview_pass.png` on success).
6. Logs the execution summary directly into `execution_results.csv`.
