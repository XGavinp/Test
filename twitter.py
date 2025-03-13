import tweepy
import pandas as pd
import time


# Twitter API Credentials
API_KEY = "pxtIxzXwIB7bdMg8599HmdgnC"
API_SECRET = "RkzyKAr0DXA5fmjE63gtBdFZssuIzyMYcArZnTtZNNMQSbsuLb"
ACCESS_TOKEN = "1898041138268798976-LnAahXCihEX5THG2HJFVCT4aswNXUu"
ACCESS_SECRET = "utMBkH0BgmaUr9ESudojsvhJOmUjORj7zybuDWSDchlAB"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAAUlzwEAAAAAQqINPYnfODsabAuG%2Fb5wF9YdKmw%3DB5XP770O3Hx1rlI4z4weTcqAvWsfT2xbwd9HuvkIrYazNd8qzl"

# Authenticate using OAuth2
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# List of topics to fetch tweets for
topics = ["Artificial Intelligence", "Cybersecurity", "Stock Market", "Movies", "Breaking News"]

# Calculate how many tweets per topic (90 tweets total, 5 topics)
tweets_per_topic = 90 // len(topics)  # 18 tweets per topic

# Function to fetch tweets with rate limit handling
def fetch_tweets(query, count=10):
    try:
        tweets = client.search_recent_tweets(query=query, max_results=count, tweet_fields=["author_id", "created_at"])
        tweet_data = [[query, tweet.id, tweet.text, tweet.created_at] for tweet in tweets.data] if tweets.data else []
        return tweet_data
    except tweepy.errors.TooManyRequests:
        print(f"Rate limit exceeded for {query}. Moving to next topic and will retry later...")
        return None  # Indicate failure due to rate limit
    except Exception as e:
        print(f"Error fetching tweets for {query}: {e}")
        return []

# Collect tweets for all topics with handling for rate limits
all_tweets = []
remaining_topics = topics.copy()
while remaining_topics:
    for topic in remaining_topics[:]:  # Iterate over a copy to modify list safely
        result = fetch_tweets(topic, count=tweets_per_topic)
        if result is None:
            continue  # Skip topic for now, retry later
        all_tweets.extend(result)
        remaining_topics.remove(topic)  # Remove successfully fetched topic
        time.sleep(10)  # Add a 10-second delay between requests
    if remaining_topics:
        print("Waiting 15 minutes before retrying failed topics...")
        time.sleep(900)  # Wait 15 minutes before retrying failed topics

# Save to CSV
df = pd.DataFrame(all_tweets, columns=["Topic", "Tweet_ID", "Tweet_Text", "Created_At"])
df.to_csv("tweets_remaining_90.csv", index=False)

print("Tweets successfully saved to tweets_remaining_90.csv")