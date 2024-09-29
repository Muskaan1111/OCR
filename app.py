import streamlit as st
import pytesseract
from PIL import Image
import re
import os

# Function to find the Tesseract executable path
def find_tesseract_path():
    possible_paths = [
        '/opt/homebrew/bin/tesseract',  # Homebrew path for Tesseract on macOS M1/M2
        '/usr/local/bin/tesseract'  # Default path for Tesseract on macOS Intel
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None

# Set Tesseract executable path
tesseract_path = find_tesseract_path()
if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
else:
    st.error("Tesseract not found. Please install Tesseract OCR.")

# Function to search for a keyword in the text
def searchWord(text, keyword):
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    matches = [(match.start(), match.end()) for match in pattern.finditer(text)]
    return matches

# Title and description
st.markdown(
    "<h1 style='color: white; text-decoration: underline; text-decoration-color: yellow;'>"
    "Our OCR Web Application App which extracts text from an image and searches for keywords"
    "</h1>", 
    unsafe_allow_html=True
)

# File uploader for the image
File_image = st.file_uploader(label="Upload your image here !!!", type=["jpg", "png", "jpeg"])

if File_image:
    st.write(File_image.type)
    
    if "image" in File_image.type:
        img = Image.open(File_image)
        st.image(img, caption="Uploaded Image")

        try:
            # Extract text in both English and Hindi
            text = pytesseract.image_to_string(img, lang='eng+hin')

            # Display extracted text
            st.markdown(
                "<h3 style='color: blue; text-decoration: underline; text-decoration-color: yellow;'>"
                "The extracted text from the image is:"
                "</h3>", 
                unsafe_allow_html=True
            )
            st.write(text)

            # Keyword search functionality
            keyword = st.text_input("Enter a keyword to search in the extracted text")
            if keyword:
                st.markdown(
                    "<h3 style='color: green; text-decoration: underline; text-decoration-color: orange;'>"
                    "The search output from the extracted text is:"
                    "</h3>", 
                    unsafe_allow_html=True
                )
                
                matches = searchWord(text, keyword)
                if matches:
                    highlighted_text = text
                    for start, end in reversed(matches):  # Highlight matches in reverse to avoid shifting indexes
                        highlighted_text = highlighted_text[:start] + '**' + highlighted_text[start:end] + '**' + highlighted_text[end:]
                    st.markdown(highlighted_text.replace('\n', '  \n'))  # Display text with bold highlighting
                else:
                    st.write("Keyword not found in the extracted text.")
        except pytesseract.TesseractError as e:
            st.error(f"An error occurred during OCR: {e}")
    else:
        st.error("Uploaded file is not an image.")
