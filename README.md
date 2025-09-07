# Scrollmark Trend Identification Project

## Overview
A comprehensive data analysis project for identifying trends and actionable insights from Instagram comments data for @treehut, a popular skincare brand.

## Project Structure
```
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore file
├── engagements.csv          # Raw data (Instagram comments)
├── notebooks/               # Jupyter notebooks for analysis
│   └── trend_analysis.ipynb # Main analysis notebook
├── src/                     # Source code modules (skeleton for future development)
│   ├── __init__.py
│   ├── data_processor.py    # Data cleaning and preprocessing (template)
│   ├── text_analyzer.py     # NLP and text processing (template)
│   ├── trend_detector.py    # Trend identification logic (template)
│   └── visualizer.py        # Visualization utilities (template)
└── outputs/                 # Generated reports and visualizations
    ├── figures/             # Chart outputs
    └── reports/             # Final reports
```

## Key Findings

✅ **Analysis Complete!** 

Our trend analysis of 17,513 Instagram comments revealed:

- **🎁 Giveaways drive 10x engagement** (5,731 comments on top post)
- **👃 Scent is #1 engagement driver** (134+ mentions of fragrance terms)
- **💰 High purchase intent** ("need" mentioned 326 times)
- **📅 Viral timing discovered** (March 21st: 3,471 comments in one day)
- **🎯 5 actionable recommendations** for immediate implementation

**📊 Results**: [Executive Summary](outputs/reports/executive_summary.md) | [Full Analysis](notebooks/trend_analysis.ipynb)

## Data Description
- **Dataset**: 17,513 Instagram comments from March-April 2025 (originally ~18K before cleaning)
- **Date Range**: March 1 - April 2, 2025
- **Posts Analyzed**: 350 unique Instagram posts
- **Fields**: 
  - `timestamp`: When the comment was posted
  - `media_id`: Unique identifier for the Instagram post
  - `media_caption`: Caption of the Instagram post
  - `comment_text`: The actual comment content

## Key Deliverables
1. **Actionable Insights & Visuals**: Data-driven recommendations for social media managers
2. **Well-Organized Codebase**: Modular, clean code with proper documentation
3. **Robust Data Pipeline**: Error handling and scalable processing
4. **Extension Plan**: Future feature roadmap

## Getting Started

### Prerequisites
- Python 3.8+
- Jupyter Notebook
- Required packages (see requirements.txt)

### Installation
```bash
# Clone the repository
git clone https://github.com/NikhilSoni15/scrollmark_test.git
cd scrollmark_test

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter notebook
jupyter notebook notebooks/trend_analysis.ipynb
```

## Analysis Approach
1. **Data Exploration**: Understanding the dataset structure and quality
2. **Text Processing**: NLP techniques for extracting meaningful insights
3. **Temporal Analysis**: Tracking trends over time
4. **Topic Modeling**: Identifying key themes and topics
5. **Sentiment Analysis**: Understanding community sentiment
6. **Engagement Patterns**: Analyzing what content performs best

## Extension Plan
- Real-time trend monitoring
- Competitor analysis integration
- Automated reporting dashboard
- Influencer identification
- Content recommendation engine

## Tools & Technologies Used
- **AI/ML Tools**: Claude 3.5 Sonnet for code assistance and analysis guidance
- **Data Analysis**: pandas, numpy
- **NLP**: NLTK, TextBlob, WordCloud
- **Machine Learning**: scikit-learn (TF-IDF, LDA topic modeling)
- **Visualization**: matplotlib, seaborn, plotly
- **Development**: Jupyter notebooks, Python virtual environment

---
*This project was completed as part of the Scrollmark coding assessment.*
