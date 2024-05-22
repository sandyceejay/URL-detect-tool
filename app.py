from flask import Flask, request, render_template
import joblib
import re

def custom_tokenizer(url):
    return re.split(r'\W+', url)

app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load('phishing_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    features = vectorizer.transform([url])
    prediction = model.predict(features)[0]
    
    # Analyze the URL to provide additional feedback
    analysis = {
        'has_https': 'https' in url,
        'num_dots': url.count('.'),
        'url_length': len(url),
        'hostname_length': len(url.split('/')[2]) if '/' in url else len(url)
    }

    # Display different messages based on the classification
    if prediction == 0:
        prediction_text = 'Legitimate'
    else:
        prediction_text = 'Phishing'

    return render_template('index.html', prediction_text=prediction_text, analysis=analysis)

if __name__ == '__main__':
    app.run(debug=True)
