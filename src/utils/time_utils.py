from datetime import datetime, timedelta, timezone

def get_time_range(option: str):
    """
    Convert a timeframe option into start and end ISO 8601 timestamps.
    
    Args:
        option (str): One of "24h", "7d", "30d", "90d"
    
    Returns:
        tuple: (start_time_iso, end_time_iso)
    """
    now = datetime.now(timezone.utc)

    if option == "24h":
        start = now - timedelta(hours=24)
    elif option == "7d":
        start = now - timedelta(days=7)
    elif option == "30d":
        start = now - timedelta(days=30)
    elif option == "90d":
        start = now - timedelta(days=90)
    else:
        raise ValueError(f"Invalid timeframe option: {option}")

    return start.isoformat(), now.isoformat()
