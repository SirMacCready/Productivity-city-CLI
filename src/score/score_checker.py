import requests
from score.productivity_scoring import ScoringEngine
from datetime import datetime, timezone
from dateutil.parser import isoparse

def normalize_score(total_score, total_duration, max_multiplier=30):
    """
    Normalize the total score into a range between -10 and 10.
    
    The normalization scales the raw score based on the maximum
    theoretical score (total_duration * max_multiplier) and maps
    it onto a scale from -10 to 10.
    
    If total_duration is zero, returns 0 to avoid division by zero.
    """
    if total_duration == 0:
        return 0

    max_theoretical_score = total_duration * max_multiplier
    normalized = (total_score / max_theoretical_score) * 20
    # Clamp the normalized score between -10 and 10
    return max(-10, min(10, normalized))

def score_checking():
    # Initialize scoring engine with config file
    engine = ScoringEngine("./config_files/config.json")
    
    # Get today's midnight in UTC to filter today's events
    midnight = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)

    base_url = "http://localhost:5600/api/0"
    total_score = 0
    total_duration = 0

    try:
        # Fetch all bucket identifiers
        buckets = requests.get(f"{base_url}/buckets/").json()
    except Exception as e:
        print(f"Error fetching buckets: {e} | Did you turn on Activity Watcher?")
        return 1

    for bucket in buckets:
        try:
            # Fetch events for each bucket
            events = requests.get(f"{base_url}/buckets/{bucket}/events").json()
        except Exception as e:
            print(f"Error fetching events for bucket '{bucket}': {e}")
            continue

        for event in events:
            try:
                # Parse event timestamp and check if it's from today
                timestamp = isoparse(event["timestamp"])
                if timestamp < midnight:
                    continue

                # Extract duration and title safely
                duration = event.get("duration", 0)
                title = event.get("data", {}).get("title", "")

                # Score the event and accumulate results
                score = engine.score(title, duration)
                total_score += score
                total_duration += duration
            except Exception as e:
                print(f"Error processing an event: {e}")

    normalized = normalize_score(total_score, total_duration)
    return (total_score,normalized)

if __name__ == "__main__":
    score_checking()
