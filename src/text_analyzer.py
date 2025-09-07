"""
Text analysis module for Instagram comments sentiment and topic analysis.

This module handles NLP processing including sentiment analysis,
topic modeling, and keyword extraction.
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Tuple, Any
import logging
from collections import Counter
import re

# NLP imports
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from wordcloud import WordCloud
import nltk

class TextAnalyzer:
    """
    Handles text analysis tasks including sentiment analysis and topic modeling.
    
    This class provides methods for analyzing comment sentiment,
    extracting topics, and identifying key terms.
    """
    
    def __init__(self, logger=None):
        """
        Initialize the TextAnalyzer.
        
        Args:
            logger: Optional logger instance for tracking operations
        """
        self.logger = logger or logging.getLogger(__name__)
        self.sia = None
        self._download_nltk_data()
        
    def _download_nltk_data(self):
        """Download required NLTK data."""
        try:
            nltk.download('vader_lexicon', quiet=True)
            nltk.download('stopwords', quiet=True)
            self.sia = SentimentIntensityAnalyzer()
        except Exception as e:
            self.logger.error(f"Error downloading NLTK data: {str(e)}")
    
    def analyze_sentiment_vader(self, text: str) -> Dict[str, float]:
        """
        Analyze sentiment using VADER.
        
        Args:
            text: Text to analyze
            
        Returns:
            Dictionary with sentiment scores
        """
        try:
            if not self.sia:
                self.sia = SentimentIntensityAnalyzer()
            
            scores = self.sia.polarity_scores(text)
            return scores
        except Exception as e:
            self.logger.error(f"Error in VADER sentiment analysis: {str(e)}")
            return {'compound': 0, 'pos': 0, 'neu': 0, 'neg': 0}
    
    def analyze_sentiment_textblob(self, text: str) -> Dict[str, float]:
        """
        Analyze sentiment using TextBlob.
        
        Args:
            text: Text to analyze
            
        Returns:
            Dictionary with sentiment scores
        """
        try:
            blob = TextBlob(text)
            return {
                'polarity': blob.sentiment.polarity,
                'subjectivity': blob.sentiment.subjectivity
            }
        except Exception as e:
            self.logger.error(f"Error in TextBlob sentiment analysis: {str(e)}")
            return {'polarity': 0, 'subjectivity': 0}
    
    def categorize_sentiment(self, compound_score: float) -> str:
        """
        Categorize sentiment based on compound score.
        
        Args:
            compound_score: VADER compound score
            
        Returns:
            Sentiment category ('Positive', 'Negative', 'Neutral')
        """
        if compound_score >= 0.05:
            return 'Positive'
        elif compound_score <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'
    
    def extract_keywords_tfidf(self, texts: List[str], top_n: int = 20) -> List[Tuple[str, float]]:
        """
        Extract keywords using TF-IDF.
        
        Args:
            texts: List of text documents
            top_n: Number of top keywords to return
            
        Returns:
            List of (keyword, score) tuples
        """
        try:
            # Get English stopwords
            from nltk.corpus import stopwords
            stop_words = set(stopwords.words('english'))
            
            # Add custom stopwords for Instagram comments
            custom_stopwords = {'treehut', 'love', 'like', 'really', 'much', 'good', 'great'}
            stop_words.update(custom_stopwords)
            
            vectorizer = TfidfVectorizer(
                max_features=1000,
                stop_words=list(stop_words),
                ngram_range=(1, 2),
                min_df=2
            )
            
            tfidf_matrix = vectorizer.fit_transform(texts)
            feature_names = vectorizer.get_feature_names_out()
            
            # Get mean TF-IDF scores
            tfidf_scores = np.mean(tfidf_matrix.toarray(), axis=0)
            
            # Create keyword-score pairs and sort
            keyword_scores = list(zip(feature_names, tfidf_scores))
            keyword_scores.sort(key=lambda x: x[1], reverse=True)
            
            return keyword_scores[:top_n]
            
        except Exception as e:
            self.logger.error(f"Error extracting TF-IDF keywords: {str(e)}")
            return []
    
    def perform_topic_modeling(self, texts: List[str], n_topics: int = 5) -> Tuple[Any, List[List[str]]]:
        """
        Perform LDA topic modeling.
        
        Args:
            texts: List of text documents
            n_topics: Number of topics to extract
            
        Returns:
            Tuple of (LDA model, list of topic words)
        """
        try:
            from nltk.corpus import stopwords
            stop_words = set(stopwords.words('english'))
            custom_stopwords = {'treehut', 'love', 'like', 'really', 'much', 'good', 'great'}
            stop_words.update(custom_stopwords)
            
            count_vectorizer = CountVectorizer(
                max_features=1000,
                stop_words=list(stop_words),
                min_df=2,
                max_df=0.95
            )
            
            count_matrix = count_vectorizer.fit_transform(texts)
            
            lda = LatentDirichletAllocation(
                n_components=n_topics,
                random_state=42,
                max_iter=10
            )
            
            lda.fit(count_matrix)
            
            feature_names = count_vectorizer.get_feature_names_out()
            
            # Extract top words for each topic
            topics = []
            for topic_idx, topic in enumerate(lda.components_):
                top_words_idx = topic.argsort()[-10:][::-1]
                top_words = [feature_names[i] for i in top_words_idx]
                topics.append(top_words)
            
            return lda, topics
            
        except Exception as e:
            self.logger.error(f"Error in topic modeling: {str(e)}")
            return None, []
    
    def count_keyword_mentions(self, texts: List[str], keywords: List[str]) -> Dict[str, int]:
        """
        Count mentions of specific keywords.
        
        Args:
            texts: List of text documents
            keywords: List of keywords to count
            
        Returns:
            Dictionary with keyword counts
        """
        try:
            keyword_counts = {}
            
            for keyword in keywords:
                count = 0
                pattern = r'\b' + re.escape(keyword.lower()) + r'\b'
                
                for text in texts:
                    count += len(re.findall(pattern, text.lower()))
                
                keyword_counts[keyword] = count
            
            return keyword_counts
            
        except Exception as e:
            self.logger.error(f"Error counting keywords: {str(e)}")
            return {}

from typing import List, Dict, Tuple
import re


class TextAnalyzer:
    """Main class for text analysis operations."""
    
    def __init__(self):
        """Initialize the TextAnalyzer."""
        self.stop_words = set()
        self.sentiment_analyzer = None
    
    def preprocess_text(self, text: str) -> str:
        """
        Preprocess text for analysis.
        
        Args:
            text (str): Raw text to preprocess
            
        Returns:
            str: Cleaned and preprocessed text
        """
        # TODO: Implement text preprocessing
        # - Convert to lowercase
        # - Remove special characters
        # - Handle emojis
        # - Remove URLs
        pass
    
    def extract_hashtags(self, text: str) -> List[str]:
        """
        Extract hashtags from text.
        
        Args:
            text (str): Text to extract hashtags from
            
        Returns:
            List[str]: List of hashtags found
        """
        # TODO: Implement hashtag extraction
        pass
    
    def extract_mentions(self, text: str) -> List[str]:
        """
        Extract user mentions from text.
        
        Args:
            text (str): Text to extract mentions from
            
        Returns:
            List[str]: List of mentions found
        """
        # TODO: Implement mention extraction
        pass
    
    def analyze_sentiment(self, text: str) -> Dict[str, float]:
        """
        Analyze sentiment of text.
        
        Args:
            text (str): Text to analyze
            
        Returns:
            Dict[str, float]: Sentiment scores
        """
        # TODO: Implement sentiment analysis
        # - Use pre-trained model or lexicon
        # - Return sentiment scores (positive, negative, neutral)
        pass
    
    def extract_keywords(self, texts: List[str], top_n: int = 20) -> List[Tuple[str, int]]:
        """
        Extract top keywords from a collection of texts.
        
        Args:
            texts (List[str]): List of texts to analyze
            top_n (int): Number of top keywords to return
            
        Returns:
            List[Tuple[str, int]]: List of (keyword, frequency) tuples
        """
        # TODO: Implement keyword extraction
        # - TF-IDF or frequency-based
        # - Filter stop words
        # - Return top keywords
        pass
