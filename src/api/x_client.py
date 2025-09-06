import requests
from src.utils.config import BEARER_TOKEN

BASE_URL = "https://api.twitter.com/2"  # X API v2 base URL

headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}


def get_user_id(username: str) -> str:
    """
    Fetch user ID from username (handle).
    
    Args:
        username (str): X handle without '@'
    
    Returns:
        str: user_id of the handle
    """
    url = f"{BASE_URL}/users/by/username/{username}"
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    return data["data"]["id"]


def fetch_tweets(user_id: str, start_time: str, end_time: str, query: str):
    """
    Fetch tweets from a user within timeframe that mention a sub-project.
    
    Args:
        user_id (str): author_id from get_user_id()
        start_time (str): ISO 8601 start time
        end_time (str): ISO 8601 end time
        query (str): sub-project handle (e.g., @Anoma)
    
    Returns:
        list[dict]: list of tweet objects
    """
    url = f"{BASE_URL}/tweets/search/recent"
    params = {
        "query": f"from:{user_id} {query}",
        "start_time": start_time,
        "end_time": end_time,
        "max_results": 100,
        "tweet.fields": "public_metrics,created_at,text"
    }
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json().get("data", [])
