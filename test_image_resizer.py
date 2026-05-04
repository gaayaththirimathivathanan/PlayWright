import csv
import os
from playwright.sync_api import sync_playwright, TimeoutError

def run_test():
    # Setup paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    results_dir = os.path.join(base_dir, "results")
    os.makedirs(results_dir, exist_ok=True)
    
    file_path = os.path.join(base_dir, "sample.png")
    csv_file = os.path.join(base_dir, "execution_results.csv")
    
    # Create a dummy sample.png if it doesn't exist to ensure the script can run independently
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82')

    with sync_playwright() as p:
        # Launch browser (set headless=True to run without UI)
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        status = "Fail"
        preview_detected = "No"
        screenshot_path = ""

        try:
            print("Navigating to the Image Resizer page...")
            page.goto("https://www.pixelssuite.com/image-resizer", timeout=60000)
            
            # Wait for the file input to be available
            print("Uploading sample.png...")
            file_input = page.locator("input[type='file']")
            file_input.wait_for(state="attached", timeout=10000)
            file_input.set_input_files(file_path)

            # Wait for preview image to appear
            print("Waiting for image preview...")
            # Using generic selectors to identify an image preview appearing dynamically
            preview_locator = page.locator("img[src^='blob:'], img[src^='data:'], canvas, .preview-container img, img[alt*='preview']")
            
            try:
                # Wait up to 15 seconds for the preview to be visible
                preview_locator.first.wait_for(state="visible", timeout=15000)
                preview_detected = "Yes"
                status = "Pass"
                screenshot_filename = "preview_pass.png"
                print("Preview detected successfully!")
            except TimeoutError:
                preview_detected = "No"
                status = "Fail"
                screenshot_filename = "preview_fail.png"
                print("Preview not detected within timeout.")

            # Take screenshot
            screenshot_path = os.path.join("results", screenshot_filename)
            page.screenshot(path=os.path.join(base_dir, screenshot_path))
            print(f"Screenshot saved to {screenshot_path}")

        except Exception as e:
            print(f"Test encountered an error: {e}")
            status = "Error"
            screenshot_path = "N/A"
        
        finally:
            browser.close()
            
            # Log results to CSV
            file_exists = os.path.isfile(csv_file)
            
            with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                if not file_exists:
                    # Write header
                    writer.writerow(["file_type", "file_path", "preview_detected", "status", "screenshot"])
                
                writer.writerow(["PNG", "sample.png", preview_detected, status, screenshot_path])
            
            print(f"Results logged to {csv_file}")

if __name__ == "__main__":
    run_test()
