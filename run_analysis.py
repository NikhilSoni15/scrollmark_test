#!/usr/bin/env python3
"""
Driver script for Instagram trend analysis pipeline.

This script orchestrates the entire analysis pipeline from data loading
to insight generation, demonstrating modular architecture and error handling.
"""

import sys
import os
import logging
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from data_processor import DataProcessor
from text_analyzer import TextAnalyzer

def setup_logging():
    """Configure logging for the pipeline."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('pipeline.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger(__name__)

def main():
    """Main pipeline execution."""
    logger = setup_logging()
    logger.info("Starting Instagram trend analysis pipeline")
    
    try:
        # Initialize processors
        data_processor = DataProcessor(logger)
        text_analyzer = TextAnalyzer(logger)
        
        # Define data path
        data_path = 'engagements.csv'
        
        if not os.path.exists(data_path):
            logger.error(f"Data file not found: {data_path}")
            sys.exit(1)
        
        # Step 1: Load and preprocess data
        logger.info("Step 1: Loading and preprocessing data")
        raw_data = data_processor.load_data(data_path)
        clean_data = data_processor.preprocess_data(raw_data)
        summary = data_processor.get_data_summary(clean_data)
        
        logger.info(f"Data summary: {summary['total_records']} records, "
                   f"{summary['unique_posts']} unique posts")
        
        # Step 2: Sentiment Analysis
        logger.info("Step 2: Performing sentiment analysis")
        comments = clean_data['comment_text_clean'].tolist()
        
        # Sample sentiment analysis on first 100 comments for demo
        sample_comments = comments[:100]
        sentiments = []
        
        for comment in sample_comments:
            vader_scores = text_analyzer.analyze_sentiment_vader(comment)
            textblob_scores = text_analyzer.analyze_sentiment_textblob(comment)
            
            sentiment_category = text_analyzer.categorize_sentiment(vader_scores['compound'])
            
            sentiments.append({
                'comment': comment[:50] + "..." if len(comment) > 50 else comment,
                'vader_compound': vader_scores['compound'],
                'textblob_polarity': textblob_scores['polarity'],
                'category': sentiment_category
            })
        
        # Step 3: Keyword Extraction
        logger.info("Step 3: Extracting keywords")
        keywords = text_analyzer.extract_keywords_tfidf(sample_comments, top_n=10)
        
        # Step 4: Topic Modeling
        logger.info("Step 4: Performing topic modeling")
        lda_model, topics = text_analyzer.perform_topic_modeling(sample_comments, n_topics=3)
        
        # Step 5: Generate insights
        logger.info("Step 5: Generating insights")
        
        # Sentiment distribution
        sentiment_dist = {}
        for sent in sentiments:
            category = sent['category']
            sentiment_dist[category] = sentiment_dist.get(category, 0) + 1
        
        # Results summary
        results = {
            'data_summary': summary,
            'sentiment_distribution': sentiment_dist,
            'top_keywords': keywords[:5],
            'topics': topics,
            'sample_size': len(sample_comments)
        }
        
        # Step 6: Output results
        logger.info("Step 6: Outputting results")
        print("\n" + "="*50)
        print("INSTAGRAM TREND ANALYSIS RESULTS")
        print("="*50)
        
        print(f"\n📊 Dataset Summary:")
        print(f"   Total Records: {results['data_summary']['total_records']:,}")
        print(f"   Unique Posts: {results['data_summary']['unique_posts']:,}")
        print(f"   Date Range: {results['data_summary']['date_range']['start']} to {results['data_summary']['date_range']['end']}")
        
        print(f"\n💭 Sentiment Distribution (sample of {results['sample_size']} comments):")
        for sentiment, count in results['sentiment_distribution'].items():
            percentage = (count / results['sample_size']) * 100
            print(f"   {sentiment}: {count} ({percentage:.1f}%)")
        
        print(f"\n🔑 Top Keywords:")
        for i, (keyword, score) in enumerate(results['top_keywords'], 1):
            print(f"   {i}. {keyword} (score: {score:.3f})")
        
        print(f"\n📝 Discovered Topics:")
        for i, topic_words in enumerate(results['topics'], 1):
            print(f"   Topic {i}: {', '.join(topic_words[:5])}")
        
        print("\n✅ Pipeline completed successfully!")
        print("📓 For full analysis, see notebooks/trend_analysis.ipynb")
        
        logger.info("Pipeline completed successfully")
        
    except Exception as e:
        logger.error(f"Pipeline failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
