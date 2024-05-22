import pandas as pd
import re
from urllib.parse import urlparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

def load_data(filepath):
    try:
        data = pd.read_csv(filepath)
        print("Columns in the dataset:", data.columns)
        return data
    except Exception as e:
        print("Error loading data:", e)
        return None

def custom_tokenizer(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path.split('/') if parsed_url.path else []
    query = parsed_url.query.split('&') if parsed_url.query else []
    
    domain_tokens = re.split(r'\W+', domain.replace('.', ''))
    path_tokens = [token for segment in path for token in re.split(r'\W+', segment)]
    query_tokens = [token for parameter in query for token in re.split(r'\W+', parameter)]
    
    return domain_tokens + path_tokens + query_tokens

def label_mapper(label):
    return 0 if label == 'good' else 1

def train_model(data_path):
    data = load_data(data_path)
    if data is not None:
        try:
            vectorizer = TfidfVectorizer(tokenizer=custom_tokenizer, max_features=10000)
            X = vectorizer.fit_transform(data['URL'])
            y = data['Label'].map(label_mapper)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            model = LogisticRegression(max_iter=1000)
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)
            print(classification_report(y_test, predictions))

            joblib.dump(model, 'phishing_model.pkl')
            joblib.dump(vectorizer, 'vectorizer.pkl')
            print("Model and vectorizer saved successfully.")
        
        except KeyError as ke:
            print(f"KeyError: Check if the dataset has the column {ke}")
        except Exception as e:
            print("Error during model training or saving:", e)

if __name__ == '__main__':
    train_model('phishing.csv')
