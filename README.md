#  AI-Powered PPT to Study Notes Generator using OCR

An AI-powered Python application that converts **PowerPoint presentations into organized and easy-to-study notes** using text extraction and OCR technology.

The system extracts normal text from PPTX slides and uses **Tesseract OCR** to recognize text present inside images. The extracted content is organized into topics, bullet points, definitions, keywords, quick revision points, and a mind map. Finally, the generated study material can be downloaded as a **PDF file**.

---

##  Introduction

The **AI-Powered PPT to Study Notes Generator using OCR** is a Python-based application designed to convert PowerPoint presentations into **organized and easy-to-study notes**.

The application allows users to upload a **PPTX file**, extracts text from the slides, and uses **OCR (Optical Character Recognition)** to read text present inside images.

The extracted content is processed and organized into:

* Topics
* Bullet points
* Important definitions
* Important keywords
* Quick revision points
* Mind maps

The final study notes can be generated as a **PDF file** and downloaded by the user.

---

##  Objectives

* Automatically extract content from PowerPoint presentations.
* Extract text from image-based slides using OCR.
* Organize PPT content into readable study notes.
* Identify important headings and content.
* Generate important definitions and keywords.
* Create quick revision points.
* Generate a mind map from important keywords.
* Provide the final notes as a downloadable PDF.
* Reduce the time required for manually preparing study notes.

---

##  Features

*  PPTX file upload
*  PowerPoint text extraction
*  OCR support for image-based text
*  Automatic study notes generation
*  Topic and heading identification
*  Important definitions
*  Important keywords
*  Quick revision points
*  Mind map generation
*  PDF generation
*  Downloadable study notes
*  Streamlit web interface

---

##  System Workflow

```text
PPT/PPTX Upload
       ↓
Extract Slide Content
       ↓
Check Image-Based Content
       ↓
OCR using Tesseract
       ↓
Combine Extracted Text
       ↓
Identify Headings & Content
       ↓
Organize Study Notes
       ↓
Extract Definitions & Keywords
       ↓
Generate Mind Map
       ↓
Create PDF
       ↓
Download Study Notes
```

---

## Application preview
<img width="1358" height="709" alt="1" src="https://github.com/user-attachments/assets/8095d795-1f0e-4685-9493-1aa84aa5efa0" />
<img width="1352" height="578" alt="2" src="https://github.com/user-attachments/assets/10b150dc-22a4-48db-b869-335a56ad19f8" />
<img width="1344" height="653" alt="3" src="https://github.com/user-attachments/assets/c301daba-604f-4939-92d7-966270aa68d8" />
<img width="1352" height="617" alt="4" src="https://github.com/user-attachments/assets/1d747a56-67fc-4043-838d-e4cd987b187b" />
<img width="1338" height="687" alt="5" src="https://github.com/user-attachments/assets/38a88cb1-edb2-4957-b0d5-67638bf0465b" />



##  Technologies Used

| Technology    | Purpose                        |
| ------------- | ------------------------------ |
| Python        | Main programming language      |
| Streamlit     | Web application interface      |
| python-pptx   | PowerPoint text extraction     |
| Tesseract OCR | Extracting text from images    |
| pytesseract   | Python interface for Tesseract |
| OpenCV        | Image preprocessing            |
| Pillow        | Image processing               |
| NumPy         | Numerical and image operations |
| ReportLab     | PDF generation                 |

---

##  Project Structure

```text
AI-PPT-Study-Notes-Generator/
│
├── app.py
├── ppt_processor.py
├── ocr.py
├── notes_generator.py
├── pdf_generator.py
├── requirements.txt
│
└── output/
    └── Generated Study Notes PDF
```

---

##  File Description

### `app.py`

The main Streamlit application.

It handles:

* PPTX file upload
* Study notes generation
* Notes preview
* PDF generation
* PDF download

### `ppt_processor.py`

Responsible for extracting content from PowerPoint presentations.

It processes:

* Normal slide text
* Image-based content
* OCR extraction

### `ocr.py`

Handles Optical Character Recognition.

It uses:

* OpenCV
* NumPy
* Pillow
* Tesseract OCR

Image preprocessing is performed before extracting text.

### `notes_generator.py`

Converts extracted text into organized study notes.

It identifies:

* Headings
* Content
* Definitions
* Keywords
* Quick revision points

### `pdf_generator.py`

Generates the final study notes PDF.

The PDF contains:

* Study notes
* Important definitions
* Keywords
* Mind map
* Quick revision content

### `requirements.txt`

Contains the Python libraries required to install and run the project.

---

##  Installation

### Step 1: Open the Project

Open the project folder in **VS Code**.

```text
AI-PPT-Study-Notes-Generator
```

### Step 2: Create a Virtual Environment

Open PowerShell in VS Code and run:

```powershell
python -m venv .venv
```

### Step 3: Activate the Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell gives an execution policy error, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 4: Install Requirements

```powershell
python -m pip install -r requirements.txt
```

---

##  Tesseract OCR Installation

The project uses **Tesseract OCR** to extract text from images.

Install Tesseract OCR on Windows.

The default configuration uses:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

If Tesseract is installed in another location, update the path in:

```text
ocr.py
```

---

##  Run the Application

After activating the virtual environment, run:

```powershell
python -m streamlit run app.py
```

The application will open in your browser.

Usually:

```text
http://localhost:8501
```

---

##  How to Use

### Step 1

Open the Streamlit application.

### Step 2

Click:

```text
Upload your PowerPoint file
```

### Step 3

Select a `.pptx` file.

### Step 4

Click:

```text
Generate Study Notes
```

### Step 5

The application processes the PPT and extracts the content.

### Step 6

The generated notes are displayed in the application.

The output includes:

```text
Topics
   ↓
Bullet Points
   ↓
Important Definitions
   ↓
Important Keywords
   ↓
Mind Map
   ↓
Quick Revision
```

### Step 7

Click:

```text
Download Study Notes PDF
```

to download the generated study notes.

---

##  OCR Processing

OCR is used when important text is present inside images.

The OCR process is:

```text
Image in PPT
     ↓
Image Extraction
     ↓
Grayscale Conversion
     ↓
Image Resizing
     ↓
Noise Reduction
     ↓
Thresholding
     ↓
Tesseract OCR
     ↓
Extracted Text
```

This allows the application to process both:

* Normal PowerPoint text
* Image-based text

---

##  Study Notes Generation

The extracted content is processed and organized into different sections.

The system identifies possible headings based on:

* Short lines
* Uppercase text
* Numbered headings
* Text structure

The remaining content is converted into bullet points for easier reading and revision.

---

##  Important Definitions

The system detects definition-style content and displays it separately.

Example:

```text
Term: Definition
```

The definitions are shown under:

```text
Important Definitions
```

This makes the generated notes useful for examination preparation.

---

##  Important Keywords

Frequently occurring meaningful words are identified from the extracted content.

Example:

```text
tree
poet
casuarina
stanza
Toru
Dutt
```

These keywords can be useful for:

* Quick revision
* Exam preparation
* Topic identification

---

##  Mind Map

The application creates a visual mind map using important keywords.

Example:

```text
                  Main Topic
                      |
          -------------------------
          |           |           |
       Topic 1     Topic 2     Topic 3
          |           |           |
       Keyword     Keyword     Keyword
```

The mind map helps students understand relationships between important concepts.

---

##  PDF Output

The generated PDF contains organized study material such as:

```text
Study Notes
     ↓
Topics
     ↓
Important Definitions
     ↓
Important Keywords
     ↓
Mind Map
     ↓
Quick Revision
```

The PDF can be downloaded and used for offline study.

---

##  Advantages

* Saves time in preparing notes.
* Reduces manual note-taking.
* Supports image-based PPT content through OCR.
* Organizes large amounts of PPT content.
* Provides quick revision material.
* Generates downloadable PDF notes.
* Easy-to-use interface.
* Useful for students and examination preparation.

---

##  Applications

This project can be used for:

* College lecture notes
* Exam preparation
* Revision material
* Classroom presentations
* Educational content processing
* Study material generation
* Image-based presentation processing

---

##  Future Enhancements

The project can be improved by adding:

* AI-based summarization using an LLM.
* Automatic question-and-answer generation.
* Multiple language support.
* Voice-based study notes.
* Flashcard generation.
* Quiz generation.
* More advanced mind maps.
* Support for PDF and DOCX files.
* Improved PDF design and formatting.

---


##  Author

**Nikitha R**
B.Sc. Computer Science with Artificial Intelligence

---


