def calculate_metrics(tweets: list) -> dict:
    """
    Calculate contribution metrics from a list of tweets.

    Args:
        tweets (list): List of tweet objects returned by fetch_tweets()

    Returns:
        dict: Aggregated metrics including:
            - tweets: total number of tweets
            - likes: total like count
            - replies: total reply count
            - retweets: total retweet count
            - quotes: total quote count
    """
    stats = {
        "tweets": len(tweets),
        "likes": 0,
        "replies": 0,
        "retweets": 0,
        "quotes": 0,
    }

    for tweet in tweets:
        metrics = tweet.get("public_metrics", {})
        stats["likes"] += metrics.get("like_count", 0)
        stats["replies"] += metrics.get("reply_count", 0)
        stats["retweets"] += metrics.get("retweet_count", 0)
        stats["quotes"] += metrics.get("quote_count", 0)

    return stats
