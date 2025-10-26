import os
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
import joblib

from feature import FeatureExtraction


def find_csv():
    base = os.path.dirname(__file__)
    candidates = [
        os.path.join(base, 'phishing.csv'),
        os.path.join(base, '..', 'ml_model', 'phishing.csv'),
        os.path.join(base, '..', 'ml_model', 'phishing.csv'),
    ]
    for p in candidates:
        p = os.path.abspath(p)
        if os.path.exists(p):
            return p
    raise FileNotFoundError('phishing.csv not found in backend or ../ml_model')


def load_data(csv_path):
    df = pd.read_csv(csv_path)
    return df


def extract_features_if_urls(df):
    # If the CSV already contains numeric features (no URL column), use them directly.
    # Otherwise, try to extract features from a URL column (common names: url, URL, link).
    url_cols = [c for c in df.columns if c.lower() in ('url', 'link')]
    if len(url_cols) == 0:
        return None

    url_col = url_cols[0]
    X = []
    for u in df[url_col].fillna(''):
        fe = FeatureExtraction(u)
        X.append(fe.getFeaturesList())
    X = pd.DataFrame(X)
    return X


def main():
    csv_path = find_csv()
    df = load_data(csv_path)

    # Prefer to extract features using FeatureExtraction if a URL column exists.
    X_urls = extract_features_if_urls(df)
    if X_urls is not None:
        X = X_urls
        y = df.get('class')
    else:
        # CSV already contains features: drop index-like and class columns
        X = df.drop(columns=['Index', 'index', 'class'], errors='ignore')
        if 'class' in df.columns:
            y = df['class']
        else:
            raise KeyError('Target column "class" not found in CSV')

    # Quick, small model for speed
    clf = GradientBoostingClassifier(n_estimators=50, random_state=42)
    clf.fit(X, y)

    # Save model to project root as model.pkl
    out_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    out_path = os.path.join(out_dir, 'model.pkl')
    joblib.dump(clf, out_path)

    print('Model retrained successfully!')


if __name__ == '__main__':
    main()
