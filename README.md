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
├── src/                     # Source code modules
│   ├── __init__.py
│   ├── data_processor.py    # Data cleaning and preprocessing
│   ├── text_analyzer.py     # NLP and text processing
│   ├── trend_detector.py    # Trend identification logic
│   └── visualizer.py        # Visualization utilities
└── outputs/                 # Generated reports and visualizations
    ├── figures/             # Chart outputs
    └── reports/             # Final reports
```

## Objective
Create a metrics-driven report of trends and topics of interest, and how they shift over time, for consumers of @treehut.

## Data Description
- **Dataset**: ~18,000 Instagram comments from March 2025
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
- **Data Analysis**: pandas, numpy, scipy
- **NLP**: NLTK, spaCy, transformers
- **Visualization**: matplotlib, seaborn, plotly
- **Topic Modeling**: scikit-learn, gensim

---
*This project was completed as part of the Scrollmark coding assessment.*
