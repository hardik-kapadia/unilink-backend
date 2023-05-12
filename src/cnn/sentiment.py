from pprint import pprint
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class SentimentAnalyser:
    def __init__(self) -> None:
        nltk.download(
            [
                "names",
                "stopwords",
                "twitter_samples",
                "averaged_perceptron_tagger",
                "vader_lexicon",
                "punkt",
            ]
        )

        self.vader = SentimentIntensityAnalyzer()

        pass

    def get_score(self, text):
        words = nltk.word_tokenize(text)

        stopwords = nltk.corpus.stopwords.words("english")

        words = [w for w in words if w.lower() not in stopwords]

        scores = self.vader.polarity_scores(text)

        return scores
