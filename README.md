# Waterfall Classifier Project - Ultimate Predictor (v3.5cnn-lite)

This project demonstrates binary classification of standard SATNOGS waterfall data based on the presence of signal in the images using a Convolutional Neural Network (CNN) trained over data from multiple satellites downloaded using the SATNOGS API.

The current "lite" version extracts the model and prediction modules from the main project. It has only the essential files and focuses on smaller file sizes and user convenience. Users will interact with the program using terminal command lines.

A report of this project maybe found in this repository. Email Tata Li at tlofbj.public@outlook.com for further questions or suggestions!

## Versions

* **3.5 (CNN) Lite** - Able to classify single or a directory of images from either an image file path or a valid observation ID. Includes only the predicting module with a simpler and more versatile user interface. Uses model `model_2025-05-08T17-34-36.pth` from v3.0 for making predictions. Final edit: May 15, 2025.
* **3.5 (CNN)** - Able to classify waterfalls. Includes three separate modules for training, evaluating, and predicting. In progress...
* **3.0 (CNN)** - Able to classify waterfalls of any satellite with significantly greater accuracy. Includes a more comprehensive logger. Training sample: 1650, accuracy 95.52%. Final edit: Apr 23, 2025.
* **2.0 (SVM)** - Able to classify waterfalls of any satellite. Includes logging and a API-based SATNOGS waterfall scraper. Training sample: 605 images, accuracy 69.5%. Final edit: Apr 10, 2025.
* **1.0 (SVM)** - Able to classify waterfalls of NOAA-19 satellite at 137.1 MHz only. Training sample: 44 images, accuracy 87.5% . Final edit: Feb 23, 2025.

## Usage

Setting Up Local Project
1. Clone this repository (https://github.com/tlofbj/waterfall-classifier-project-v3.5cnn-lite.git)
2. Create a virtual environment (optional but recommended)
3. Install the required dependencies: `pip install -r requirements.txt`

Obtaining Images
* Included in the `images` directory are a few sample images you can begin with. You may add images of interest into `images` or any directory of your choice. All images added should be unedited, uncropped, and unresized; the program will automatically modify it. Altering in any way from the standard downloadable may cause errors. Waterfalls after 2018-08-07 is preferred due to its updated color code.
* Run `python3 src/utils/scraper.py` in terminal to download the most recent standard waterfalls from SatNOGS. Use `-h` for further instructions.

Making Predictions
* Run this program with a python version compatible with PyTorch (torch), preferably 3.10.13.
* Run `python3 src/predict.py <IMG_PATH>` in terminal to predict an image of known path. 
* Run `python3 src/predict.py -o <OBSERVATION_ID>` in terminal to predict an image that can be downloaded from SatNOGS. Use `-h` for further instructions.
* Run `python3 src/predict_many.py` in terminal to generate and log predictions for all images in `images` into a `prediction_log.json` file. Use `-i` to change image directory. Use `-l` to change log file directory. Use `-h` for further instructions.

## Main Dependencies

* **torch** - Core PyTorch library.
* **torchvision** - Image datasets and transforms.
* **pillow (PIL)** - Image manipulation.
* **requests** - HTTP requests (for scraping).
* **termcolor** - Colored terminal output.
Please refer to requirements.txt on other dependencies...

## Contributors

This project was created by Tata Li and mentored by Mitch McLean. The first version began in February, 2025 as an independent research project with Hawai'i's Aspiring Aerospace Engineers Academy. 

