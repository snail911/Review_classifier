import joblib
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


class ReviewModel:
    def __init__(self):
        self.loaded_model = joblib.load('model/model1.pkl')
        self.loaded_vectorizer = joblib.load('model/tfidf_vectorizer1.pkl')
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words('english'))

    def preprocess_text(self, text):

        tokens = word_tokenize(text.lower())
        tokens = [token for token in tokens if token.isalpha() and token not in self.stop_words]
        for i in range(len(tokens)):
            if tokens[i] == 'not' and i + 1 < len(tokens):
                tokens[i + 1] = 'not_' + tokens[i + 1]
        tokens = [self.stemmer.stem(token) for token in tokens]
        return " ".join(tokens)

    def preprocess_review_text(self, review_text):

        new_data = review_text

        loaded_model = self.loaded_model
        loaded_vectorizer = self.loaded_vectorizer

        preprocessed_new_data = self.preprocess_text(new_data)
        X_new_data = loaded_vectorizer.transform([preprocessed_new_data])

        sentiment_prediction = loaded_model.predict(X_new_data)

        predicted_rating = int(np.round(loaded_model.predict_proba(X_new_data)[:, 1] * 10, 0)[0])

        sentiment = 'Positive' if sentiment_prediction[0] == 1 else "'Negative"

        return predicted_rating,sentiment

