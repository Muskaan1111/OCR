# OCR
Web application  which extracts text from an image and searches for keywords

# How to setup 
First of all create a python virtual environment in which you will install packages
```
virtualenv ocr_env
```

activate the virtual env

```
source ./ocr_env/bin/activate
```

## install tesseract in your system
```
sudo apt update
```

```
sudo apt install tesseract-ocr
```

## install python packages
```
pip3 install -r requirements.txt
```

## now run the app using command

```
streamlit run app.py
```

