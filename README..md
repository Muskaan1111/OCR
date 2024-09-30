# OCR
Web application  which extracts text from an image and searches for keywords
# How to Set for windows

## Step 1: Install Python and Set Up in Your System

### Command to install packages
```
pip install -r requirements.txt
```



## Firstly install Tesseract
### *For Windows*

1. Go to the Tesseract OCR GitHub page: [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract)
2. Scroll down to the "Installing Tesseract" section.
3. You can either install Tesseract via a pre-built binary package or build it from source.
4. Scroll down to the Windows section then: 
   [Click on UB-Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).

   
5.  Download the Tesseract installer:[ tesseract install(64 bit)](https://github.com/UB-Mannheim/tesseract/releases/download/v5.4.0.20240606/tesseract-ocr-w64-setup-5.4.0.20240606.exe)
6. After successful installation, set up Tesseract and add the Tesseract path to the environment variables.




## Step2 : Set up for Streamlit
*command for Windows:*
   ```pip install streamlit```


## Step3 : How to run the web application app
*command is:*
   ```streamlit run app.py```

# How to setup for linux
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

