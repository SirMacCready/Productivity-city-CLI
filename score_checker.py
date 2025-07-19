import requests
from productivity_scoring import ScoringEngine  # ⬅️ importation ici
import os
from dotenv import load_dotenv, dotenv_values 


#defining the bucket ID in .env file
load_dotenv() 
# if not os.getenv("BUCKET_ID")
bucket_id =os.getenv("BUCKET_ID")
url = f"http://localhost:5600/api/0/buckets/{bucket_id}/events"

res = requests.get(url)
events = res.json()

engine = ScoringEngine("config.json")
total_score = 0

for event in events:
    title = event.get("data", {}).get("title", "")
    duration = event.get("duration", 0)
    total_score += engine.score(title, duration)

print(f"Score total (pondéré) en heures : {total_score / 3600:.2f}")
