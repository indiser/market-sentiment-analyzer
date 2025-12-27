from flask import Flask, render_template
import requests
from textblob import TextBlob

app = Flask(__name__)

def get_sentiment(subreddit="stocks"):
    url = f"https://www.reddit.com/r/{subreddit}/new.json?limit=100"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        children = data['data']['children']
        
        bullish = 0
        bearish = 0
        neutral = 0
        
        latest_posts = []

        for post in children:
            title = post['data']['title']
            score = TextBlob(title).sentiment.polarity
            
            # Simple Logic: Decide the bucket
            if score > 0.1:
                bullish += 1
                sentiment_label = "BULLISH 🟢"
            elif score < -0.1:
                bearish += 1
                sentiment_label = "BEARISH 🔴"
            else:
                neutral += 1
                sentiment_label = "NEUTRAL ⚪"
            
            # Save the top 5 posts to show on screen
            if len(latest_posts) < 5:
                latest_posts.append({"title": title, "label": sentiment_label})

        return bullish, bearish, neutral, latest_posts

    except Exception as e:
        print(f"Error: {e}")
        return 0, 0, 0, []

@app.route("/")
def home():
    # 1. Run the analysis
    bull, bear, neut, posts = get_sentiment("stocks")
    
    # 2. Send data to HTML
    return render_template("index.html", 
                           bull=bull, 
                           bear=bear, 
                           neut=neut, 
                           posts=posts)

if __name__ == "__main__":
    app.run(debug=True)