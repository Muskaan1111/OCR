import streamlit as st
import pytesseract
from PIL import Image
import re
import os

# Function to find the Tesseract executable path
def find_tesseract_path():
    possible_paths = [
        '/opt/homebrew/bin/tesseract'  # Homebrew path for Tesseract on macOS
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None

# Setting up Tesseract
tesseract_path = find_tesseract_path()
if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
else:
    st.error("Tesseract executable not found. Please install Tesseract OCR.")

# Function to extract text in both English and Hindi
def extract_text(image):
    # Specify languages as 'eng+hin' for dual-language extraction
    return pytesseract.image_to_string(image, lang='eng+hin')

# Function to search for keywords in the extracted text
def search_keywords(text, keyword):
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    matches = [(match.start(), match.end()) for match in pattern.finditer(text)]
    return matches

# Streamlit App
st.title("OCR and Keyword Search (English and Hindi)")

# Image upload
uploaded_image = st.file_uploader("Upload an image for OCR", type=["png", "jpg", "jpeg"])
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Extract text from the image (English and Hindi)
    extracted_text = extract_text(image)
    st.subheader("Extracted Text")
    st.write(extracted_text)

    # Keyword search
    keyword = st.text_input("Enter a keyword to search in the extracted text")
    if keyword:
        st.subheader("Search Results")
        matches = search_keywords(extracted_text, keyword)
        if matches:
            highlighted_text = extracted_text
            # Highlight matches
            for start, end in reversed(matches):  # Prevent index shifting by reversing
                highlighted_text = highlighted_text[:start] + '**' + highlighted_text[start:end] + '**' + highlighted_text[end:]
            st.markdown(highlighted_text.replace('\n', '  \n'))  # Markdown for bold highlighting
        else:
            st.write("No matches found.")
