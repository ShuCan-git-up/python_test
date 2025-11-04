# Python Test Project

## Project Overview

This is a Python learning and practice repository containing multiple Python application examples across different domains:

1. **Machine Learning/Data Analysis** - Iris Dataset Analysis
2. **Computer Vision** - Face Recognition and Facial Feature Processing
3. **Web Scraping** - TV Program Information Crawler

## Project Structure

```
python_test/
├── web/                          # Web-related code
│   └── src/
│       ├── face_recognition/     # Face recognition module
│       ├── main_face/           # Facial feature processing
│       ├── main/                # Web scraping code
│       └── request/             # HTTP request examples
├── *.ipynb                      # Jupyter Notebook files
├── iris.data                    # Iris dataset
└── README.md                    # Project documentation
```

## Main Features

### 1. Iris Data Analysis (莺尾花分析.ipynb)

**Description:**
- Classic machine learning introduction project using the famous Iris dataset
- Includes data visualization, statistical analysis, and basic machine learning operations

**Key Content:**
- Data loading and preprocessing
- Exploratory Data Analysis (EDA)
  - Distribution histograms for sepal length/width
  - Distribution histograms for petal length/width
  - Petal scatter plot analysis
- Data visualization
  - Various charts using matplotlib
  - Pairplot analysis using seaborn
- Feature engineering
  - Creating new features (e.g., petal area)
  - Label mapping
- Statistical modeling
  - Linear regression analysis using statsmodels (OLS)

**Tech Stack:**
- pandas - Data processing
- matplotlib - Data visualization
- seaborn - Advanced visualization
- numpy - Numerical computing
- statsmodels - Statistical modeling
- requests - Data download

---

### 2. Face Recognition System (web/src/face_recognition/)

**Description:**
A deep learning-based real-time face recognition system that can identify faces from camera and match against a database.

**Core Files:**

#### `face_reco_from_camera.py` - Real-time Face Recognition
- **Function:** Capture from camera, detect faces and match with stored features
- **Technology:**
  - dlib for face detection
  - Pre-trained ResNet model for 128D face feature extraction
  - Euclidean distance for similarity measurement
  - Real-time video stream processing
- **Key Features:**
  - Multi-face detection support
  - Real-time feature extraction
  - Face matching (threshold: 0.4)
  - Video annotation and display

#### `get_face_from_camera.py` - Face Collection
- Collect face samples from camera
- Save face images for training

#### `get_features_into_csv.py` - Feature Extraction
- Extract 128D face feature vectors
- Save features to CSV file
- Build face feature database

#### `rgb2gray.py` - Image Preprocessing
- RGB to grayscale conversion
- Image preprocessing utilities

**Model Files:**
- `dlib_face_recognition_resnet_model_v1.dat` - Face recognition model (22MB)
- `shape_predictor_68_face_landmarks.dat` - 68-point facial landmark model (95MB)
- `shape_predictor_5_face_landmarks.dat` - 5-point facial landmark model (9MB)

---

### 3. Facial Feature Processing (web/src/main_face/)

**Description:**
Face beautification and feature analysis toolkit

#### `face_beauty.py` - Digital Makeup
- **Function:** Apply digital makeup effects to faces in photos
- **Effects:**
  - Eyebrow rendering
  - Lipstick effect
  - Eye shadow effect
  - Eyeliner effect
- **Technology:** face_recognition library and PIL for image processing

#### `face_to_match.py` - Face Matching
- Face similarity comparison
- Face verification

#### `features.py` - Feature Extraction
- Extract facial keypoints
- Facial feature analysis

#### `find_all_face_show.py` - Multi-face Detection
- Detect all faces in image
- Annotate and display face locations

#### `draw.py` - Drawing Tools
- Facial landmark visualization
- Auxiliary drawing functions

---

### 4. Web Scraping Module (web/src/main/)

**Description:**
Web scrapers for TV program information

#### `tvmao.py` - TVMao Website Scraper
- **Target:** https://www.tvmao.com
- **Features:**
  - Scrape provincial TV station information
  - Get TV program listings
  - Save data to Excel files
- **Tech Stack:**
  - requests - HTTP requests
  - BeautifulSoup4 - HTML parsing
  - xlwt - Excel file writing
  - Tkinter - GUI interface (example)

#### `tvopen.py` - TV Streaming Website Scraper
- **Target:** http://www.tvyan.com
- **Features:**
  - Scrape TV station lists
  - Get station descriptions
  - Download station icons
  - Save to Excel files
- **Characteristics:**
  - Recursive multi-page crawling
  - Automatic deduplication
  - Data persistence

#### `open_province_url.py` - Provincial TV URLs
- Collect provincial TV station streaming links
- Data organization and storage

#### Other Test Files
- `test1.py`, `test2_opt.py`, `test3.py`, `test4.py` - Various test scripts
- `loss.py`, `power.py` - Utility functions

---

### 5. HTTP Request Examples (web/src/request/)

#### `request1.py` - Data Request and Processing
- **Features:**
  - Download Iris dataset from UCI ML repository
  - Data analysis using pandas
  - Data visualization (histograms)
- **Example Code:**
  - GitHub API calls
  - Statistical analysis
  - DataFrame operations
  - Data filtering and querying

---

## Technology Stack Summary

### Data Science & Machine Learning
- **pandas** - Data processing and analysis
- **numpy** - Numerical computing
- **matplotlib** - Basic visualization
- **seaborn** - Advanced statistical visualization
- **statsmodels** - Statistical modeling

### Computer Vision
- **dlib** - Face detection and recognition
- **OpenCV (cv2)** - Image processing and video streams
- **face_recognition** - High-level face recognition API
- **PIL/Pillow** - Image processing

### Web Scraping
- **requests** - HTTP request library
- **BeautifulSoup4** - HTML/XML parsing
- **urllib3** - URL handling
- **xlwt** - Excel file operations

### GUI
- **Tkinter** - Python standard GUI library

---

## Datasets

### Iris Dataset (iris.data)
- **Source:** UCI Machine Learning Repository
- **Size:** 150 samples
- **Features:** 4 numerical features (sepal length, sepal width, petal length, petal width)
- **Classes:** 3 iris species (Setosa, Versicolor, Virginica)
- **Purpose:** Classic machine learning classification problem

---

## Project Highlights

1. **Multi-domain Coverage:** Spans data analysis, computer vision, and web scraping
2. **Practical Applications:** Contains runnable real-world examples
3. **Educational Value:** Suitable for Python beginners as learning reference
4. **Clear Code Structure:** Modular organization, easy to understand and extend

---

## Usage Instructions

### Environment Setup
```bash
# Main dependencies
pip install pandas numpy matplotlib seaborn
pip install requests beautifulsoup4 xlwt
pip install opencv-python dlib face_recognition
pip install statsmodels jupyter
```

### Face Recognition System Usage
1. Run `get_face_from_camera.py` to collect face samples
2. Run `get_features_into_csv.py` to extract and save features
3. Run `face_reco_from_camera.py` to start real-time recognition

### Data Analysis
- Open `莺尾花分析.ipynb` with Jupyter Notebook
- Execute cells sequentially

### Web Scraping
- Run `tvmao.py` or `tvopen.py`
- Results will be saved as Excel files

---

## Important Notes

1. **Path Configuration:** Code contains hardcoded local paths (e.g., `/Users/shucan/...`), modify according to your environment
2. **Model Files:** Face recognition requires pre-downloaded dlib model files
3. **Python Version:** Some code may require Python 2.x (e.g., Tkinter import), recommend Python 3.x with appropriate modifications
4. **Web Scraping:** Please follow robots.txt protocol and website terms of service

---

## Learning Path Suggestions

1. **Beginners:** Start with Iris data analysis to learn data processing and visualization
2. **Intermediate:** Try face recognition system to understand computer vision applications
3. **Advanced:** Run web scrapers to learn data collection and processing

---

## Author Information

- **Author:** ShuCan
- **Purpose:** Python learning and practice

---

## Summary

This is a comprehensive Python learning project that demonstrates Python applications in different domains (data analysis, computer vision, web scraping) through three main application areas. The code is practical and suitable for learning reference and hands-on practice.
