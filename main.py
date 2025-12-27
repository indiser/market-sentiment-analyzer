import requests
import time
from textblob import TextBlob

# --- CONFIGURATION ---
SUBREDDIT = "stocks" # Try: "bitcoin", "technology", "politics"
URL = f"https://www.reddit.com/r/{SUBREDDIT}/new.json?limit=50"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

print(f"🕵️  Scanning r/{SUBREDDIT} for market sentiment...\n")

try:
    response = requests.get(URL, headers=headers)
    
    if response.status_code == 429:
        print("Blocked! You are hitting them too fast. Wait a minute.")
        exit()
    elif response.status_code != 200:
        print(f"Error: {response.status_code}")
        exit()

    data = response.json()
    posts = data['data']['children']

    positive_count = 0
    negative_count = 0

    for post in posts:
        post_data = post['data']
        title = post_data['title']
        upvotes = post_data['ups']
        
        # --- THE AI BRAIN ---
        analysis = TextBlob(title)
        polarity = analysis.sentiment.polarity # Score between -1 (Bad) and +1 (Good)

        # Classify
        if polarity > 0.1:
            sentiment = "🟢 BULLISH"
            positive_count += 1
        elif polarity < -0.1:
            sentiment = "🔴 BEARISH"
            negative_count += 1
        else:
            sentiment = "⚪ NEUTRAL"

        # Only print if it's not neutral (to reduce noise)
        if sentiment != "⚪ NEUTRAL":
            print(f"[{sentiment}] {title[:60]}...")
            print(f"   Score: {polarity:.2f} | Upvotes: {upvotes}")
            print("-" * 30)

    # --- THE SUMMARY ---
    print("\n=== MARKET REPORT ===")
    print(f"Bullish Posts: {positive_count}")
    print(f"Bearish Posts: {negative_count}")
    
    if positive_count > negative_count:
        print("Verdict: 🚀 THE MARKET IS OPTIMISTIC")
    else:
        print("Verdict: 📉 THE MARKET IS FEARFUL")

except Exception as e:
    print(f"Crash: {e}")