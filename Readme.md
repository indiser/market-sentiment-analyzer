# Market Sentiment Analyzer 📈

> Real-time sentiment analysis of Reddit stock market discussions using NLP and interactive visualization

[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=flat&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=flat&logo=flask)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Overview

Market Sentiment Analyzer is a full-stack application that monitors Reddit's r/stocks community to gauge market sentiment in real-time. It employs Natural Language Processing (NLP) to classify post titles as bullish, bearish, or neutral, then visualizes the sentiment distribution through an interactive dashboard.

**Perfect for traders and investors seeking alternative data on market psychology.**

---

## ✨ Features

- **Real-Time Sentiment Analysis**: Analyzes the latest 100+ posts from r/stocks using TextBlob NLP
- **Multi-Sentiment Classification**: Categorizes content into three buckets:
  - 🟢 **Bullish**: Positive market outlook (polarity > 0.1)
  - 🔴 **Bearish**: Negative market outlook (polarity < -0.1)
  - ⚪ **Neutral**: Mixed or indifferent sentiment
- **Interactive Dashboard**: Beautiful, responsive web UI built with Bootstrap 5 and Chart.js
- **Data Visualization**: Doughnut chart displaying sentiment distribution at a glance
- **Live Headlines**: Shows the 5 most recent scanned posts with their sentiment labels
- **Flexible Subreddit Support**: Easily analyze sentiment from different subreddits (stocks, bitcoin, technology, etc.)
- **CLI Tool**: Standalone Python script for headless sentiment analysis and market reports

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/market-sentiment-analyzer.git
   cd market-sentiment-analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the web application**
   ```bash
   python app.py
   ```
   
   Open your browser and navigate to `http://localhost:5000`

---

## 📖 Usage

### Web Dashboard (Flask App)

The interactive web application provides a real-time sentiment dashboard:

```bash
python app.py
```

Access the dashboard at `http://localhost:5000` to view:
- Sentiment distribution chart
- Live sentiment counts (Bullish/Bearish/Neutral)
- Latest 5 analyzed headlines with sentiment labels

### CLI Tool (Command Line)

For headless analysis and terminal-based reports:

```bash
python main.py
```

**Example output:**
```
🕵️  Scanning r/stocks for market sentiment...

[🟢 BULLISH] Stock market surges on optimistic economic data...
   Score: 0.85 | Upvotes: 2847
------------------------------
[🔴 BEARISH] Fed signals more rate hikes ahead...
   Score: -0.72 | Upvotes: 1953
------------------------------

=== MARKET REPORT ===
Bullish Posts: 34
Bearish Posts: 12
Verdict: 🚀 THE MARKET IS OPTIMISTIC
```

### Analyze Different Subreddits

Edit the `SUBREDDIT` variable in `main.py` or modify `get_sentiment()` parameter in `app.py`:

```python
get_sentiment("bitcoin")      # For Bitcoin sentiment
get_sentiment("technology")   # For Tech sector
get_sentiment("politics")     # For Political news impact
```

---

## 🏗️ Project Structure

```
market-sentiment-analyzer/
├── app.py                 # Flask web application & sentiment engine
├── main.py               # CLI tool for terminal-based analysis
├── templates/
│   └── index.html        # Interactive dashboard frontend
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

---

## 🔧 Technical Stack

| Component | Technology |
|-----------|-----------|
| Backend | Python 3.8+, Flask 2.0+ |
| NLP Engine | TextBlob |
| Data Source | Reddit API (via PRAW compatible requests) |
| Frontend | HTML5, Bootstrap 5, Chart.js |
| HTTP Client | Requests library |

---

## 📊 How Sentiment Analysis Works

1. **Data Collection**: Fetches latest posts from Reddit's r/stocks via JSON API
2. **Text Processing**: TextBlob analyzes post titles and calculates polarity scores
3. **Classification**: 
   - Polarity > 0.1 → **Bullish** 🟢
   - Polarity < -0.1 → **Bearish** 🔴
   - Between -0.1 and 0.1 → **Neutral** ⚪
4. **Visualization**: Aggregates sentiment counts and renders interactive chart

---

## ⚙️ Configuration

### Modify Request Limits
Edit the `limit` parameter in `app.py` or `main.py` (default: 50-100 posts):

```python
url = f"https://www.reddit.com/r/{subreddit}/new.json?limit=200"  # Fetch 200 posts
```

### Rate Limiting
Reddit may rate-limit requests if they're too frequent. The app includes error handling:
- 429 responses trigger a timeout message
- Adjust request frequency or add delays as needed

---

## 🎯 Use Cases

- **Retail Traders**: Gauge public sentiment before making trading decisions
- **Sentiment Research**: Study how social media sentiment correlates with market movements
- **Contrarian Analysis**: Identify potential reversal signals when sentiment is extremely bullish/bearish
- **Data Science Projects**: Source alternative data for ML models predicting market behavior

---

## 🤝 Contributing

Contributions are welcome! Ways to enhance this project:

- [ ] Add sentiment analysis for multiple subreddits simultaneously
- [ ] Implement historical sentiment tracking and trends
- [ ] Integrate additional data sources (Twitter, news APIs)
- [ ] Add advanced NLP models (VADER, DistilBERT)
- [ ] Deploy as cloud service (Heroku, AWS, GCP)
- [ ] Create mobile app interface
- [ ] Add portfolio-specific sentiment analysis

---

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details

---

## ⚠️ Disclaimer

This tool is for educational and research purposes only. Sentiment analysis is a heuristic approach and should not be used as the sole basis for investment decisions. Always conduct your own due diligence and consult financial advisors.

---

## 🙋 Support

Encountering issues? Here are common solutions:

**"Import 'textblob' could not be resolved"**
- Run: `pip install textblob`

**"Connection Error when fetching Reddit data"**
- Check your internet connection
- Reddit may be rate-limiting; wait a few minutes before retrying

**"Chart not displaying"**
- Ensure JavaScript is enabled in your browser
- Check browser console for errors (F12)

---

## 🔗 Links

- **GitHub**: [https://github.com/yourusername/market-sentiment-analyzer](https://github.com/indiser/market-sentiment-analyzer)
- **Issues**: [Report bugs here](https://github.com/indiser/market-sentiment-analyzer/issues)

---

**Made with ❤️ by Indiser**

*Last updated: December 2025*