# URL-detect-tool

A tool to detect phishing and legitimate URLs.

## Phishing URL Detector

This project contains a tool to detect phishing URLs using a trained machine-learning model.

## Files

- `app.py`: Main application script.
- `train_model.py`: Script to train the model.
- `phishing.csv`: Dataset used for training.
- `feature_list.pkl`: Pickle file containing the feature list.
- `phishing_model.pkl`: Trained phishing model.
- `url_phishing_detector.pkl`: Pickle file of the URL phishing detector.
- `vectorizer.pkl`: Vectorizer for transforming URL text data.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sandyceejay/URL-detect-tool.git
    cd URL-detect-tool
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the main application script:
    ```bash
    python app.py
    ```

2. Follow the prompts to input a URL and check if it's phishing or legitimate.

## Training the Model

If you want to retrain the model, run the `train_model.py` script:
```bash
python train_model.py
