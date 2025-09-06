import unittest
from src.api.metrics import calculate_metrics

class TestMetrics(unittest.TestCase):

    def test_empty_tweets(self):
        # No tweets
        tweets = []
        stats = calculate_metrics(tweets)
        expected = {"tweets": 0, "likes": 0, "replies": 0, "retweets": 0, "quotes": 0}
        self.assertEqual(stats, expected)

    def test_single_tweet(self):
        tweets = [
            {
                "id": "1",
                "text": "Hello @Anoma",
                "public_metrics": {
                    "like_count": 3,
                    "reply_count": 1,
                    "retweet_count": 2,
                    "quote_count": 0
                }
            }
        ]
        stats = calculate_metrics(tweets)
        expected = {"tweets": 1, "likes": 3, "replies": 1, "retweets": 2, "quotes": 0}
        self.assertEqual(stats, expected)

    def test_multiple_tweets(self):
        tweets = [
            {"id": "1", "public_metrics": {"like_count": 2, "reply_count": 0, "retweet_count": 1, "quote_count": 0}},
            {"id": "2", "public_metrics": {"like_count": 5, "reply_count": 2, "retweet_count": 0, "quote_count":_
