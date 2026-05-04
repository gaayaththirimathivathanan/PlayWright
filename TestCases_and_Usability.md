# Task 1: Test Case Design (36 Test Cases)

| TC ID | Feature Tested | Input | Expected Output | Actual Output | Status | Assumptions |
|---|---|---|---|---|---|---|
| Pos_01 | Document conversion | Valid DOCX file (< 10MB) | Downloadable converted PDF file | Pending | Pending | Feature is online |
| Neg_01 | Document conversion | Corrupted DOCX file | "Invalid file" error message | Pending | Pending | Validation exists |
| Neg_02 | Document conversion | File exceeding max size limit (e.g., 500MB) | "File too large" error message | Pending | Pending | Max file size enforced |
| Pos_02 | PDF editing | Valid PDF file, add text | PDF updates with new text and can be saved | Pending | Pending | Browser supports PDF canvas |
| Neg_03 | PDF editing | Password-protected PDF | Prompt for password or error message | Pending | Pending | System checks encryption |
| Neg_04 | PDF editing | Try saving without making edits | "No changes made" message or disabled save button | Pending | Pending | UI state management exists |
| Pos_03 | Image resizing | Valid JPG, scale to 50% | Downloadable JPG at half original dimensions | Pending | Pending | Correct resizing logic |
| Neg_05 | Image resizing | Negative dimension inputs (-100px) | Validation error, unable to process | Pending | Pending | Input fields sanitize data |
| Neg_06 | Image resizing | Non-image file upload (.txt) | "Unsupported format" error message | Pending | Pending | Format validation on upload |
| Pos_04 | Cropping (Crop PNG) | Valid PNG, select 100x100 area | Downloadable cropped PNG of 100x100 | Pending | Pending | Canvas interaction works |
| Neg_07 | Cropping (Crop PNG) | Select a 0x0 area | "Selection too small" error or disabled apply button | Pending | Pending | Minimum crop area enforced |
| Neg_08 | Cropping (Crop PNG) | Upload a WebP image | "Only PNG supported" error message | Pending | Pending | Strict format restriction |
| Pos_05 | Compression (PNG) | 5MB PNG file, standard compression | Compressed PNG file, size reduced | Pending | Pending | Compression algorithm active |
| Neg_09 | Compression (PNG) | Already heavily compressed 10KB PNG | "Cannot compress further" info message | Pending | Pending | Smart compression check |
| Neg_10 | Compression (PNG) | Corrupted PNG file | "Invalid image data" error | Pending | Pending | Image parsing verification |
| Pos_06 | Image format conversion| Valid PNG file, target JPG | Downloadable JPG file matching source image | Pending | Pending | Encoding libraries active |
| Neg_11 | Image format conversion| Upload unsupported format (.exe) | Error message rejecting the upload | Pending | Pending | MIME type checking |
| Neg_12 | Image format conversion| Select PNG as target for PNG image | "Already in target format" message | Pending | Pending | Format redundancy check |
| Pos_07 | Meme generation | Valid image, Top: "Hello", Bottom: "World" | Downloadable image with text overlay | Pending | Pending | Text rendering functional |
| Neg_13 | Meme generation | Generate meme without uploading image | "Please upload an image" error | Pending | Pending | Mandatory field validation |
| Neg_14 | Meme generation | Entering extremely long text (1000+ chars) | Text truncation or "Text too long" error | Pending | Pending | Text length limits enforced |
| Pos_08 | Color picker | Valid image, click on pure red pixel | Hex code `#FF0000` is displayed | Pending | Pending | Pixel data is accessible |
| Neg_15 | Color picker | Click picker before image finishes loading | Picker disabled or loading indicator | Pending | Pending | Async state handling |
| Neg_16 | Color picker | Click on a completely transparent area | Hex code `#00000000` or 'Transparent' | Pending | Pending | Alpha channel support |
| Pos_09 | Image rotation | Valid image, rotate 90° clockwise | Downloadable image rotated 90° | Pending | Pending | Canvas rotation logic works |
| Neg_17 | Image rotation | Enter non-numeric angle "ABC" | Input rejected or validation error | Pending | Pending | Type enforcement on input |
| Neg_18 | Image rotation | Rotate image exceeding max supported res | "Image too large to rotate" error | Pending | Pending | Memory limit safety |
| Pos_10 | Image flipping | Valid image, apply horizontal flip | Downloadable mirrored image | Pending | Pending | Canvas flip logic works |
| Neg_19 | Image flipping | Apply flip without uploading image | Disabled button or "Upload image first" | Pending | Pending | State dependency check |
| Neg_20 | Image flipping | Click flip button 50 times rapidly | UI handles queue or disables button temporarily | Pending | Pending | Rate limiting / debouncing |
| Pos_11 | Usability - Mobile | Open site on mobile viewport (375px width)| Elements resize properly, no horizontal scroll | Pending | Pending | Responsive CSS used |
| Neg_21 | Usability - JS disabled| Disable JS in browser and load site | Fallback message "Please enable JS" | Pending | Pending | No-script tags implemented |
| Pos_12 | Functionality - Navigation| Click 'More' dropdown in header | Dropdown opens showing sub-tools | Pending | Pending | Navigation scripts working |
| Neg_22 | Functionality - Timeout| Throttle network to 'Slow 3G', upload 20MB | Clean timeout error instead of infinite hang | Pending | Pending | Timeout handles implemented |
| Pos_13 | Usability - Accessibility| Navigate site using Tab key only | Focus rings visible on all interactive elements | Pending | Pending | ARIA and focus styles set |
| Neg_23 | Usability - Contrast | Test primary buttons with contrast checker | Pass WCAG AA (Contrast ratio >= 4.5:1) | Pending | Pending | Accessible color palette |

---

# Task 4: Usability Weaknesses

Based on typical usability testing principles (like Nielsen's heuristics: clarity, consistency, ease of use), here are 5 expected usability weaknesses on such a platform:

1. **Visibility of System Status (Lack of Progress Indicators):** During potentially slow operations like Document Conversion or heavy PNG Compression, the site might lack an estimated time remaining or a detailed progress bar. Users might assume the website has frozen if it takes too long.
2. **Help Users Recognize, Diagnose, and Recover from Errors:** If a user uploads an incorrect file format (e.g., `.exe` in an image resizer), the system might fail silently or provide a vague "Upload Failed" error rather than specifically stating "Invalid format: Please upload a PNG or JPG".
3. **User Control and Freedom (No Undo Button):** In interactive tools like PDF Editing, Meme Generation, or Cropping, making a mistake usually forces the user to clear the canvas or re-upload the original image because a simple `Ctrl+Z` or "Undo" button is often not implemented.
4. **Discoverability (Burying Core Features):** Storing several useful tools (Meme generation, Color picker, Flip/Rotate) strictly under a single "More" dropdown significantly reduces their discoverability. Users looking for a specific tool might leave the site before finding it.
5. **Flexibility and Efficiency of Use (Lack of Batch Processing):** Tools like Image Resizing or Format Conversion often only accept one file at a time. This severely degrades usability for power users needing to resize or compress multiple images simultaneously.
